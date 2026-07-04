from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    # Limit to first 4000 characters
    return text[:4000]