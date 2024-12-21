from src.utils.pdf_utils import extract_text_from_pdf
from src.utils.chunk_utils import split_text_into_chunks
from src.models.embedding_model import EmbeddingModel

class PDFManager:
    def __init__(self):
        self.embedding_model = EmbeddingModel()

    def process_pdf(self, pdf_path):
        # Extract text from PDF
        text = extract_text_from_pdf(pdf_path)
        
        # Split text into chunks
        chunks = split_text_into_chunks(text)
        
        # Generate embeddings
        embeddings = self.embedding_model.generate_embeddings(chunks)
        
        # Check for compliance issues (dummy logic here)
        defects = [chunk for chunk in chunks if "defect" in chunk.lower()]
        return defects
