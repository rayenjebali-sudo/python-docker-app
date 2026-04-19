import os
import requests

url = os.getenv("API_URL", "https://api.github.com")

response = requests.get(url)

print("Status:", response.status_code)
