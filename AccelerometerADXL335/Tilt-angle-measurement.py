'''
GUI Program to plot acceleration data using ADXL335 sensor in real-time


ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3

Calibration:
For calculating acceleration in terms of g
Ref: https://www.sparkfun.com/datasheets/Components/SMD/adxl335.pdf
For 	0g  	v = 1.61 volt
	-1g	v = 1.31 volt
	+1g 	v = 1.91 volt
Sensitivity 	0.3v/g
 
For tilt angle calculation:
atan2(y, x)-------- Returns atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.



'''
import gettext					#Internationalization
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext


import time, math, sys
if sys.version_info.major==3:			# Python 3 compatibility
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path


from math import*

# from numpy import*
import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath
p=eyes.open()


		
print p.set_voltage(3.6)   # set voltage at PVS  3.6v is operating voltage for ADXL335
		
t,v = p.get_voltage_time(1)  	# Read A1
v2 = p.get_voltage(2)		# Read A2
v3 = p.get_voltage(3)		# Read IN1

Xaccl = (v-1.6) / 0.3
Yaccl = (v2-1.6) / 0.3
Zaccl = (v3-1.6) / 0.3

angle_x =atan2(-Yaccl,-Zaccl)*57.2957795+180;	# The rotation(for x axis) is calculated using atan2 function. It calculates angle from length of y, z vectors. *57.2957795 – is conversation of radian to degree. +180 is for offset.

angle_y =atan2(-Zaccl,-Xaccl)*57.2957795+180;

angle_z =atan2(-Xaccl,-Yaccl)*57.2957795+180;

print "Tilt angle X-axis = ", angle_x, "degree"
print "Tilt angle Y-axis = ", angle_y, "degree"
print "Tilt angle z-axis = ", angle_z, "degree"
	
