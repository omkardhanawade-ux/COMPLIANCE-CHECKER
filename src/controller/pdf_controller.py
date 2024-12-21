from fastapi import APIRouter, UploadFile, HTTPException
from src.manager.pdf_manager import PDFManager

router = APIRouter()
pdf_manager = PDFManager()

@router.post("/upload/")
async def upload_pdf(file: UploadFile):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    content = await file.read()
    pdf_path = f"data/{file.filename}"
    
    with open(pdf_path, "wb") as f:
        f.write(content)
    
    try:
        defects = pdf_manager.process_pdf(pdf_path)
        return {"message": "File processed successfully", "defects": defects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
