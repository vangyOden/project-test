import io
from PyPDF2 import PdfReader
from docx import Document


async def process_files(files, contents):
    
    results = []
    
    for file, content in zip(files, contents):
        filename = file.filename
        ext = filename.split(".")[-1].lower()

        extracted_text = ""

        # this will handle the pdf files and extract the text from it using PyPDF2 library
        if ext == "pdf":
            try:
                reader = PdfReader(io.BytesIO(content))
                for page in reader.pages:
                    extracted_text += page.extract_text() or ""
            except Exception:
                extracted_text = "Could not extract text from PDF."

        # this will handle the docx files and extract the text from it using python-docx library
        elif ext == "docx":
            try:
                doc = Document(io.BytesIO(content))
                extracted_text = "\n".join(
                    [para.text for para in doc.paragraphs]
                )
            except Exception:
                extracted_text = "Could not extract text from DOCX."

        # if the file type is not supported, we return a message indicating that the file type is unsupported
        else:
            extracted_text = "Unsupported file type."

        results.append({
            "filename": filename,
            "content": extracted_text.strip()
        })

    return results



# import io
# from typing import List

# # from docx import Document  # for .docx support (optional)
# # import PyPDF2

# async def process_files(files: List, contents: List):
#     """
#     Extract readable content from uploaded files.
#     Returns a list of dict: {"filename": ..., "content": ...}
#     """
#     results = []

#     for file, content in zip(files, contents):
#         text = ""
#         ext = file.filename.split(".")[-1].lower()

#         if ext == "pdf":
#             # Read PDF text
#             reader = PyPDF2.PdfReader(io.BytesIO(content))
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#         elif ext == "doc":
#             # Simple DOC reading (if needed, you can switch to python-docx for .docx)
#             text = "Binary DOC content (preview not implemented)"
#         results.append({"filename": file.filename, "content": text})

#     return results