# using json and the Weather Underground API
# pulling weather data and displaying

import urllib.request
import json
from API_KEYS import WEATHER_UNDERGROUND_KEY

# getting the url
f = urllib.request.urlopen('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/IN/Martinsville.json')

# decoding the text
json_string = f.read().decode('utf-8')

# parsing the information
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
relative_humidity = parsed_json['current_observation']['relative_humidity']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_gust = parsed_json['current_observation']['wind_gust_mph']
pressure_mb = parsed_json['current_observation']['pressure_mb']
feels_like = parsed_json['current_observation']['feelslike_f']
visibility_mi = parsed_json['current_observation']['visibility_mi']
precipitation_in = parsed_json['current_observation']['precip_today_in']
weather = parsed_json['current_observation']['weather']

# printing the location and temperature
print('Current temperature in %s is: %s F' % (location, temp_f))
print('Relative Humidity is at: %s' % (relative_humidity))
print('Winds are: %s mph' % (wind_mph))
print('Wind gusts are at: %s mph' % (wind_gust))
print('Pressure is: %s mb' % (pressure_mb))
print('Feels like: %s F' % (feels_like))
print('Visibility is: %s mi' % (visibility_mi))
print('Precipitation today: %s inches' % (precipitation_in))
print('General weather is: %s' % (weather))
f.close()
