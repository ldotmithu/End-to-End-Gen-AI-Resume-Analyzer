import streamlit as st
from src.helper import get_data, get_chunks, get_embedding_vecter_index, get_rag_chain,load_embedding,load_vector
import os


st.title("Resume Analyzer Assistant")
st.write("Upload your resume in PDF format to get feedback and suggestions for improvement.")


uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    

    data = get_data("temp_resume.pdf")
    docs = get_chunks(data)
    embedding = load_embedding()
    vector_store = get_embedding_vecter_index(docs,embedding)
    
    vector_db = load_vector(path="resume_index",embedding=embedding)
    rag_chain = get_rag_chain(vector_db)
    
    st.success("Resume uploaded and processed successfully!")
    
    user_query = st.text_input("Ask a question about your resume:")
    
    if user_query:
        response = rag_chain.invoke({"input": user_query})
        
       
        st.write("**Response:**")
        st.write(response["answer"])
    
    os.remove("temp_resume.pdf")
else:
    st.info("Please upload a PDF file to proceed.")