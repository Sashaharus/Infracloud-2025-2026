import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print("Connecting via SSH => show version")
#
from netmiko import ConnectHandler
### VAR

### EXEC
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="devnetsandboxiosxec8k.cisco.com",
    port="22",
    username="harussasha72",
    password="nR_9NjvFuqU-U827"
    )
output=sshCli.send_command("show version")
for line in output.splitlines():
    if 'Cisco IOS Software' in line:
        ios_version = line.strip()
    elif 'uptime' in line:
        hostname = line.split()[0]
        sys_uptime = line    
    elif 'interface' in line:
        num_interfaces = line.split()[0]
print("IOS Version")
print(ios_version)
print("Hostname")
print(hostname)
print("System uptime")
print(sys_uptime)
print("Number of Interfaces")
print(num_interfaces)

import pandas as pd

# Data in tabelvorm zetten
data = {
    "IOS Version": [ios_version],
    "Hostname": [hostname],
    "System Uptime": [sys_uptime],
    "Number of Interfaces": [num_interfaces],
    "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
}

# DataFrame maken
df = pd.DataFrame(data)

# Schrijf het naar een Excel-bestand
df.to_excel("device_info.xlsx", index=False)

print("\n✅ Data opgeslagen in 'device_info.xlsx'")