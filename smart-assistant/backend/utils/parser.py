import os
import pdfplumber
 
def parse_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
 
def parse_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
 
def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return parse_pdf(file_path)
    elif ext == '.txt':
        return parse_txt(file_path)
    else:
        raise ValueError("Unsupported file type")