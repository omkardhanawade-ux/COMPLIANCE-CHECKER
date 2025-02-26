# COMPLIANCE-CHECKER

## Overview
The Compliance Checker is a Python-based application built with FastAPI that processes PDF documents, extracts their content, splits them into smaller chunks, and generates embeddings using OpenAI's `text-embedding-ada-002` model. These embeddings are then stored in a FAISS vector database for later use.

---

## Features
1. **Upload PDF**: Allows users to upload PDF documents.
2. **Extract Content**: Extracts the content from the uploaded PDF.
3. **Split Content**: Splits the content into smaller, manageable chunks.
4. **Generate Embeddings**: Creates embeddings for the text chunks using OpenAI's API.
5. **Store Embeddings**: Saves the embeddings in a FAISS vector database.

---

## Requirements
- Python 3.8+
- Pip

### Python Dependencies
Install the required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

**Key Libraries Used:**
- FastAPI: For creating the RESTful API.
- OpenAI: For generating text embeddings.
- FAISS: For storing and managing vector embeddings.
- Pydantic: For request validation.
- Uvicorn: For running the FastAPI app.
- Python-dotenv: For loading environment variables from `.env` file.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Compliance-Checker
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root directory and add the following:
```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

### 1. `POST /process-pdf/`
Processes a PDF document by uploading, extracting, splitting, and embedding the data.

#### Request
- **Form Data**: Upload the PDF as a file using `file` parameter.

#### Response
```json
{
  "status": "Success",
  "message": "PDF processed successfully. Data stored in vector database."
}
```

---

## Testing the API

### Using Postman
1. Open Postman and create a new `POST` request.
2. Set the URL to `http://127.0.0.1:8000/process-pdf/`.
3. Under the `Body` tab, select `form-data` and upload a PDF file with the key as `file`.
4. Send the request.
5. View the response for the status of the operation.

### Using Curl
```bash
curl -X POST "http://127.0.0.1:8000/process-pdf/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_file.pdf"
```

---

## Project Structure
```
Compliance-Checker/
|
├── main.py                    # Main FastAPI application
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── uploaded_files/            # Directory to store uploaded PDFs
├── src/
|   ├── controller/
|   │   ├── load_controller.py  # Handles PDF loading and extraction
|   │   ├── split_controller.py # Handles splitting content into chunks
|   ├── models/
|       ├── embedding_model.py  # Handles embedding generation and storage
|
├── faiss_index/               # Directory to store FAISS index
```

---

## Troubleshooting

### Common Issues
1. **Missing API Key**: Ensure the `OPENAI_API_KEY` is correctly set in the `.env` file.
2. **Library Version Errors**: Ensure all dependencies are installed with compatible versions using the `requirements.txt` file.
3. **File Format Errors**: Make sure to upload valid PDF files.

### Debugging Logs
Logs are displayed in the terminal to help trace errors and monitor the application.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
- [OpenAI](https://openai.com) for the text embedding API.
- [LangChain](https://langchain.com) for simplifying vector database management.
- [FAISS](https://faiss.ai/) for efficient similarity search.

