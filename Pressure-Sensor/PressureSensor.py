'''
A simple code to test pressure sensor SPD015AAsil by SMARTEC

Connections
Pin 1 and Pin 5 not connected
Pin 2 VCC  Connect to PVS of ExpEYES at +5V , Pin 3 Output  to IN1 / A1
Pin 4  GND  Between pin 2 and 4 connect a 100nF capacitor
Result needs to be calibrated.
'''

import pylab
import expeyes.eyesj
p=expeyes.eyesj.open()
print p.set_voltage(5.0) 
print p.get_voltage(1)   
t,v = p.capture(1,300,100)
plot(t,v)
show()
