# Chatbot with RAG using LangChain and OpenAI

This is a basic console project for creating chatbots with RAG using **LangChain** and OpenAI's **language model**. You can save **PDFs** in a folder and have the chatbot respond with information extracted from them.

## 1. Prerequisites

Ensure you have the following installed:

- **Python 3.12.5**
- **Git** (optional) for cloning repositories and managing the code

## 2. Environment Setup

### Clone the repository or extract the project
If you received the project as a **ZIP file**, extract it to a directory of your choice.

Navigate to the project directory:


chatbot_rag_langchain/
 ├── src/
 │   ├── chatbot.py          # Contains chatbot logic
 │   ├── main.py             # Main entry point of the project
 │   ├── rag_pipeline.py     # Handles the RAG (Retrieval-Augmented Generation) pipeline
 ├── config/
 │   ├── config.py           # Configuration settings for the project
 ├── data/
 │   ├── pdfs/               # Directory where PDFs are stored for analysis or retrieval
 ├── requirements.txt        # Dependencies required for the project
 ├── .env                    # Environment variables (API keys, paths, etc.)
