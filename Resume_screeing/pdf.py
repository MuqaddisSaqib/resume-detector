import fitz  # PyMuPDF

def pdf_to_text(pdf_file):
    text = ''

    # Open the PDF file using the file-like object
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as pdf:
        # Iterate through each page
        for page in pdf:
            text += page.get_text()

    return text

