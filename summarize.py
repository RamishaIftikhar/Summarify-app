import requests
import os
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in .env")

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": f"Summarize the following text:\n{text}"}]
        }]
    }

    response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)
    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    candidates = response.json().get("candidates", [])
    if not candidates:
        return "No summary generated."
    return candidates[0]["content"]["parts"][0]["text"]
