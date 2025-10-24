import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_dir):
    combined_text = ""
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, filename)
            try:
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        combined_text += text + "\n"
            except Exception as e:
                print(f"Could not read '{filename}': {e}")
                
    return combined_text