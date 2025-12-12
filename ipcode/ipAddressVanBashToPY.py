import requests

response = requests.get("https://api.myip.com")
data = response.json()

print(data)
