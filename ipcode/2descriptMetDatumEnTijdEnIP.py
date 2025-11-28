import requests
from datetime import datetime

# Huidige datum en tijd ophalen
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Publiek IP-adres ophalen
response = requests.get("https://api.myip.com")
data = response.json()
ip = data.get("ip", "Onbekend")

# Resultaat weergeven
print(f"Datum en tijd: {formatted_time}")
print(f"IP-adres: {ip}")
