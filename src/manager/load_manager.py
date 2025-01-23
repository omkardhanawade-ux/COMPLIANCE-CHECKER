from langchain_community.document_loaders import PyPDFLoader

def load_pdf_manager(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    return do