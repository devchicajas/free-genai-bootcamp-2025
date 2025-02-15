# OPEA Implementation with Ollama 🚀

## Quick Navigation 🧭
- [Introduction](#1-introduction-what-are-we-building)
- [Setup Guide](#3-setup--installation)
- [Usage Guide](#4-usage-guide)
- [Troubleshooting](#5-troubleshooting)
- [Testing](#6-testing-guide)
- [Advanced Features](mega-service/README.md)

## 1. Introduction: What Are We Building? 🎯
We're creating a system that can run AI models locally (on your computer) instead of using cloud services like ChatGPT. Think of it like having your own mini-AI assistant that runs on your machine!

## 2. Technical Overview 🔍

### 2.1 Components
#### Docker 📦
- **What is it?** Think of Docker like a shipping container for software
- **Why use it?** Makes sure our AI runs the same way on every computer
- **How we use it:** To run Ollama in a controlled environment

#### Ollama 🤖
- **What is it?** Software that runs AI models locally
- **Why use it?** Lets us run AI without internet/cloud services
- **Current model:** Using "Mistral" (a smaller, faster AI model)

### 2.2 System Architecture
```
┌─────────────────────────────┐
│        Your Computer        │
│                             │
│  ┌─────────────────────┐    │
│  │   Docker Desktop    │    │
│  │  ┌─────────────┐   │    │
│  │  │   Ollama    │   │    │
│  │  │    (AI)     │   │    │
│  │  └──────┬──────┘   │    │
│  │         │          │    │
│  └─────────┼──────────┘    │
│            │               │
│     Port 8008              │
└────────────┼───────────────┘
             │
      Your Commands
```

### 2.3 How It Works
```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│   You    │ → │  Docker  │ → │  Ollama  │ → │   AI     │
│  (curl)  │    │ (8008)   │    │ (Model)  │    │Response │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

## 3. Setup & Installation 🛠️

### 3.1 First Time Setup
```bash
# Go to the project folder
cd opea-comps

# Start Docker
docker compose up
```

### 3.2 Download AI Model
```bash
# Download Mistral model
curl http://localhost:8008/api/pull -d '{
  "model": "mistral"
}'
```

### 3.3 Configuration
```yaml
# docker-compose.yml
version: '3.8'
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "8008:11434"
```

## 4. Usage Guide 🔨

### 4.1 Basic Commands
```bash
# Talk to the AI
curl http://localhost:8008/api/generate -d '{
  "model": "mistral",
  "prompt": "Hello, how are you?"
}'
```

### 4.2 API Endpoints
1. `/api/pull` - Downloads models
2. `/api/generate` - Creates AI responses
3. `/api/tags` - Lists available models

## 5. Troubleshooting 🔧

### 5.1 Common Issues & Solutions

#### Docker Issues
```bash
# Error: Cannot connect to Docker daemon
# Fix: Start Docker Desktop and wait for it to initialize

# Error: Port already in use
# Fix: Find and stop the process using port 8008
lsof -i :8008
```

#### Ollama Issues
```bash
# Error: Model not found
# Fix: Pull the model first
curl http://localhost:8008/api/pull -d '{"model": "mistral"}'

# Error: Generation failed
# Fix: Restart the service
docker compose restart
```

### 5.2 Quick Fixes
```bash
# Full system reset
docker compose down
docker system prune -f
docker compose up

# Check system health
curl http://localhost:8008/api/version
```

### 5.3 System Flow
```
┌─────────────┐
│ Start Here  │
└──────┬──────┘
       ▼
┌──────────────┐
│ Docker       │  ←── If fails: Check Docker Desktop
└──────┬───────┘
       ▼
┌──────────────┐
│ Pull Model   │  ←── If fails: Check internet
└──────┬───────┘
       ▼
┌──────────────┐
│ Generate Text│  ←── If fails: Check model loaded
└──────┬───────┘
       ▼
┌──────────────┐
│  Success!    │
└──────────────┘
```

## 6. Testing Guide 🧪

### 6.1 Health Checks
```bash
# Version check
curl http://localhost:8008/api/version

# Model check
curl http://localhost:8008/api/tags
```

### 6.2 Full System Test
```bash
# Generate response
curl http://localhost:8008/api/generate -d '{
  "model": "mistral",
  "prompt": "Test message"
}'
```

## 7. Current Status & Next Steps 🎯

### 7.1 Working Features ✅
- Docker container setup
- Ollama integration
- Basic text generation
- Model management

### 7.2 In Development 🔄
- Multiple service orchestration
- Enhanced error handling
- Performance optimization

### 7.3 Future Improvements 📋
- Save models permanently
- Web interface
- Better error messages
- More AI models

## 8. Advanced Features 🌟

### 8.1 Multi-Service Orchestration
We're implementing a multi-service setup that combines:
- Ollama LLM service
- Embedding service
- Service orchestration

📚 **Detailed Documentation:**
- [Multi-Service Setup & Configuration](mega-service/README.md#how-it-works)
- [Architecture Details](mega-service/README.md#architecture)
- [Technical Specifications](mega-service/README.md#technical-details)