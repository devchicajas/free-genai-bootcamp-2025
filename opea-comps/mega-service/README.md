# Multi-Service Orchestration with OPEA 🚀

## Quick Navigation 🧭
- [← Back to Main Guide](../README.md)
- [How It Works](#how-it-works)
- [Features](#features)
- [Technical Details](#technical-details)

> 📌 **Quick Links:**
> - [Main Project Setup](../README.md#3-setup--installation)
> - [Basic Usage](../README.md#4-usage-guide)
> - [Troubleshooting](../README.md#5-troubleshooting)

This implementation demonstrates orchestrating multiple AI services:
- Ollama LLM for text generation
- Sentence Transformers for embeddings

## How It Works 🔄

1. Start the services:
```bash
docker compose up
```

2. Test the orchestrated services:
```bash
curl -X POST http://localhost:8000/v1/multi-service \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:1b",
    "messages": "Analyze this text and provide embeddings"
  }'
```

## Architecture 🏗️

- Ollama Service: Handles text generation
- Embedding Service: Creates text embeddings
- Orchestrator: Manages service flow and communication

## Features ✨

1. Service Flow Control
2. Error Handling
3. Response Processing
4. Easy Configuration

## Technical Details 📝

- Uses OPEA's ServiceOrchestrator
- Implements service flow patterns
- Handles both sync and async operations

## See Also 👀
- [Main Project Documentation](../README.md)
- [Basic Setup Guide](../README.md#3-setup--installation)
- [Testing Guide](../README.md#6-testing-guide)