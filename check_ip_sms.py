import bs4 as bs
import urllib.request
from twilio.rest import TwilioRestClient

# pulling the KEY and TOKEN
ACCOUNT_KEY = open('twilio_account.txt').read().strip()
ACCOUNT_TOKEN = open('twilio_token.txt').read().strip()
TWILIO_PHONE = open('twilio_phone.txt').read().strip()
CELL_PHONE = open('cell_phone.txt').read().strip()

sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print the IP address
print(soup.body.text)

# setting up twilio information
client = TwilioRestClient(account=(ACCOUNT_KEY), token=(ACCOUNT_TOKEN))

# sending the IP address via sms
client.messages.create(from_=(TWILIO_PHONE), to=(CELL_PHONE), body=(soup.body.text))
