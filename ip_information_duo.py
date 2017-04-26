import nmap
nm = nmap.PortScannerYield()
for progressive_result in nm.scan('127.0.0.1/24', '22-25'):
    print(progressive_result)
