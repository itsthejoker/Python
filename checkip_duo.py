# check ip using requests
# second go round with a new way to grab ip

import requests

data = {'format': 'json'}
r = requests.get('https://api.ipify.org', data)
r.json()

print(r.text)

