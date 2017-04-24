import os

def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

def get_nmap(ip):
    command = 'nmap -F ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results

url = input('Type in url you wish to use: ')
ip = (get_ip_address(url))
print (ip)
print(get_nmap(ip))
