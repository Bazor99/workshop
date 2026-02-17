from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages


def extract_text(pages):
    text = ""
    for page in pages:
        text += page.page_content + "\n"
    return text
