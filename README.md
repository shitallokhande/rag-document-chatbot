# RAG Document Question Answering Chatbot

This project implements a Retrieval Augmented Generation (RAG) chatbot that answers questions from PDF documents. The system loads PDF documents, splits text into chunks, converts text into embeddings, stores embeddings in a FAISS vector database, retrieves relevant document chunks, and generates answers using a local LLM.

## Features
- PDF document loading
- Text chunking
- Embeddings using HuggingFace
- Vector database using FAISS
- Semantic search
- Retrieval Augmented Generation (RAG)
- Question answering from documents

## Technologies Used
- Python
- LangChain
- HuggingFace
- FAISS
- Transformers
- Streamlit (optional)

## How It Works
1. Load PDF document
2. Split document into chunks
3. Convert text to embeddings
4. Store embeddings in vector database
5. Retrieve relevant chunks
6. Generate answer using LLM

## Run Project

pip install -r requirements.txt
python app.py

Project Architecture
PDF Document → Text Chunking → Embeddings → FAISS Vector DB
                                      ↓
User Question → Embedding → Similar Chunks → LLM → Answer
Example Questions
What is Artificial Intelligence?
Summarize the document
What is RAG?
Explain Machine Learning
Future Improvements
Add Streamlit UI
Support multiple PDFs
Add chat history
Deploy as web app
