import os
from apikey import apikey
os.environ["OPENAI_API_KEY"] = apikey

import streamlit as st
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

# App framkework
st.title('Chat with PDF')

# Upload PDF file
pdf_file = st.file_uploader('Upload your PDF file')

# If PDF is uploaded then provide instruction prompt
prompt = ""
if pdf_file:
    prompt = st.text_input('What would you like to do with your PDF?')

