from langchain.vectorstores import FAISS
from openai.embeddings_utils import get_embedding
from dotenv import load_dotenv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

def generate_embeddings_and_store(chunks = "final_documents" , faiss_index_path="faiss_index"):
    """
    Generate embeddings using OpenAI and store them in a FAISS vector store.

    Args:
        chunks (list): List of document chunks, where each chunk has a "page_content" and "metadata".
        faiss_index_path (str): Path to save the FAISS index.

    Returns:
        None
    """
    try:
        # Retrieve OpenAI API key from environment
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key not found in environment variables. Please set it in your .env file.")

        import openai
        openai.api_key = openai_api_key

        logger.info(f"Starting embedding generation for {len(chunks)} document chunks.")

        # Prepare data for FAISS
        texts = [chunk["page_content"] for chunk in chunks]
        metadatas = [chunk["metadata"] for chunk in chunks]

        # Generate embeddings
        embeddings = []
        for text in texts:
            embedding = get_embedding(text, engine="text-embedding-ada-002")
            embeddings.append(embedding)

        logger.info("Embedding generation complete.")

        # Create FAISS vector store
        logger.info("Saving embeddings to FAISS vector store.")
        vector_store = FAISS.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas)
        vector_store.save_local(faiss_index_path)

        logger.info(f"FAISS vector store successfully saved at {faiss_index_path}.")

    except Exception as e:
        logger.error(f"Error in embedding generation or storage: {e}")
        raise
 

    # Call the embedding and storage function
    generate_embeddings_and_store(chunks, faiss_index_path="faiss_index")
