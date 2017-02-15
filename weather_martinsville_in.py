#check Temperature in Martinsville IN 

import bs4 as bs 
import urllib.request

#grab the url
sauce = urllib.request.urlopen('https://www.wunderground.com/cgi-bin/findweather/getForecast?query=Martinsville%2C+IN').read()

soup = bs.BeautifulSoup(sauce,'lxml')

#print the title
print(soup.title.string)

#still working on the part ot parse the temperature with fahrenheit

wx_value = soup.find_all()

print(wx_value)

