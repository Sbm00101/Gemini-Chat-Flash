from dotenv import load_dotenv
load_dotenv() ##loading all env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

##Function to  load Gemini pro model

model = genai.GenerativeModel("gemini-1.5-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.header("Gemini Application")
input = st.text_input("Input : ", key="input")
submit = st.button("Ask your question")

if(submit):
    response = get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response)

