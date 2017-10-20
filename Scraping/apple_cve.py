# going to parse data from Apple's current CVE
# 

import urllib.request
import json

# getting the url
f = urllib.request.urlopen('https://cve.circl.lu/api/search/apple/mac_os')

# decoding the text
json_string = f.read().decode('utf-8')

# parsing the information
parsed_json = json.loads(json_string)
cve = parsed_json[0]['id']

print('CVE is: %s' % (cve))

f.close()
