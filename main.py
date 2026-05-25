from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from orchestrator import Orchestrator
from models.output_models import DocumentAnalysisOutput
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

app = FastAPI(title="Multi-Agent Document Intelligence API")
orchestrator = Orchestrator(api_key)

class DocumentRequest(BaseModel):
    document: str

@app.post("/analyze", response_model=DocumentAnalysisOutput)
async def analyze_document(request: DocumentRequest):
    try:
        result = orchestrator.process_document(request.document)
        return DocumentAnalysisOutput(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Multi-Agent Document Intelligence API"}
