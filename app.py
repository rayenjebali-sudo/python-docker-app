import requests
response=requests.get("https://api.github.com")
print("status:",response.status_code)
print("headers:",response.headers["content-type"])

