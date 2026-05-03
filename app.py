import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

from utils import extract_text_from_pdf, chunk_text

# Load API key
load_dotenv()
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
st.set_page_config(page_title="Text Summarizer", layout="wide")

st.title("📄 AI Text & PDF Summarizer")

# ---------------- INPUT ----------------
option = st.radio("Choose Input Type", ["Text", "PDF Upload"])

text = ""

if option == "Text":
    text = st.text_area("Paste your text here", height=300)

elif option == "PDF Upload":
    file = st.file_uploader("Upload PDF", type=["pdf"])
    if file:
        text = extract_text_from_pdf(file)
        st.success("PDF loaded successfully!")

# ---------------- SETTINGS ----------------
length = st.selectbox("Summary Length", ["Short", "Medium", "Detailed"])
bullet = st.checkbox("Bullet Point Summary")

# ---------------- SUMMARIZATION ----------------
def summarize(text, length, bullet):
    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        prompt = f"""
        Summarize the following text in {length.lower()} form.
        {"Give bullet points." if bullet else "Give paragraph format."}

        Text:
        {chunk}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful summarization assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=400
        )

        summaries.append(response.choices[0].message.content)

    return "\n\n".join(summaries)


# ---------------- BUTTON ----------------
if st.button("✨ Generate Summary"):
    if text.strip() == "":
        st.warning("Please enter or upload text first.")
    else:
        with st.spinner("Summarizing..."):
            result = summarize(text, length, bullet)

        st.subheader("📝 Summary")
        st.write(result)