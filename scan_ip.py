import os
from tld import get_tld

# create the directory
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# write the output to a file    
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

# get top level domain
def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name
print('Getting domain name')

# get ip address of top level domain
def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]
print('Getting IP address')

# run nmap "fast" scan of ip address
def get_nmap(ip):
    command = 'nmap -F ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results
print('Processing nmap results')

# bringing it all together
root_dir = 'targets'
create_directory(root_dir)

def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap(ip_address)
    create_report(name, url, domain_name, nmap)

def create_report(name, full_url, domain_name, nmap):
    project_dir = root_dir + '/' + name
    create_directory(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/ip_address.txt', get_ip_address)
    write_file(project_dir + '/nmap results.txt', nmap)
    
print('Finished gathering information')

gather_info('quantifiedcode', 'https://www.quantifiedcode.com/')
