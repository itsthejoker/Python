import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = (s.getsockname()[0])
print(ip_address)
host_name = socket.gethostname()
print(host_name)
s.close()
