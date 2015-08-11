'''
ExpEYES-Weather Station GUI

ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES

Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3

This programme is for logging weather data like temperature,barometric pressure, humidity and wind speed.
'''

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext


import time, math, sys
if sys.version_info.major==3:
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path

import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath

WIDTH  = 1000   # width of drawing canvas
HEIGHT = 600   # height    


class WS:
	tv = [ [], [], [], [], [] ]		# Three Lists for Readings time, v  , v1 and v2
	TIMER = 500			# Time interval between reads
	MINY = 0			# Voltage range
	MAXY = 100
	running = False
	MAXTIME = 10

	
	def v2t(self, v):			# Convert Voltage to Temperature for LM35
		
		t = v * 100
		return t
	def start(self):
		self.running = True
		self.index = 0
		p.set_state(10,1)
		self.tv = [ [], [], [], [], [] ]
		try:
			self.MAXTIME = int(DURATION.get())
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('Data'))
			self.TIMER = int(TGAP.get())
			Total.config(state=DISABLED)
			Dur.config(state=DISABLED)
			self.msg(_('Starting the Measurements'))
			root.after(self.TIMER, self.update)
		except:
			self.msg(_('Failed to Start'))
			pass

	def stop(self):
		self.running = False
		Total.config(state=NORMAL)
		Dur.config(state=NORMAL)
		self.msg(_('User Stopped the measurements'))


	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(4) 			# Read IN2 for Time and Temperature ...Read IN2 as IN1 is useful for capacity measurements and is required for HS1101 sensor for humidity measurements
		
		
		v1 = p.get_voltage(3) 				# Read IN1  for Humidity in %  
'''
Modification needed as capacity of HS1101 can be measured at IN1
'''
		v2 = p.get_voltage(2)				# Read A2 for Wind Speed
		v3 = p.get_voltage(5)				# Read SEN for Barrometric Pressure
		# calculations of various parameters from v, v1 v2 and v3 to be done.humidity from v1 wind speed from v2 and pressure from v3
		
		
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time   # To be done : make changes to have system time

		temp = self.v2t(v)
		self.tv[1].append(temp)
		self.tv[0].append(elapsed)
		self.tv[1].append(temp)
		self.tv[2].append(v1)
		self.tv[3].append(v2)
		self.tv[4].append(v3)
		if len(self.tv[0]) >= 3:
			g.delete_lines()
			g.line(self.tv[0], self.tv[1])
			g.line(self.tv[0], self.tv[2],1)
			g.line(self.tv[0], self.tv[3],2)
			g.line(self.tv[0], self.tv[4],3)
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
			fn = 'weather-station.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s')%fn)

	def clear(self):
		if self.running == True:
			return
		self.tv = [ [], [], [], [], [] ]
		g.delete_lines()
		self.msg(_('Cleared Data and Trace'))

	def msg(self,s, col = 'blue'):
		msgwin.config(text=s, fg=col)



p = eyes.open()
p.disable_actions()
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)	# make plot objects using draw.disp
log = WS()


cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

b3 = Label(cf, text = _('Read Every'))
b3.pack(side = LEFT, anchor = SW)
TGAP = StringVar()
Dur =Entry(cf, width=5, bg = 'white', textvariable = TGAP)
TGAP.set('1000')
Dur.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('mS,'))
b3.pack(side = LEFT, anchor = SW)


b3 = Label(cf, text = _('for total'))
b3.pack(side = LEFT, anchor = SW)
DURATION = StringVar()
Total =Entry(cf, width=5, bg = 'white', textvariable = DURATION)
DURATION.set('100')
Total.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Seconds'))
b3.pack(side = LEFT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)


b1 = Button(cf, text = _('START'), command = log.start)
b1.pack(side = LEFT, anchor = N)
b1 = Button(cf, text = _('STOP'), command = log.stop)
b1.pack(side = LEFT, anchor = N)
b4 = Button(cf, text = _('CLEAR'), command = log.clear)
b4.pack(side = LEFT, anchor = N)

b3 = Button(cf, text = _('SAVE to'), command = log.save)
b3.pack(side = LEFT, anchor = N)
filename = StringVar()
e1 =Entry(cf, width=15, bg = 'white', textvariable = filename)
filename.set('weather-station.dat')
e1.pack(side = LEFT)
b5 = Button(cf, text = _('QUIT'), command = sys.exit)
b5.pack(side = RIGHT, anchor = N)

mf = Frame(root, width = WIDTH, height = 10)
mf.pack(side=TOP)
msgwin = Label(mf,text=_('Message'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)


eyeplot.pop_image('pics/image-name.png', _('---'))  # save the image in the same directory as of the program
root.title(_('Weather Station Data Logger'))
root.mainloop()
