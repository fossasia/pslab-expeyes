'''
PSLab program for auto-tweeting weather station data

Install tweepy module
Add API keys from tweetter spp
'''

import tweepy
from datetime import datetime

API_KEY = 'YOUR API KEY'
API_SECRET = 'YOUR API SECRET'
ACCESS_TOKEN = 'YOUR ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR ACCESS TOKEN SECRET'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tempfile = open("address of the weather data file")
thetext = tempfile.read()
tempfile.close()
tempdata = thetext.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = str(temperature / 1000)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')

api.update_status(temperature + " C at " + thetime)
