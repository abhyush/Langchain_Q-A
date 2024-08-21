#Q&A Chatbot
import os
import streamlit as st
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()    #This will load all the enviromemnt variables from .env file



def get_openai_response(question):
    llm = OpenAI(api_key = os.getenv("OPENAI_API_KEY"), model_name= "gpt-3.5-turbo", temperature = 0.5)
    response = llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain application")

input = st.text_input("Input", key = "input")

response = get_openai_response(input)
submit = st.button("Ask the question")


##if the submit button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)


