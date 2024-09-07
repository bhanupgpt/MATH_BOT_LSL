from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize the streamlit app
st.set_page_config(page_title="Demo")
st.header("Application")

st.subheader("Select the Subject, Grade, Topic and Content you want to generate")
subject = st.selectbox("Select Subject", ["Math", "Science", "History"])
grade = st.selectbox("Select Grade", ["Grade 6", "Grade 7", "Grade 8"])
topic = st.selectbox("Select Topic", ["prime factorization", "probability", "pythagoras theorem"])
content = st.selectbox("Select content", ["10 practice problems", "lesson plan", "detailed notes"])

st.write(f"You selected {subject} for {grade} on {topic}.")
st.write(f"You want to generate {content}.")
input = f"Generate a {topic} {content} for {subject} at {grade} level."

# input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)  
    