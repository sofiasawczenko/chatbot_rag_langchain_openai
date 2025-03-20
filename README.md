# Chatbot with RAG using LangChain and OpenAI

This is a basic console project for creating chatbots with RAG using **LangChain** and OpenAI's **language model**. You can save **PDFs** in a folder and have the chatbot respond with information extracted from them.

## 1. Prerequisites

Ensure you have the following installed:

- **Python 3.12.5**
- **Git** (optional) for cloning repositories and managing the code

## 2. Environment Setup

### Clone the repository or extract the project
If you received the project as a **ZIP file**, extract it to a directory of your choice.

## 3. Installing Dependencies

With the virtual environment activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

## 4. Project Configuration
Set up environment variables in the .env file as needed. This file should contain necessary variables such as API keys, directory paths, etc.

## 5. Running the Project
To run the project, execute the main script:

```bash
python src/main.py
```

## 6. File & Folder Structure

```bash
 ├── src/
 │   ├── chatbot.py    
 │   ├── main.py           
 │   ├── rag_pipeline.py   
 ├── config/
 │   ├── config.py          
 ├── data/
 │   ├── pdfs/              
 ├── requirements.txt        
 ├── .env                    
```
Now you're ready to build, test, and enhance this chatbot.
