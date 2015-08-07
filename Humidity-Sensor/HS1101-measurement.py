'''
https://www.parallax.com/sites/default/files/downloads/27920-Humidity-Sensor-Datasheet.pdf

'''
cap = 190
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
