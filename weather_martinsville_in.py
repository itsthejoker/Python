#check Temperature in Martinsville IN 

from bs4 import BeautifulSoup
import requests

#grab the url
site = requests.get('https://www.wunderground.com/cgi-bin/findweather/getForecast?query=Martinsville%2C+IN')

soup = BeautifulSoup(site.text, 'html.parser')

#drilling down on data
site2 = soup.find('div',{'id':'curTemp'})
site3 = site2.find('span',{'class':'wx-value'})

print(site3.text, 'Degrees Fahrenheit')
