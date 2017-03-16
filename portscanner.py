import socket
import subprocess
import sys
from datetime import datetime

# clearing the screen
subprocess.call('clear', shell=True)

# get the ip address to scan
remoteServer = input('Enter a remote host to scan: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# print the scanning ip
print('*' * 60)
print('Please wait, scanning remote host', remoteServerIP)
print('*' * 60)

# time scan started
t1 = datetime.now()

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
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print('Could not connect to server')
    sys.exit()

# time for script to finish
t2 = datetime.now()
total = t2 - t1

# print compltetion time
print('Scanning Completed in: ', total)
