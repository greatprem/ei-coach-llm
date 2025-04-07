import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
print("Your API Key:", api_key)

# Test a dummy request (optional example)
# response = requests.get("https://httpbin.org/get")
# print(response.json())