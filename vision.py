from dotenv import load_dotenv

load_dotenv()  # loading all env variables

import streamlit as st
import os
import google.generativeai as genai
import PIL.Image

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to load Gemini model and get response
def get_gemini_response(question, image=None):
    if image:
        img = PIL.Image.open(image)
        response = model.generate_content([question, img], stream=True)
    else:
        response = model.generate_content([question], stream=True)

    response.resolve()
    return response.text


# Function to handle the input and image submission
def handle_submit():
    if st.session_state.input:
        response = get_gemini_response(st.session_state.input, uploaded_image)
        st.session_state.response = response
    else:
        st.session_state.response = "Please enter a question."


# Streamlit frontend
st.header("Gemini-SBM-Chat")

# Image upload section
uploaded_image = st.file_uploader("Upload an image (optional):", type=["jpg", "jpeg", "png"])

# Text input section with on_change callback
st.text_input("Ask your question:", key="input", on_change=handle_submit)

# Display the response when available
if "response" in st.session_state:
    st.subheader("The response is:")
    st.write(st.session_state.response)
