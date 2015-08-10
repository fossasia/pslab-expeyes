'''
expEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3


Program to convert capacitancein pF to relative humidity in %
For Calculations this data sheet is used:
https://www.parallax.com/sites/default/files/downloads/27920-Humidity-Sensor-Datasheet.pdf

Slope of the curve and y-intercept is determined for 4 different linear sections of the response curve 
given in the data sheet using

y=mx+c 		Here y is capacity ( cap) in pF and x is relative humidity (RH) in % and c is y-intercept
m = dy/dx
c =y-mx
and 
x= (y-c)/m

For Humidity 0% to 50%
c= 163 in pF
m = 0.3

For Humidity 50% to 70%
c= 160.25 in pF
m = 0.375

For Humidity 70% to 90%
c= 156.75 in pF
m = 0.425

For Humidity 90% to 100%
c= 136.5 in pF
m = 0.65

'''
#connect HS1011 between IN1 ans GND

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

