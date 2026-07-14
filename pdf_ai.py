from ai import ask_ai
from pypdf import PdfReader

def ask_pdf(uploaded_pdf, question):

    reader = PdfReader(uploaded_pdf)

    text = ""

    for page in reader.pages[:3]:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    prompt = f"""
Use this PDF to answer the question.

PDF:

{text}

Question:

{question}
"""

    return ask_ai(prompt)
