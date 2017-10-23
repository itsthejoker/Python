# Microsoft's current CVE list from
# circl.lu
# pulling the last 100 CVE's

import urllib.request
import json
import pandas as pd

# getting the url

f = urllib.request.urlopen('https://cve.circl.lu/api/search/microsoft/windows')

# decoding the text
json_string = f.read().decode('utf-8')

# parsing the information
parsed_json = json.loads(json_string)

records = []
num = 0
while (num < 100):
    cve = parsed_json[num]['id']
    cwe = parsed_json[num]['cwe']
    summary = parsed_json[num]['summary']
    published = parsed_json[num]['Published']
    last_modified = parsed_json[num]['last-modified']
    records.append((cve, cwe, summary, published, last_modified))
    num = num + 1

# export to csv
df = pd.DataFrame(records, columns=['cve', 'cwe', 'summary', 'published', 'last_modified'])
df.to_csv('cve_microsoft.csv', index=False, encoding='utf-8')
f.close()
