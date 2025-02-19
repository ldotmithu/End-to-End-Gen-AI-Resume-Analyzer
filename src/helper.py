import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader,PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chat_models import ChatGooglePalm
from langchain.embeddings import GooglePalmEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from PyPDF2 import PdfReader

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#llm 
llm = ChatGroq(
    model='llama-3.3-70b-versatile',
    temperature=0.3
)

# def get_pdf_text(pdf_docs):
#     text=""
#     for pdf in pdf_docs:
#         pdf_reader= PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text+= page.extract_text()
#     return  text

def get_data(uploaded_file):
    loader = PyPDFLoader(uploaded_file)  # Use the file directly here
    data = loader.load()
    return data

def get_chunks(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                   chunk_overlap = 200)
    docs = splitter.split_documents(data)
    return docs

def load_embedding():
    embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embedding

def get_embedding_vecter_index(docs,embedding):
    vecter_store = FAISS.from_documents(documents=docs,
            embedding=embedding)
    vecter_store.save_local("resume_index")
    return vecter_store

def load_vector(path,embedding):
    vector_db =FAISS.load_local(path,embeddings=embedding,allow_dangerous_deserialization=True)
    return vector_db


def get_rag_chain(vector_db):
    system_prompt = (
    """
    You are a Resume Analyzer Assistant. Your job is to evaluate resumes and provide clear, insightful feedback on skills, occupation, and overall structure. 
    Identify strengths, suggest improvements, and ensure alignment with industry standards. Offer concise and actionable recommendations to enhance career opportunities.

    If the user asks about something not available in the resume, generate a reasonable answer based on common industry standards.

    If the user's question is not relevant to resume analysis, simply say: 
    "I don't know. This question is not relevant for me. I am here to help you analyze and improve your resume."

    ### Example Format:
    - ✅ Clear experience in software development  
    - ✅ Strong skills in Python and SQL  
    
    Always maintain a professional and helpful tone.
    "\n\n"
    "{context}"
    """
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_prompt),
        ("human","{input}"),
    ])
    retriever = vector_db.as_retriever()
    qa_chain = create_stuff_documents_chain(llm=llm,prompt=prompt)
    rag_chain= create_retrieval_chain(retriever,qa_chain)
    return rag_chain
    

