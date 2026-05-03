# 📝 AI Text Summarizer

## 🚀 Overview

The **AI Text Summarizer** is a web application that converts long text or PDF documents into short, meaningful summaries using AI.

Built with **Python**, **Streamlit**, and the **Groq API**, this tool helps students, researchers, and professionals quickly understand large amounts of content.

---

## 🎯 Features

* 📄 Summarize long text instantly
* 📂 Upload PDF documents for summarization
* 📏 Summary length options:

  * Short
  * Medium
  * Detailed
* 📌 Bullet-point summary option
* ⚡ Fast AI-powered responses
* 🎨 Simple and clean UI

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM API:** Groq
* **Model:** llama3-8b-8192
* **PDF Parsing:** PyPDF2 / pdfplumber

---

## 📂 Project Structure

```id="0y0r8l"
AI-Text-Summarizer/
│
├── app.py               # Main Streamlit app
├── llm_helper.py        # Summarization logic
├── pdf_parser.py        # PDF text extraction
├── config.py (optional) # API client setup
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```id="sqxhgg"
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Install dependencies

```id="6z8gk7"
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

### Windows (PowerShell)

```id="7js83h"
$env:GROQ_API_KEY="your_api_key_here"
```

### Windows (CMD)

```id="2lmdas"
set GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```id="gx36rb"
streamlit run app.py
```

---

## 💡 Usage

1. Paste your **text** or upload a **PDF file**
2. Select summary length (**short / medium / detailed**)
3. Choose format (**paragraph / bullet points**)
4. Click **Summarize**

---

## 🧪 Example Input

```id="v4zqqv"
Artificial Intelligence (AI) is transforming industries by automating tasks, improving efficiency, and enabling data-driven decisions...
```

---

## ⚠️ Common Errors & Fixes

### ❌ `client not defined`

✔ Ensure `client` is initialized in `llm_helper.py`

---

### ❌ API Key Error

✔ Set `GROQ_API_KEY` correctly

---

### ❌ Token Limit Error (413)

✔ Reduce input text size or split into chunks

---

### ❌ PDF Not Reading

✔ Install required libraries:

```id="o5y7ey"
pip install PyPDF2 pdfplumber
```

---

### ❌ Model Decommissioned

✔ Use a valid model:

```id="0qzpfm"
llama3-8b-8192
```

---

## 📌 Future Improvements

* Multi-language summarization
* Audio summarization
* Highlight key points automatically
* Export summary as PDF/Word
* Chrome extension integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Groq API
* Streamlit
* Open-source community

---

## 📧 Contact

**Thirumal Jeegari**
📍 India
📧 [thirumaljeegari21@example.com](mailto:thirumaljeegari21@example.com)

---

⭐ If you found this project useful, give it a star on GitHub!
