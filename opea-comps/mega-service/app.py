from fastapi import HTTPException
from comps.cores.proto.api_protocol import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletionResponseChoice,
    ChatMessage,
    UsageInfo
)
from comps.cores.mega.constants import ServiceType, ServiceRoleType
from comps import MicroService, ServiceOrchestrator
import os

class MultiServiceOrchestrator:
    def __init__(self, host="0.0.0.0", port=8000):
        os.environ["TELEMETRY_ENDPOINT"] = ""
        self.host = host
        self.port = port
        self.endpoint = "/v1/multi-service"
        self.megaservice = ServiceOrchestrator()

    def setup_services(self):
        # Add Ollama LLM service
        llm = MicroService(
            name="llm",
            host=os.getenv("LLM_SERVICE_HOST_IP", "0.0.0.0"),
            port=int(os.getenv("LLM_SERVICE_PORT", 9000)),
            endpoint="/v1/chat/completions",
            use_remote_service=True,
            service_type=ServiceType.LLM,
        )

        # Add embedding service
        embedding = MicroService(
            name="embedding",
            host=os.getenv("EMBEDDING_SERVICE_HOST_IP", "0.0.0.0"),
            port=int(os.getenv("EMBEDDING_SERVICE_PORT", 6000)),
            endpoint="/v1/embeddings",
            use_remote_service=True,
            service_type=ServiceType.EMBEDDING,
        )

        # Add services to orchestrator
        self.megaservice.add(llm).add(embedding)
        # Create flow: embedding -> llm
        self.megaservice.flow_to(embedding, llm)

    async def handle_request(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        try:
            # Process text through both services
            result = await self.megaservice.schedule({
                "text": request.messages,
                "model": request.model or "llama3.2:1b"
            })
            
            # Extract response
            content = self._process_response(result)
            
            return ChatCompletionResponse(
                model=request.model,
                choices=[
                    ChatCompletionResponseChoice(
                        index=0,
                        message=ChatMessage(role="assistant", content=content),
                        finish_reason="stop"
                    )
                ],
                usage=UsageInfo(
                    prompt_tokens=0,
                    completion_tokens=0,
                    total_tokens=0
                )
            )
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def _process_response(self, result):
        # Process both embedding and LLM responses
        if isinstance(result, tuple) and len(result) > 1:
            embedding_response = result[0].get('embedding/MicroService', {})
            llm_response = result[1].get('llm/MicroService', {})
            
            # Combine responses
            return f"Embedding: {embedding_response}\nLLM: {llm_response}"
        return "Invalid response format"

    def start(self):
        service = MicroService(
            self.__class__.__name__,
            service_role=ServiceRoleType.MEGASERVICE,
            host=self.host,
            port=self.port,
            endpoint=self.endpoint,
            input_datatype=ChatCompletionRequest,
            output_datatype=ChatCompletionResponse,
        )

        service.add_route(self.endpoint, self.handle_request, methods=["POST"])
        service.start()

# Start the orchestrator
orchestrator = MultiServiceOrchestrator()
orchestrator.setup_services()
orchestrator.start()