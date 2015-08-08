'''
expEYES program for measuring temperature using LM35 sensor
Developed as a part of GSoC Project 
Mentor Organisation : FOSSASIA
License : GNU GPL version 3
'''
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

class LM35:
	tv = [ [], [], [] ]			# Lists for Readings
	TIMER = 500				# Time interval between reads
	MINY = 0				# Temperature range
	MAXY = 100
	running = False
				
	
	def v2t(self, v):			# Convert Voltage to Temperature for LM35
		
		t = v * 100
		return t

	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		self.running = True
		self.index = 0
		self.tv = [ [], [], [] ]
		p.set_state (10,1)
		try:
			self.MAXTIME = int(DURATION.get())
			self.MINY = int(TMIN.get())
			self.MAXY = int(TMAX.get())
			
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time in second'),_('Temp in celsius'))
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
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(4)  # # Read IN2 as IN1 is useful for capacity measurements and is required for HS1101 sensor for humidity measurements
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time
		self.tv[0].append(elapsed)
		
		temp = self.v2t(v)
		self.tv[1].append(temp)
		fahrenheit= (9/5 * temp )+ 32
		self.tv[2].append(fahrenheit)
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			
			g.line(self.tv[0], self.tv[1],1)    # red line - temperature in celsius scale
			g.line(self.tv[0], self.tv[2],2)	# blue line - temperature in fahrenheit scale
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
			fn = 'LM35.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s')%fn)

	def clear(self):
		if self.running == True:
			return
