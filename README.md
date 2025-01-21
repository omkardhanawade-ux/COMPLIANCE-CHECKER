# Compliance Checker

The **Compliance Checker** is a tool designed to help automate the process of checking compliance rules and regulations in various documents. The application utilizes advanced machine learning models and integrates with Pinecone for vector storage and retrieval. It leverages OpenAI's API for language processing and embedding generation.

## Features

- **PDF Processing**: The app allows users to upload and process PDF files.
- **Document Embedding**: It generates embeddings for documents using OpenAI's embedding model.
- **Compliance Checks**: The app checks the uploaded documents for compliance with predefined rules.
- **Pinecone Integration**: Uses Pinecone for storing and retrieving vector embeddings.
- **API Integration**: Exposes APIs to interact with the backend for document processing and compliance checks.

## Technologies Used

- **Python**: The backend is developed in Python, utilizing popular libraries such as FastAPI for the web framework, Pinecone for vector storage, and LangChain for OpenAI embeddings.
- **OpenAI**: For generating document embeddings.
- **Pinecone**: For scalable, high-performance vector search.
- **FastAPI**: Fast, modern web framework for building APIs.
- **Uvicorn**: ASGI server to run the FastAPI app.

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.7+
- A virtual environment (optional, but recommended)
- OpenAI API Key (you can get one from [OpenAI's website](https://beta.openai.com/signup/))
- Pinecone API Key (you can get one from [Pinecone's website](https://www.pinecone.io/))

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/omkardhanawade-ux/COMPLIANCE-CHECKER.git
   cd COMPLIANCE-CHECKER
