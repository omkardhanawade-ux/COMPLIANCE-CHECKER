from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def split_pdf_manager(docs):
    """
    Split the loaded documents into smaller chunks using RecursiveCharacterTextSplitter.

    Args:
        docs (list): List of documents to be split. Each document is typically a dictionary or string.

    Returns:
        list: List of split document chunks.
    """
    try:
        # Validate input
        if not isinstance(docs, list) or not all(isinstance(doc, dict) for doc in docs):
            raise ValueError("Invalid input: Expected a list of documents (each document as a dictionary).")
        
        logger.info(f"Starting document splitting for {len(docs)} documents.")

        # Configure and apply text splitter
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        final_documents = text_splitter.split_documents(docs)

        logger.info(f"Document splitting complete. Total chunks created: {len(final_documents)}")
        return final_documents

    except Exception as e:
        logger.error(f"Error during document splitting: {e}")
        raise
