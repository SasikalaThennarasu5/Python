import PyPDF2

def extract_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                try:
                    reader.decrypt('')
                except:
                    raise ValueError("Cannot decrypt the PDF.")
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    yield text.strip()
                else:
                    yield "[No extractable text on this page]"
    except FileNotFoundError:
        print(f"File not found: {pdf_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    path = "sample.pdf"
    for i, page_text in enumerate(extract_text(path), 1):
        print(f"--- Page {i} ---")
        print(page_text)
