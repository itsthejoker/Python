import validators
import socket
import subprocess
import sys
from datetime import datetime

# clearing the screen
subprocess.call('clear', shell=True)

# get the ip address to scan
remoteServer = input('Enter a remote host to scan: ')

# validation
if validators.ip_address.ipv4(remoteServer):
    remoteServerIP = socket.gethostbyname(remoteServer)
else:
    print('Not a valid IPv4 address. Search for valid IPv4 addresses in your favorite search engine.')
    exit()
 
# print the scanning ip
print('*' * 60)
print('Please wait, scanning remote host of well-know ports', remoteServerIP)
print('*' * 60)

# time scan started
start_time = datetime.now()

# scan all ports between 1 and 1024
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print('Port {}: 	 Open'.format(port))
        sock.close()

# error handling
except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit(1)

except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit(1)

except socket.error:
    print('Could not connect to server')
    sys.exit(1)

# time for script to finish
end_time = datetime.now()
completion_time = end_time - start_time

# print completion time
print('Scanning completed in: ', completion_time)
