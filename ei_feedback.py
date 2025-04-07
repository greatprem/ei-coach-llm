import os
import requests
from dotenv import load_dotenv

load_dotenv()  # ✅ Make sure this is called BEFORE reading the API key
api_key = os.getenv("OPENROUTER_API_KEY")
print("🔐 Loaded API Key:", api_key)  # ← Add this to debug


def get_feedback(user_input):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model":
        "meta-llama/llama-4-maverick",
        "messages": [{
            "role":
            "user",
            "content":
            f"Analyze this sentence for emotional intelligence: '{user_input}'. Give feedback on tone, empathy, and clarity."
        }]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                             headers=headers,
                             json=data)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "⚠️ Error: Unable to get feedback. Check your API key or model name."


while True:
    user_input = input("\n🧑 Enter your message (or type 'exit'): ")
    if user_input.lower() == 'exit':
        break
    feedback = get_feedback(user_input)
    print("\n🧠 Feedback from EI Coach:\n", feedback)
