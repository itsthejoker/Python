import subprocess
import ipaddress

network_address = input('Enter a network address in CIDR format(example 192.168.1.0/24): ')
ip_network = ipaddress.ip_network(network_address)
all_hosts = list(ip_network.hosts())

print(all_hosts)
