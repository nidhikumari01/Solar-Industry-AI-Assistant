import requests
import base64

def analyze_rooftop_image(image_bytes, api_key):
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",  # or another vision model
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": open("prompts/analysis_prompt.txt").read()},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"
