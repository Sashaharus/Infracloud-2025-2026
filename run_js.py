import yaml

with open("JS1-examen.yaml", "r") as f:
    data = yaml.safe_load(f)

print("Device hostname:", data["device"]["hostname"])
print("Interfaces:")

for interface in data["interfaces"]:
    print(
        f"- {interface['name']} | "
        f"IP: {interface['ip_address']} | "
        f"Status: {interface['status']}"
    )
