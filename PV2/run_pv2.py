
hostname = "Router1"
ip_address = "192.168.1.1"
status = "up"

device = {
    "hostname": hostname,
    "ip_address": ip_address,
    "status": status
}

interfaces = [
    {
        "name": "GigabitEthernet0/0",
        "ip": "192.168.1.1",
        "status": "up"
    },
    {
        "name": "GigabitEthernet0/1",
        "ip": "192.168.2.1",
        "status": "down"
    }
]

print("Device info:")
print(device)

print("\nInterfaces:")
for interface in interfaces:
    print(
        f"- {interface['name']} | "
        f"IP: {interface['ip']} | "
        f"Status: {interface['status']}"
    )