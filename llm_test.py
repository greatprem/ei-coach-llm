import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# 🔁 EASY MODEL SWITCHER
model = "meta-llama/llama-4-maverick:free"  # 🔄 change to other models here

# Prompt
user_input = "What is emotional intelligence in simple words?"

# Headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Payload
data = {
    "model": model,
    "messages": [
        {"role": "user", "content": user_input}
    ]
}

# Make request
response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

# Debugging output
print("Raw response:")
print(response.text)

try:
    content = response.json()["choices"][0]["message"]["content"]
    print("\n🧠 AI Response:")
    print(content)
except KeyError:
    print("\n❌ 'choices' not found in response.")