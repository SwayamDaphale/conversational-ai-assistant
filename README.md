# conversational-ai-assistant
A conversational AI assistant built with LangChain, FastAPI, Streamlit, and Groq, featuring persistent chat history and multi-session conversations.
# 🤖 Conversational AI Assistant

A production-oriented Conversational AI Assistant built using **LangChain**, **Streamlit**, **OpenAI/Groq APIs**, **LangSmith**, and later **RAG**, **Memory**, **Agents**, and **MCP**.

This repository is not just a chatbot; it is being developed as a complete learning project that gradually evolves into a production-ready AI assistant while following modern AI engineering practices.

---

# 📌 Project Vision

The objective of this project is to learn and implement every important component required for building modern LLM applications.

Instead of creating everything at once, the project follows an incremental development workflow.

Each module builds upon the previous one.

Eventually, this repository will become a complete AI Assistant capable of

- Conversational Chat
- Long-Term Memory
- Document Question Answering
- Retrieval Augmented Generation (RAG)
- Multi-Agent Workflows
- Tool Calling
- MCP Integration
- Deployment

---

# 🏗 Overall Architecture

```

                    User Query
                         │
                         ▼
              ┌────────────────────┐
              │    Streamlit App    │
              │  (Frontend / UI)    │
              └─────────┬───────────┘
                        │
                        ▼
                Prompt Engineering
                        │
                        ▼
          ┌─────────────────────────┐
          │     LangChain Pipeline   │
          └──────────┬──────────────┘
                     │
                     ▼
              OpenAI / Groq API
                     │
                     ▼
          GPT-4o / GPT-4 / GPT-4 Turbo
          Llama 3.3 70B / GPT OSS 20B
                     │
                     ▼
                AI Response
                     │
                     ▼
                 Streamlit UI

                     │
                     ▼
                 LangSmith
          ├── Monitoring
          ├── Debugging
          ├── Tracing
          ├── Cost Analysis
          └── Performance Metrics

```

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Backend

- Python
- LangChain
- LangGraph (Upcoming)

## LLM Providers

### OpenAI

- GPT-4o
- GPT-4 Turbo
- GPT-4

### Groq

- Llama 3.3 70B
- GPT OSS 20B
- GPT OSS 120B

### Local Models (Ollama)

- Llama 3
- Gemma 2
- Mistral
- Qwen
- DeepSeek
- Phi

---

# 📂 Current Project Workflow

```

User
 │
 ▼
Streamlit Interface
 │
 ▼
Prompt Template
 │
 ▼
LLM API
 │
 ▼
Generated Response
 │
 ▼
Display Response

```

---

# 📈 Future Workflow

```

User Query
      │
      ▼
Input Validation
      │
      ▼
Prompt Engineering
      │
      ▼
Conversation Memory
      │
      ▼
Retriever
      │
      ▼
Vector Database
      │
      ▼
Relevant Context
      │
      ▼
LLM
      │
      ▼
Output Parser
      │
      ▼
Response Validation
      │
      ▼
Streamlit UI

```

---

# 📁 Project Structure

```

Conversational-AI-Assistant/

│

├── .env
├── requirements.txt
├── README.md
├── .gitignore

│

├── app/
│   ├── streamlit_app.py
│   ├── chatbot.py
│   ├── prompt.py
│   ├── chains.py
│   └── utils.py

│

├── notebooks/
│   ├── intro_chatbot.ipynb
│   ├── vectorstore.ipynb
│   ├── conversation.ipynb
│   └── rag.ipynb

│

├── data/

├── embeddings/

├── vectorstore/

├── agents/

├── memory/

├── tools/

├── prompts/

├── config/

├── logs/

└── docs/

```

---

# 🚀 Development Workflow

## Phase 1

### Project Setup

- Create Project
- Create Virtual Environment
- Install Dependencies
- Configure Git
- Configure VS Code

---

## Phase 2

### Environment Variables

Store

- OpenAI API Key
- Groq API Key
- LangSmith API Key
- HuggingFace Token

inside

```
.env
```

---

## Phase 3

### Install Dependencies

Example

```
langchain
langchain-core
langgraph
streamlit
openai
langchain-openai
langchain-groq
langsmith
python-dotenv
chromadb
faiss-cpu
sentence-transformers
langchain-huggingface
langchain-community
```

---

## Phase 4

### Streamlit Interface

Current Features

- User Input
- Response Generation

Upcoming

- Chat History
- Sidebar
- Session Management
- File Upload
- Voice Input

---

## Phase 5

### LLM Integration

Supported Providers

- OpenAI
- Groq
- Ollama

Future

- Claude
- Gemini
- Azure OpenAI

---

## Phase 6

### LangSmith Integration

LangSmith will be used for

- Prompt Debugging
- Chain Visualization
- Token Usage
- Cost Tracking
- Performance Monitoring
- Latency Analysis

---

# 🗂 Upcoming Roadmap

## Stage 1

- Basic Chatbot

---

## Stage 2

- Prompt Templates

---

## Stage 3

- Output Parsers

---

## Stage 4

- Conversation Memory

---

## Stage 5

- Chat History

---

## Stage 6

- Embeddings

---

## Stage 7

- Vector Databases

- ChromaDB
- FAISS

---

## Stage 8

- Document Loader

---

## Stage 9

- Text Splitter

---

## Stage 10

- Retrieval Augmented Generation (RAG)

---

## Stage 11

- Hybrid Search

---

## Stage 12

- Multi Query Retriever

---

## Stage 13

- Parent Document Retriever

---

## Stage 14

- Context Compression

---

## Stage 15

- Tool Calling

---

## Stage 16

- Agents

- ReAct Agent
- Tool Agent
- Multi-Agent

---

## Stage 17

- LangGraph

- Stateful Graph
- Conditional Edges
- Memory
- Human-in-the-loop

---

## Stage 18

- MCP (Model Context Protocol)

---

## Stage 19

- Local Models using Ollama

- Llama
- Gemma
- Mistral
- Qwen

---

## Stage 20

- Deployment

- Docker
- FastAPI
- Nginx
- Render
- Railway
- AWS

---

# 🔍 Monitoring

Using **LangSmith**

✔ Prompt Tracing

✔ Chain Visualization

✔ Cost Analysis

✔ Token Usage

✔ Execution Time

✔ Latency

✔ Errors

✔ Debugging

---

# 🎯 Learning Objectives

This project covers

- Prompt Engineering
- LangChain
- LangGraph
- LLM APIs
- Streamlit
- RAG
- Embeddings
- Vector Databases
- Memory
- Agents
- Tool Calling
- MCP
- Production Deployment

---

# 📌 Long-Term Goal

Transform this repository from a simple chatbot into a production-grade AI assistant capable of

- Chatting naturally
- Remembering conversations
- Understanding uploaded documents
- Searching external knowledge
- Calling APIs and tools
- Running autonomous agents
- Working with local and cloud LLMs
- Supporting multimodal inputs
- Deploying as a scalable production application

This repository serves as a complete end-to-end journey for learning modern AI engineering and building real-world LLM applications.