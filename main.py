from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
import logging
from src.controller.load_controller import load_pdf_controller
from src.controller.split_controller import split_pdf_controller
from src.models.embedding_model import generate_embeddings_and_store
from pydantic import field_validator


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Temporary directory to save uploaded files
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-pdf/")
def upload_pdf(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file.

    Args:
        file (UploadFile): The uploaded PDF file.

    Returns:
        dict: Response containing the upload status and file path.
    """
    try:
        logger.info(f"Received file upload request: {file.filename}")

        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Invalid file format. Only PDF files are supported.")

        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"File successfully uploaded: {file_path}")
        return {"status": "Success", "file_path": file_path}

    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/load-pdf/")
def load_pdf(file_path: str):
    """
    Endpoint to load a PDF file.

    Args:
        file_path (str): Path to the PDF file to load.

    Returns:
        dict: Response containing the loaded document data.
    """
    try:
        logger.info(f"Loading PDF from path: {file_path}")
        docs = load_pdf_controller(file_path)
        return {"status": "Success", "data": docs}

    except Exception as e:
        logger.error(f"Error loading PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/split-pdf/")
def split_pdf(docs: list):
    """
    Endpoint to split a PDF into smaller chunks.

    Args:
        docs (list): List of documents to split. Each document should be a dictionary with a "text" field.

    Returns:
        dict: Response containing the split document chunks.
    """
    try:
        logger.info("Splitting PDF into chunks.")
        split_docs = split_pdf_controller(docs)
        return {"status": "Success", "chunks": split_docs}

    except Exception as e:
        logger.error(f"Error splitting PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-embeddings/")
def generate_embeddings(chunks: list):
    """
    Endpoint to generate embeddings and store them in a FAISS vector store.

    Args:
        chunks (list): List of document chunks, where each chunk has "page_content" and "metadata" fields.

    Returns:
        dict: Response indicating success.
    """
    try:
        logger.info("Generating embeddings and storing them in FAISS vector store.")
        generate_embeddings_and_store(chunks)
        return {"status": "Success", "message": "Embeddings generated and stored successfully."}

    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

