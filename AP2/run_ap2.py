import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("HTTP status code:", response.status_code)

users = response.json()

print("Users:")

for user in users:
    print(
        f"- {user['name']} | "
        f"Email: {user['email']} | "
        f"City: {user['address']['city']}"
    )
