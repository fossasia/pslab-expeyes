'''
PSLab program for auto-tweeting weather station data
This can be embeded in weather station program

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
'''
#tempfile = open("/sys/bus/w1/devices/28-00000XXXXXX/w1_slave")
#thetext = tempfile.read()
tempfile.close()
tempdata = thetext.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = str(temperature / 1000)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')
'''
temperature = 27 
temperature = str(27)
thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')
api.update_status(" Temperature at Belgaum - India  "+ temperature + " C at " + thetime + " #loklak #fossasia @lklknt   Testing ... :) ")
