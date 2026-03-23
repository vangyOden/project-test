from fastapi import FastAPI
from app.routes import upload

app = FastAPI(
    title="File Processing Workflow",
    description="Upload PDF and DOC files and get readable content",
    version="1.0.0",
    openapi_url="/openapi.json"
)

# Included upload router
app.include_router(
    upload.router,
    prefix="",
    tags=["Upload"]
)

# home route for testing the server
@app.get("/")
async def root():
    return {"message": "File Processing API is running."}