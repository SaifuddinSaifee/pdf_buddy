import streamlit as st # App framework
from streamlit_extras.add_vertical_space import add_vertical_space

from PyPDF2 import PdfReader  # Read pdf
import pickle
import openai

from langchain.text_splitter import RecursiveCharacterTextSplitter # To divide text in multiple chunks
from langchain.embeddings.openai import OpenAIEmbeddings # To form embeddings of the chunks
from langchain.vectorstores import FAISS # To store embedding to vector store
from langchain.llms import OpenAI # OpenAI LLM
from langchain.chains.question_answering import load_qa_chain # Langchain Chain for QnA
from langchain.callbacks import get_openai_callback # Get price of each API call

import os
# from apikey import OPENAI_API_KEY
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# App framework

# Runner code
def main():
    st.header('Ask your pdf📖')
    pdf_file = st.file_uploader('Upload your PDF file') # Take in PDF File

    if pdf_file:
        pdf_reader = PdfReader(pdf_file) # Read the file

        text = "" # Entire text of the document

        for page in pdf_reader.pages: # Each page is treated as individual object of text | pages is a list of page objects
            text += page.extract_text() # Use extract_text() to extract text from single page object
        # st.write(text)

      # Converting to chunks since GPT and other models have input token limits
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(text=text)
        # st.write(chunks)

      # OpenAI Embedding (Optional)
        # emedding = OpenAIEmbeddings() # Embedding (sequencing and indexing) the text for machine to make some sense

        # Vectorize
        # VectorStore = FAISS.from_texts(chunks, embedding=emedding) # Vector is a data structure that ML Models understand | This line of code arranges the embeddings in vector datastructure.

        # Here we are optimizing our embedding process so that we don't accidently unprecedented API calls

        store_name = pdf_file.name[:-4]

      # Storing the Vector store in {pdfname}.pkl file with "binary write" accecss
        # We use `with` keyword to make sure the file is secured after the Vectoor storing is complete

        # If we already have the VectorStore embedding, execute this and just reload it in file f
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", 'rb') as f:
                VectorStore = pickle.load(f)
            st.write("Embedding fetch from the disk")
        
        # Else create embeddings of the chunks and create a new pkl file to store the VectorStore in binary
        else:
            embedding = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embedding)

            with open(f"{store_name}.pkl", 'wb') as f:
                pickle.dump(VectorStore, f)
            st.write('Embedding stored successfully')
        

    # Accept user questions and query from front-end

        query = st.text_input("Ask your PDF🚀")

        if query:
            # Find the docs/chunks that are somehow relatable to the user query | We are also setting a limiting for the number of chunks (k=4) that will be supplied to our llms so that we don't cross token limit.
            docs = VectorStore.similarity_search(query=query, k=4)
            # st.write(docs)

            # LLM configuration
            llm = OpenAI(model_name='gpt-3.5-turbo') # By default the model is "Da-vinci" which is slightly costlier that gpt-3.5-turbo
            chain = load_qa_chain(llm=llm, chain_type="stuff")

            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                st.write(response)
            
            st.write(cb)


if __name__ == '__main__':
    main()