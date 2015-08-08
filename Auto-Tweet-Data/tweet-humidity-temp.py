'''
expEYES program developed as a part of GSoC-2015 project
Mentor Organization:FOSSASIA
Author: Praveen Patil
License : GNU GPL version 3


Program to auto tweet humidity and temperature data from ExpEYES


'''
#connect HS1011 between IN1 ans GND
#connect LM35 
import tweepy
from datetime import datetime
import expeyes.eyesj
p= expeyes.eyesj.open()

cap = p.measure_cap()
if cap< 180: 
         RH= (cap -163)/0.3
elif 180<cap<186: 
        RH= (cap -160.25)/0.375
elif 186<cap<195: 
        RH= (cap -156.75)/0.425
else:
	RH= (cap -136.5)/0.65

#print RH, '%'
print ('Relative Humidity = %0.2f')%RH,'%'


#To measure temperature
# Connect LM35 to IN2, OD1 and GND

v= p.get_voltage(4)
temp = v * 100
print ('Temperature = %0.2f')%temp



API_KEY = 'ysYwSGb9bC5aqDymjj1SVUBEm'
API_SECRET = 'dr3EuqeC6rEguNbcTEPoGLyYel3TqV87WqtV3PvD80SRxebXFQ'
ACCESS_TOKEN = '3405995939-agYD9QwRu3E0JDa4SMAlfl4PEHRBhiMcIPp2XwL'
ACCESS_TOKEN_SECRET = '1nenIkhT7wvM4J4FJvr9jLqxdIFvYxzV2BzFuWEign5YI'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')
api.update_status(" Humidity and Temperature at Belgaum - India is  "  '%0.2f'%RH + "% and " + '%0.1f'%temp  + " C at " + thetime + " #loklak #fossasia @lklknt   Testing ... :) " )
