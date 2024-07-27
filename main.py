
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

 
@app.get("/")
def read_root():
    return "RAG pipeline"


