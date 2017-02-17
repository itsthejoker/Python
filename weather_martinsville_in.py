#check Temperature in Martinsville IN 

from bs4 import BeautifulSoup
import requests

#grab the url
the_url = requests.get('https://www.wunderground.com/cgi-bin/findweather/getForecast?query=Martinsville%2C+IN')

soup = BeautifulSoup(the_url.text, 'html.parser')

#drilling down on data
url_curtemp = soup.find('div',{'id':'curTemp'})
wx_value = url_curtemp.find('span',{'class':'wx-value'})

print (soup.title.text)
print(wx_value.text, 'Degrees Fahrenheit')