
# **AI-Powered Japanese Learning Platform**  

## **Overview**  
This project is focused on building an **AI-powered Japanese language learning system**, designed to run on **self-hosted infrastructure** to minimize cloud costs while keeping **privacy and security in check**. We’re starting with **Japanese**, but the long-term goal is to **expand into Chinese**.  

The system provides various **study activities**, leveraging **open-source LLMs** and **Retrieval-Augmented Generation (RAG)** to help students improve their vocabulary, sentence construction, and immersion in the language.  

---

## **Functional Requirements**  
- **Self-hosted AI**: The system will run on **our own hardware** (AI PC, ~$10K–$15K budget) instead of cloud-based services to keep **costs low and data private**.  
- **80B parameter LLM**: We’re using an **80B parameter open-source LLM** for better **long-term scalability**, especially as we expand into **Chinese**.  
- **Study Activities**: Students will interact with a **Lang Portal** that includes:  
  - Writing Practice  
  - Text Adventure Immersion  
  - Light Visual Novel Reading  
  - Sentence Constructor (AI-powered)  
  - Visual Flashcard Vocabulary  
  - Speak-to-Learn  
- **Retrieval-Augmented Generation (RAG)**: The **Sentence Constructor** feature will **pull data** from a **structured vocabulary database** to ensure **accurate sentence formation**.  
- **Guardrails & Security**: Input/output guardrails will be in place to **filter inappropriate content** and ensure a **safe learning environment**.  

---

## **Assumptions**  
- The **80B parameter LLM** should be **efficient enough** for our use case while **keeping expansion in mind**.  
- A **single AI PC setup** will be enough to support our **300 active students** in **Nagasaki**, with a **stable internet connection** for online interactions.  
- **Open-source models** will be used wherever possible, but we’ll also implement **security layers** to ensure no student data is exposed or stored without consent.  
- **Student age range varies**, so we’ll need **content filtering** and **context-aware AI responses** to **maintain appropriate interactions**.  
- We are prioritizing **hardware efficiency**—since we are avoiding cloud solutions due to **budget constraints**, our system should be **optimized for local processing**.  

---

## **Data Strategy**  
- **No scraping or external datasets**—we will **curate and purchase** learning materials to **avoid copyright issues** and store them in a **secure internal database**.  
- **Student study history will not be stored**, and we won’t be **training the model on user-generated data** to prevent any **privacy concerns**.  
- The **core 2000-word vocabulary database** will be used to **reinforce AI-generated responses**, making sure they align with **Japanese language learning best practices**.  
- We will **update the database** regularly to **expand the vocabulary, sentence structures, and grammar rules** while keeping track of content accuracy.  
- **Prompt filtering & moderation** will be in place to **ensure AI-generated content remains educationally relevant**.  

---

## **Considerations**  
- **IBM Granite** is a strong contender for our model since it’s **truly open-source**, with **traceable training data**, making it easier to **avoid copyright risks**.  
- Since we are **self-hosting**, we need to **optimize for compute efficiency**—the AI PC should be powerful enough to handle **LLM inference** within our **hardware limits**.  
- **Network bandwidth & latency** could be a factor as we **scale up**, so we need to keep an eye on **performance monitoring**.  
- If the **student base grows**, we may need to **re-evaluate our infrastructure** and decide whether to **scale hardware or explore hybrid solutions**.  
- **Compliance & privacy regulations** (e.g., GDPR-like policies in Japan) should be considered, especially for **user-generated content handling**.  

---

## **Tech Stack**  
- **LLM Model**: IBM Granite (open-source)  
- **Backend**: Retrieval-Augmented Generation (RAG)  
- **Database**: Internal word bank (Core 2000 Words)  
- **Security**: Input/Output Guardrails for content moderation  
- **Hardware**: AI PC with a $10K–$15K budget  

---

## **Future Plans**  
- **Scale to support Chinese language learning**  
- **Expand the vocabulary database beyond 2000 core words**  
- **Improve AI responses with better prompt engineering**  
- **Explore additional open-source AI models** for performance gains  

---

### **License**  
This project follows an **open-source model**, but **all educational materials and datasets used are licensed** accordingly.  
