'''
Accelerometer ADXL 335 can be used for measuring Tilt angle
ADXL335 acceleration measurement range is +/- 3 g. Supply voltage is 1.8 –  3.6 V, however all specifications at the datasheet is given at 3.0 V. This accelerometer has  3 outputs for X,Y,Z axis which voltage is proportional to acceleration on specific axis.

At midpoint when acceleration is 0 g output is typically 1/2 of supply voltage. If a supply voltage is 3V, then output is 1.5 V. Output sensitivity typically is 300 mV/g.

'''

import time, math, sys
if sys.version_info.major==3:			# Python 3 compatibility
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path
from numpy import*
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

angle_x =atan2(-Yaccl,-Zaccl)*57.2957795+180;	

angle_y =atan2(-Zaccl,-Xaccl)*57.2957795+180;
angle_z =atan2(-Xaccl,-Yaccl)*57.2957795+180;

print angle_x
print angle_y
print angle_z
	



