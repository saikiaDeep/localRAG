
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from helpers.pdf_downloader import download_from_storage
 
app = FastAPI()

 
@app.get("/")
def read_root():
    return "RAG pipeline"


@app.get("/llm")
def call_llm():
        
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama2",
        "prompt": "Why is the sky blue?",
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
    # data = response.json()
    # print(data.get('response'))
    return response.json()
    
