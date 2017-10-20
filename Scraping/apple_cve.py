# going to parse data from Apple's current CVE
# 

import urllib.request
import json
import pandas as pd

# getting the url
f = urllib.request.urlopen('https://cve.circl.lu/api/search/apple/mac_os')

# decoding the text
json_string = f.read().decode('utf-8')

# parsing the information
parsed_json = json.loads(json_string)

records = []
for i in parsed_json:
    cve = parsed_json[0]['id']
    cwe = parsed_json[0]['cwe']
    summary = parsed_json[0]['summary']
    published = parsed_json[0]['Published']
    last_modified = parsed_json[0]['last-modified']
    records.append((cve, cwe, summary, published, last_modified))

# export to csv
df = pd.DataFrame(records, columns=['cve', 'cwe', 'summary', 'published', 'last_modified'])
df.to_csv('cve_apple.csv', index=False, encoding='utf-8')
