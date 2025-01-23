from src.manager.split_manager import split_pdf_manager
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def split_pdf_controller(docs):
    """
    Controller for splitting a PDF into smaller chunks.

    Args:
        docs (list): List of documents to split. Each document should be a dictionary with a "text" field.

    Returns:
        list: List of smaller chunks of documents.
    """
    try:
        # Validate input
        if not isinstance(docs, list) or not all(isinstance(doc, dict) and "text" in doc for doc in docs):
            raise ValueError("Invalid input: Expected a list of documents with a 'text' field in each.")

        logger.info(f"Starting PDF split for {len(docs)} documents.")
        
        # Delegate to the manager
        split_docs = split_pdf_manager(docs)
        
        logger.info(f"Successfully split documents into {len(split_docs)} chunks.")
        return split_docs

    except Exception as e:
        logger.error(f"Error during document splitting: {e}")
        raise
