# Apple's current CVE list from
# circl.lu
# pulling 400 of the CVE's

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
num = 0
while (num < 400):
    cve = parsed_json[num].get('id', None)
    cwe = parsed_json[num].get('cwe', None)
    summary = parsed_json[num].get('summary', None)
    published = parsed_json[num].get('Published', None)
    last_modified = parsed_json[num].get('last-modified', None)
    records.append((cve, cwe, summary, published, last_modified))
    num = num + 1

#export to csv
df = pd.DataFrame(records, columns=('cve', 'cwe', 'summary', 'published', 'last_modified'))
df.to_csv('cve_apple.csv', index=False, encoding='utf-8')
f.close()
