# need to take a break from this. driving me crazy
# have added and deleted code
# need to re-evaluate how I want this to work

import requests
url = 'http://autocomplete.wunderground.com/aq?query=query'
city = 'Indianapolis, Indiana'
data = {'query': city}

r = requests.get(url, data)
r.json()

print(data)
print(url)
