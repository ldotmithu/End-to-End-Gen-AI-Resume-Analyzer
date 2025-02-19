# Resume Analyzer Application

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-FF6F61?style=for-the-badge&logo=LangChain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00B388?style=for-the-badge&logo=Groq&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD43B?style=for-the-badge&logo=HuggingFace&logoColor=black)

An AI-powered Resume Analyzer application built with **Streamlit**, **LangChain**, and **Groq**. This application analyzes resumes in PDF format, provides feedback on strengths and areas for improvement, and allows users to interact with an AI assistant for tailored suggestions.

---

## Features

- **Resume Analysis**: Upload a PDF resume and get instant feedback on its structure, skills, and alignment with industry standards.
- **AI-Powered Feedback**: Leverages advanced **NLP** and **RAG** techniques to provide actionable suggestions for improvement.
- **Interactive Assistant**: Ask specific questions about your resume and receive detailed, context-aware responses.
- **User-Friendly Interface**: Built with Streamlit for a seamless and intuitive user experience.

---

## How It Works

1. **Upload Resume**: Users upload their resume in PDF format.
2. **Data Processing**: The application processes the resume, splits it into manageable chunks, and creates an embedding vector index using HuggingFace embeddings.
3. **AI Analysis**: The application uses a RAG (Retrieval-Augmented Generation) chain powered by Groq's LLM to analyze the resume and generate feedback.
4. **Interactive Q&A**: Users can ask specific questions about their resumes, such as identifying key skills, suggesting improvements, or aligning the resume with industry standards.
5. **Feedback Display**: The application displays the analysis and responses in a clear, structured format.

---

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **LangChain**: For chaining NLP components and integrating with Groq's LLM.
- **Groq**: For leveraging the powerful `llama-3.3-70b-versatile` model for resume analysis.
- **HuggingFace Embeddings**: For creating vector embeddings of the resume content.
- **FAISS**: For efficient similarity search and retrieval of resume chunks.
- **PyPDF2**: For extracting text from PDF resumes.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ldotmithu/End-to-End-Gen-AI-Resume-Analyzer.git
   cd End-to-End-Gen-AI-Resume-Analyzer

2. Install dependencies
     ```bash
     pip install -r requirements.txt
3. Run the application:
    ```bash
    streamlit run app.py

