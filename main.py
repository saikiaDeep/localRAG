
from fastapi import FastAPI
from pydantic import BaseModel, Field
import requests
from helpers.query import QueryEngine
app = FastAPI()
class Query(BaseModel):
    inp_query: str = Field(default="What is AGI?", description="The query string that is used to search the vector database")

query_engine = QueryEngine()

@app.get("/")
def read_root():
    return "RAG pipeline"

@app.post("/query")
def retrieve_results(query:Query):
    return query_engine.process_response(query.inp_query)




