'''
Program to convert capacitancein pF to relative humidity in %
For Calculations this data sheet is used:
https://www.parallax.com/sites/default/files/downloads/27920-Humidity-Sensor-Datasheet.pdf

Slope of the curve and y-intercept is determined for 4 different linear sections of the response curve 
given in the data sheet using

y=mx+c 			Here y is capacity ( cap) in pF and x is relative humidity (RH) in %
m = dy/dx
c =y-mx
and 
x= (y-c)/m

For Humidity 0% to 50%
c= 163 in pF
m = 0.3




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
