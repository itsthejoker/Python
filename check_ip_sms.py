import bs4 as bs 
import urllib.request

# pulling KEY and TOKEN
ACCOUNT_KEY = open('twilio_account.txt').read().strip()
ACCOUNT_TOKEN = open('twilio_token.txt').read().strip()

sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce,'lxml')

print(soup.body.text)

from twilio.rest import TwilioRestClient

client = TwilioRestClient(account=(ACCOUNT_KEY), token=(ACCOUNT_TOKEN))

client.messages.create(from_="(619) 273-3961", to = "(812) 360-9210", body = (soup.body.text))
