# backend/app.py
 
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
 
from utils.parser import extract_text
from utils.summarizer import summarize_with_ollama
from utils.asker import get_answer
 
 
app = FastAPI()
 
# Allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
class FilePathRequest(BaseModel):
    file_path: str
 
@app.post("/summarize")
async def summarize(request: FilePathRequest):
    text = extract_text(request.file_path)
    summary = summarize_with_ollama(text)
    return {"summary": summary}
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
 
class QuestionRequest(BaseModel):
    file_path: str
    question: str
 
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    text = extract_text(request.file_path)
    response = get_answer(text, request.question)
    return response