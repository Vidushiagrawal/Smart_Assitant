import requests
import json
 
def summarize_with_ollama(text: str) -> str:
    prompt = f"Summarize the following text in about 100 words :\n\n{text}\n\nSummary:"
   
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3", "prompt": prompt, "stream": True},
        stream=True
    )
 
    summary = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8").replace("data: ", "")
            try:
                chunk = json.loads(data)
                summary += chunk.get("response", "")
            except Exception:
                pass
 
    return summary.strip()
 