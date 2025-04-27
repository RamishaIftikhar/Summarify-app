import requests

def summarize_text(text):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    api_key = "AIzaSyCJX-rqPIhPQ00gF_1mH7PwrfF13qz8LQ8"  # <-- Aapki nayi API key

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": f"Summarize the following text:\n{text}"}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url=f"{url}?key={api_key}", headers=headers, json=data
        )

        if response.status_code == 200:
            candidates = response.json().get("candidates", [])
            if candidates:
                return candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "No summary generated.")
            return "No summary generated."
        else:
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"
