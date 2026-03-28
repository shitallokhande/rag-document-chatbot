import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline

from transformers import pipeline

# Load PDF
loader = PyPDFLoader("documents/sample.pdf")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Embeddings
embeddings = HuggingFaceEmbeddings()

# Vector DB
db = FAISS.from_documents(docs, embeddings)

# Local LLM
pipe = pipeline("text2text-generation", model="google/flan-t5-base")
llm = HuggingFacePipeline(pipeline=pipe)

# RAG chain
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Ask question
query = input("Ask a question: ")
result = qa.run(query)

print("\nAnswer:", result)