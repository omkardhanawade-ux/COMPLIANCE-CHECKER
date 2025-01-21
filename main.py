from fastapi import FastAPI
from app.controller import router as pdf_router

app = FastAPI()

# Include the PDF router
app.include_router(pdf_router, prefix="/api", tags=["PDF Processing"])
