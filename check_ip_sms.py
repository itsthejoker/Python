import bs4 as bs
import urllib.request
from twilio.rest import Client
from API_KEYS import ACCOUNT_TOKEN, ACCOUNT_KEY, TWILIO_PHONE, CELL_PHONE

sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print the IP address
print(soup.body.text)

# setting up twilio information
client = Client(account=(ACCOUNT_KEY), token=(ACCOUNT_TOKEN))

# sending the IP address via sms
client.messages.create(from_=(TWILIO_PHONE), to=(CELL_PHONE), body=(soup.body.text))
