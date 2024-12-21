from fastapi import FastAPI, UploadFile, HTTPException
from src.controller.pdf_controller import router
from dotenv import load_dotenv
import os
app = FastAPI()

# Include the router from the controller
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AI Compliance Checker is running!"}


# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")