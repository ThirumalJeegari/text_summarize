import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
import pdfplumber

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📄 AI Text Summarizer")

option = st.radio("Choose Input Type", ["Text", "PDF"])

text = ""

if option == "Text":
    text = st.text_area("Enter text")

else:
    file = st.file_uploader("Upload PDF", type=["pdf"])
    if file:
        with pdfplumber.open(file) as pdf:
            text = "".join(page.extract_text() or "" for page in pdf.pages)

length = st.selectbox("Summary Length", ["Short", "Medium", "Detailed"])

if st.button("Summarize"):
    prompt = f"Summarize this in {length} format:\n\n{text}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)