# This python file uses prompt templates
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = apikey

# App framkework
st.title('Book suggestion Assistant')
prompt = st.text_input('Chat with your PDF📖✨')

# Upload PDF file
pdf_file = st.file_uploader('Upload your PDF file')

# Prompt template
title_template = PromptTemplate(
    input_variables= ['topic'],
    template='Suggest me three bestselling books on genre: {topic}'
)

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Display input if there's a prompt
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)