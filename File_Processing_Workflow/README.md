# File Processing Workflow API

A scalable backend system built with FastAPI that allows users to:

1. Upload files (PDF & DOCX)
2. Validate files securely
3. Extract readable content
4. Enforce per-user rate limiting


APP Features

 File Upload
- Supports **single file upload per request**
- Accepts:
  - `.pdf`
  - `.docx`



File Validation
Each uploaded file is validated for:

1. File size (max 20MB)
2. MIME type
3. File extension
4. Magic number (file signature check)


Content Extraction
- PDF -- Extract text using `PyPDF2`
- DOCX -- Extract text using `python-docx`



 Rate Limiting (Per User)
1. Each user can upload up to files
2. Within a **3-minute window**
3. Based on user IP (for now)


Clean Architecture
Project is modular and scalable:

app/
|-- main.py

    |-- routes/
            upload.py
    |-- validators/
            file_validator.py
    |-- services/
            file_service.py
    |-- core/
            limiter.py


---

## Program Installation

## Clone the repository

---bash---
git clone git@github.com:vangyOden/project-test.git
cd File_Processing_Workflow

# Create virtual environment
python -m venv env

Activate it:

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate


# Install dependencies
pip install fastapi uvicorn python-multipart PyPDF2 python-docx typing-extensions

# Running the Application
uvicorn app.main:app --reload


# API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs

You’ll see Swagger UI where you can:

Upload files
Test endpoints
View responses


# Upload Endpoint
POST /upload
Description:

Upload a single file and extract readable content.

# Request
Content-Type: multipart/form-data
Field: file

# Success Response
{
  "processed_file": {
    "filename": "example.pdf",
    "content": "Extracted text from file..."
  },
  "message": "File processed successfully"
}


# Error Response
{
  "message": "Uploaded file is invalid",
  "errors": [
    {
      "filename": "bad_file.pdf",
      "error": "Invalid MIME type"
    }
  ]
}


# Rate Limiting Logic
Max uploads: 3 files
Time window: 3 minutes
Based on: User IP


# Limitations
Rate limiting is in-memory (resets on server restart)
No authentication yet (IP-based tracking only)


# Future Improvements
1 Add authentication (JWT / OAuth)
2 Use Redis for distributed rate limiting
3 Support batch uploads
4 Add OCR for scanned documents
5 Store extracted content in a database
6 Add analytics & monitoring


# Key Learnings

This project demonstrates:

File handling in FastAPI
Validation strategies for uploads
Content extraction pipelines
Rate limiting design
Clean backend architecture