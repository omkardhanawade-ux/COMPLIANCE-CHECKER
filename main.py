from fastapi import FastAPI, File, UploadFile, HTTPException
import shutil
import os
import logging
from src.controller.load_controller import load_pdf_controller
from src.controller.split_controller import split_pdf_controller
from src.models.embedding_model import generate_embeddings_and_store

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Temporary directory to save uploaded files
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process-pdf/")
async def process_pdf(file: UploadFile = File(...)):
    try:
        logger.info(f"Received file upload request: {file.filename}")

        # Validate the file format
        if not file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Invalid file format. Only PDF files are supported.")

        # Save the file locally
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"File successfully uploaded: {file_path}")

        # Step 1: Load PDF and extract content
        logger.info(f"Loading and extracting data from PDF: {file_path}")
        docs = load_pdf_controller(file_path)

        # Transform docs to the expected format if necessary
        if isinstance(docs, str):
            docs = [{"text": docs}]
        elif isinstance(docs, list) and all(isinstance(doc, str) for doc in docs):
            docs = [{"text": doc} for doc in docs]

        logger.info(f"Extracted docs: {docs}")

        # Step 2: Split the extracted data into chunks
        logger.info(f"Splitting the extracted content into chunks.")
        split_docs = split_pdf_controller(docs)

        # Step 3: Generate embeddings and store in vector database
        logger.info(f"Generating embeddings and storing them in FAISS vector store.")
        generate_embeddings_and_store(split_docs)

        return {"status": "Success", "message": "PDF processed successfully. Data stored in vector database."}

    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))
