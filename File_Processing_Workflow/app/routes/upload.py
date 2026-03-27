from fastapi import APIRouter, UploadFile, File, HTTPException, Request

from app.validators.file_validator import validate_files
from app.services.file_service import process_files
from app.core.limiter import check_upload_limit

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload Document",
    description="Upload a single PDF or DOC file and get readable content."
)
async def upload_document(
    request: Request,
    file: UploadFile = File(..., description="Upload a PDF or DOC file here.")
):
    # rate limit (1 file per request)
    check_upload_limit(request, 1)

    # reading file content for validation and processing
    content = await file.read()

    # this will validate file and get valid file and content (or errors)
    valid_files, valid_contents, errors = validate_files([file], [content])

    # Handle invalid file
    if not valid_files:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Uploaded file is invalid",
                "errors": errors
            }
        )

    # Process file (extract readable content)
    processed = await process_files(valid_files, valid_contents)

    # Return result (only one file)
    return {
        "processed_file": processed[0],
        "message": "File processed successfully"
    }

# @router.post("/upload", summary="Upload Documents", description="Upload one or more PDF or DOC files. Returns the readable content of valid files.")
# async def upload_documents(
#     files: Annotated[List[UploadFile], File(..., description="Select one or more PDF/DOC files")]
# ):
#     # called the limiter function to check if the user has exceeded the upload limit before processing the files
#     check_upload_limit(request,1)

#     # reading the actual content of the files into memory (for validation and processing)
#     content = await file.read()

#     # calling the validator function to check the files and get valid files and their contents
#     valid_files, valid_contents, errors = validate_files([files], [contents])

#     # this will return a responds if all upload fails
#     if not valid_files:
#         from fastapi import HTTPException
#         raise HTTPException(
#             status_code=400,
#             detail={"message": "All uploaded files are invalid", "failed_files": errors}
        # )

    # Process valid files to extract readable content
    # processed = await process_files(valid_files, valid_contents)

    # this will return the response, if some files are processed successfully and some failed validation 
    # return {
    #     "processed_files": processed,
    #     "failed_files": errors,
    #     "total_uploaded": len(files),
    #     "total_processed": len(processed),
    #     "total_failed": len(errors)
    # }
    # return {"filenames": [file.filename for file in files]}