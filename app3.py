import streamlit as st # App framework
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader  # read pdf

from langchain.text_splitter import RecursiveCharacterTextSplitter # To divide text in multiple chunks



# App framework

## Sidebar
with st.sidebar:
    st.title("ChatPDF")
    st.markdown('''
    ## About this application is built using:
    - streamlit
    - Langchain
    - OpenAI        
    ''')

    add_vertical_space(5)
    st.write('Made by Saif💫')


# Runner code
def main():
    st.header('Chat with your application📖')
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
        st.write(chunks)


if __name__ == '__main__':
    main()