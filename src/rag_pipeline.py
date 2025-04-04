# Implementação do pipeline RAG
from config.config import OPENAI_API_KEY
from langchain.chains import create_retrieval_chain 
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
import openai

openai.api_key = OPENAI_API_KEY
llm = ChatOpenAI(model="gpt-4o")

# Função principal de QA (perguntas e respostas)
def answer_question(question):
    # Carregar o documento PDF
    loader = PyPDFLoader("data/document.pdf")
    docs = loader.load()

    # Criar embeddings e o FAISS vectorstore
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    # Definir o prompt do sistema
    system_prompt = (
        "Você é um assistente para tarefas de perguntas e respostas. "
        "Use os seguintes trechos de contexto recuperado para responder "
        "à pergunta. Se você não souber a resposta, diga que não sabe. "
        "Use no máximo três frases e mantenha a resposta concisa."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # Criar o chain de resposta de perguntas
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    # Invocar a resposta
    response = rag_chain.invoke({"input": question})

    return response["answer"]