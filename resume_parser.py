import PyPDF2

def parse_resume(uploaded_file) -> str:
    """Extract text from a PDF resume."""
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Failed to parse resume: {str(e)}")
