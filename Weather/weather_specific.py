# grab the current weather for Martinsville

import requests
r = requests.get('https://weather.com/weather/today/l/39.43,-86.42')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find('div', attrs={'class':'today_nowcard-temp'})

print('The temperature in Martinsville is',results.text)
