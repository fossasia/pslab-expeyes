'''
This GUI program is for detecting presence of various gases like Carbon Monoxide, Methane, LPG etc
Plan is to have one common GUI for four different gas sensors
'''
'''
GUI for interfacing LPG Gas Sensor MQ-4, MQ-6 and MQ-7  with ExpEYES

ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES

Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3



Ref: For calculation of gas concentration in ppm : https://cdn.sparkfun.com/datasheets/Sensors/Biometric/MQ-7%20Ver1.3%20-%20Manual.pdf
'''

#Connections vcc to OD1, GND to GND for all sensors
#MQ-4 AD to IN1
#MQ-6 AD to IN2
#MQ-7 AD to SEN

# Calibration to measure concentration in ppm is to be done

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import time, math, sys
if sys.version_info.major==3:
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path


import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath

WIDTH  = 600   # width of drawing canvas
HEIGHT = 400   # height    

class MQ6:
	tv = [ [], [], [], [] ]			    # Lists for Readings
	TIMER = 10				# Time interval between reads
	MINY = 0				
	MAXY = 5
	running = False
		
	
	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		self.running = True
		self.index = 0
		self.tv = [ [], [], [], [] ]
		p.set_state (10,1)
		try:
			self.MAXTIME = int(DURATION.get())
			self.MINY = int(TMIN.get())
			self.MAXY = int(TMAX.get())
			
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('Volt'))
			self.TIMER = int(TGAP.get())
			Total.config(state=DISABLED)
			Dur.config(state=DISABLED)
			self.msg(_('Starting the Measurements'))
			root.after(self.TIMER, self.update)
		except:
			self.msg(_('Failed to Start'))

	def stop(self):
		self.running = False
		
		Total.config(state=NORMAL)
		Dur.config(state=NORMAL)
		p.set_state (10,0)
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(3)  	# Read IN1
		v1 = p.get_voltage(4)		# Read IN2
		v2 = p.get_voltage(5)		# Read SEN
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time
		self.tv[0].append(elapsed)
		self.tv[1].append(v)
		self.tv[2].append(v1)
		self.tv[3].append(v2)

		if len(self.tv[0]) >= 2:
			g.delete_lines()
			
			g.line(self.tv[0], self.tv[1])   	# For MQ-4
			g.line(self.tv[0], self.tv[2],1)  	# For MQ-6
			g.line(self.tv[0], self.tv[3],2)  	# For MQ-7
		if elapsed > self.MAXTIME:
			self.running = False
			Total.config(state=NORMAL)
			Dur.config(state=NORMAL)
			self.msg(_('Completed the Measurements'))
			return 
		root.after(self.TIMER, self.update)

	
	def save(self):
		try:
			fn = filename.get()
		except:
			fn = 'gas-sensors.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s')%fn)

	def clear(self):
		if self.running == True:
			return
		self.nt = [ [], [] ]
		g.delete_lines()
		self.msg(_('Cleared Data and Trace'))

	def msg(self,s, col = 'blue'):
		msgwin.config(text=s, fg=col)

	def quit(self):
		p.set_state(10,0)
		sys.exit()

p = eyes.open()
p.disable_actions()

root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  

g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)
pt = MQ6()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

b3 = Label(cf, text = _('Read Every'))
b3.pack(side = LEFT, anchor = SW)
TGAP = StringVar()
Dur =Entry(cf, width=5, bg = 'white', textvariable = TGAP)
TGAP.set('10')
Dur.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('mS,'))
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('for total'))
b3.pack(side = LEFT, anchor = SW)
DURATION = StringVar()
Total =Entry(cf, width=5, bg = 'white', textvariable = DURATION)
DURATION.set('100')
Total.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Seconds.'))
b3.pack(side = LEFT, anchor = SW)

b3 = Label(cf, text = _('Range'))
b3.pack(side = LEFT, anchor = SW)
TMIN = StringVar()
TMIN.set('0')
Tmin =Entry(cf, width=5, bg = 'white', textvariable = TMIN)
Tmin.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('to,'))
b3.pack(side = LEFT, anchor = SW)
TMAX = StringVar()
TMAX.set('5')
Tmax =Entry(cf, width=5, bg = 'white', textvariable = TMAX)
Tmax.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('C. '))

b3 = Button(cf, text = _('SAVE to'), command = pt.save)
b3.pack(side = LEFT, anchor = SW)
b3.pack(side = LEFT, anchor = SW)
filename = StringVar()
e1 =Entry(cf, width=15, bg = 'white', textvariable = filename)
filename.set('gas-sensors.dat')
e1.pack(side = LEFT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

b1 = Button(cf, text = _('Xmgrace'), command = pt.xmgrace)
b1.pack(side = LEFT, anchor = SW)


cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
e1.pack(side = LEFT)

b3 = Label(cf, text = _(' Black Line - Methane'), fg = 'black')
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _(' Red Line - Liquified Petroium Gas'), fg = 'red')
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _(' Blue Line - Carbon Monoxide Gas'), fg = 'blue')
b3.pack(side = LEFT, anchor = SW)


b5 = Button(cf, text = _('QUIT'), command = pt.quit)
b5.pack(side = RIGHT, anchor = N)
b4 = Button(cf, text = _('CLEAR'), command = pt.clear)
b4.pack(side = RIGHT, anchor = N)
b1 = Button(cf, text = _('STOP'), command = pt.stop)
b1.pack(side = RIGHT, anchor = N)
b1 = Button(cf, text = _('START'), command = pt.start)
b1.pack(side = RIGHT, anchor = N)

mf = Frame(root, width = WIDTH, height = 10)
mf.pack(side=TOP)
msgwin = Label(mf,text=_('Message'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)

root.title(_('ExpEYES: Gas Sensors GUI'))
root.mainloop()