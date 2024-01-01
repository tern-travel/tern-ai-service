import PyPDF2

#This method is responsible for extractring text from a PDF to share with OpenAI
def extract_text(file_path:str):
    
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pdf_text = ""

        for page in reader.pages:
            pdf_text += page.extract_text()

    return pdf_text