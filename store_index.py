from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Chroma
persist_directory = 'db'


#Creating Embeddings for Each of The Text Chunks & storing
vectordb = Chroma.from_documents(documents=text_chunks,embedding=embeddings,persist_directory=persist_directory)