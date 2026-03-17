from fastapi import APIRouter, UploadFile, File

router = APIRouter()

# this endpoint will be used to upload documents for processing
@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }