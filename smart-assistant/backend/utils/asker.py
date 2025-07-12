import requests, json
from sentence_transformers import SentenceTransformer, util
 
# Load embedding model once
embedder = SentenceTransformer('all-MiniLM-L6-v2')
 
def local_llm_answer(question: str, context: str) -> str:
    prompt = f"Context:\n{context}\n\nAnswer this question in very short: {question}\nAnswer:"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3", "prompt": prompt, "stream": True},
        stream=True
    )
 
    full_output = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8").replace("data: ", "")
            try:
                chunk = json.loads(data)
                full_output += chunk.get("response", "")
            except:
                pass
 
    return full_output.strip()
 
def get_answer(text: str, question: str) -> str:
    # Chunk the text
    chunks = text.split(". ")
    chunks = [c.strip() for c in chunks if len(c.split()) > 5]
 
    # Embed question and chunks
    question_embedding = embedder.encode(question, convert_to_tensor=True)
    chunk_embeddings = embedder.encode(chunks, convert_to_tensor=True)
 
    # Get top 2 relevant chunks
    scores = util.pytorch_cos_sim(question_embedding, chunk_embeddings)[0]
    top_idxs = scores.topk(2).indices.tolist()
    top_context = " ".join([chunks[i] for i in top_idxs])
 
    # Ask LLM
    return local_llm_answer(question, top_context)
 