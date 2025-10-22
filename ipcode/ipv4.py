# IPv4 Subnet Masks and Prefixes

def get_number_ip_addresses(p_prefix):
    pbits = 32 - int(p_prefix[1:])
    return 2 ** pbits

def get_number_ip_hosts(p_prefix):
    pbits = 32 - int(p_prefix[1:])
    return (2 ** pbits) - 2

def get_number_ip_hosts_2(p_prefix):
    pbits = 32 - int(p_prefix[1:])
    return (2 ** pbits) - 2

### dev test function
net_number_addr = get_number_ip_addresses('/24')
net_number_ip_hosts = get_number_ip_hosts('/24')

print(net_number_addr)
print(net_number_ip_hosts)
