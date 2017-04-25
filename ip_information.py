import os
import subprocess

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

def get_ping(ip):
    command = 'ping -c 5 ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results
    
def get_whois(ip):
    command = 'whois ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results
    
def get_host(ip):
    command = 'host -l ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results

def get_geolocation(ip):
    #ipinfo.io has an API rate-limit to 1,000 API requests per day
    command = 'curl ipinfo.io/ ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results

# clearing the screen
subprocess.call('clear', shell=True)

url = input('Type in url you wish to use: ')
ip = (get_ip_address(url))
print(ip)
print(get_nmap(ip))
print(get_ping(ip))
print(get_whois(ip))
print(get_host(ip))
print(get_geolocation(ip))
