from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Document Processing Service Running"}


