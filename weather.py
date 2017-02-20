import urllib.request
import json

API_KEY = open('wu_api_key.txt').read().strip()
f = urllib.request.urlopen('http://api.wunderground.com/api/'+ API_KEY +'/geolookup/conditions/q/IN/Martinsville.json')

# json_string = f.read()
json_string = f.read().decode('utf-8')

parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']

print ('Current temperature in %s is: %s' % (location, temp_f))
f.close()
