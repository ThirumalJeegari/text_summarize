import pdfplumber

# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -------- CHUNKING (VERY IMPORTANT) --------
def chunk_text(text, chunk_size=2500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]