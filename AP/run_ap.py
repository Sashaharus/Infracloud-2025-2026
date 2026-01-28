import requests

ACCESS_TOKEN = ""

url = "https://webexapis.com/v1/people/me"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print("HTTP status code:", response.status_code)

data = response.json()

print("User info:")
print("Name:", data["displayName"])
print("Email:", data["emails"][0])
