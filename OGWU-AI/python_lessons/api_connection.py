import requests

print("OGWU API connection test")


url = "https://example.com"

response = requests.get(url)

print(response.text)