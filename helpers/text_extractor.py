import fitz
import glob
import os 
def extract_text_from_pdf(pdf_file_path):
    doc = fitz.open(pdf_file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_all_text():
    result = ""
    pdf_files = glob.glob(os.path.join('..\data', '*.pdf'))
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        result += text
    return result


     
        
