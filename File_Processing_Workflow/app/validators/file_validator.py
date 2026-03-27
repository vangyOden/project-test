import os

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB

# Match file_service (PDF + DOCX only)
ALLOWED_MIME_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # .docx
]

ALLOWED_EXTENSIONS = [".pdf", ".docx"]

# Magic numbers (file signatures)
MAGIC_NUMBERS = {
    ".pdf": b"%PDF",
    ".docx": b"PK",  # DOCX is a zipped format
}


def validate_files(files, contents):
    """
    Validates uploaded files for size, type, extension, and content signature.

    Returns:
        valid_files: List of valid UploadFile objects
        valid_contents: List of valid file contents (bytes)
        errors: List of dicts describing invalid files
    """
    valid_files = []
    valid_contents = []
    errors = []

    for file, content in zip(files, contents):
        try:
            filename = file.filename

            #  Size check
            if len(content) > MAX_FILE_SIZE:
                raise ValueError("File too large (max 20MB)")

            #  MIME type check
            if file.content_type not in ALLOWED_MIME_TYPES:
                raise ValueError("Invalid MIME type (only PDF or DOCX allowed)")

            # Extension check
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                raise ValueError("Invalid file extension (only .pdf or .docx allowed)")

            # Magic number check
            expected_magic = MAGIC_NUMBERS.get(ext)

            if not expected_magic:
                raise ValueError("Unsupported file type")

            if not content.startswith(expected_magic):
                raise ValueError("File content does not match its extension")

            # Passed all checks
            valid_files.append(file)
            valid_contents.append(content)

        except ValueError as e:
            errors.append({
                "filename": file.filename,
                "error": str(e)
            })

    return valid_files, valid_contents, errors