'''
GUI Program to plot acceleration data using ADXL335 sensor in real-time


ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3

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

import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath



WIDTH  = 600   # width of drawing canvas
HEIGHT = 400   # height    

class Accl:
	tv = [ [], [], [], [] ]		# Three Lists for Readings time, v1, v2, v3
	TIMER = 5			# Time interval between reads
	MINY = -5			# Voltage range
	MAXY = 5
	running = False
	MAXTIME = 10
	

	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		
		print p.set_voltage(3.6)   # set voltage at PVS  3.6v is operating voltage for ADXL335
		self.running = True
		self.index = 0
		self.tv = [ [], [], [], [] ]
		try:
			self.MAXTIME = int(DURATION.get())
			self.MAXTIME = int(DURATION.get())
			self.MINY = int(TMIN.get())
			self.MAXY = int(TMAX.get())

			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('m/s^2'))
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
		Dur.config(state=NORMAL)
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(1)  	# Read A1
		v2 = p.get_voltage(2)		# Read A2
		v3 = p.get_voltage(3)		# Read IN1
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time
		self.tv[0].append(elapsed)
		self.tv[1].append(v)
		self.tv[2].append(v2)
		self.tv[3].append(v3)
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			g.line(self.tv[0], self.tv[1])  	# Black line for x-axis
			g.line(self.tv[0], self.tv[2],1)	# Red line for y-axis
			g.line(self.tv[0], self.tv[3],2)	# Blue line for z-axis
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
			fn = 'acceleration.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s')%fn)

	def clear(self):
		if self.running == True:
			return
		self.tv = [ [], [], [], [] ]
		g.delete_lines()
		self.msg(_('Cleared Data and Trace'))

	def msg(self,s, col = 'blue'):
		msgwin.config(text=s, fg=col)
	def quit(self):
		sys.exit()

p = eyes.open()
p.disable_actions()
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  		# Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)		# make plot objects using draw.disp
pen = Accl()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)


b3 = Label(cf, text = _('Read Every'))
b3.pack(side = LEFT, anchor = SW)
TGAP = StringVar()
Dur =Entry(cf, width=5, bg = 'white', textvariable = TGAP)
TGAP.set('5')
Dur.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('mS,'))
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('for total'))
b3.pack(side = LEFT, anchor = SW)
DURATION = StringVar()
Total =Entry(cf, width=5, bg = 'white', textvariable = DURATION)
DURATION.set('10')
Total.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Seconds.'))
b3.pack(side = LEFT, anchor = SW)

b3 = Label(cf, text = _('Range'))
b3.pack(side = LEFT, anchor = SW)
TMIN = StringVar()
TMIN.set('-5')
Tmin =Entry(cf, width=5, bg = 'white', textvariable = TMIN)
Tmin.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('to,'))
b3.pack(side = LEFT, anchor = SW)
TMAX = StringVar()
TMAX.set('5')
Tmax =Entry(cf, width=5, bg = 'white', textvariable = TMAX)
Tmax.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('C. '))

b3 = Button(cf, text = _('SAVE to'), command = pen.save)
b3.pack(side = LEFT, anchor = SW)
b3.pack(side = LEFT, anchor = SW)
filename = StringVar()
e1 =Entry(cf, width=15, bg = 'white', textvariable = filename)
filename.set('acceleration.dat')
e1.pack(side = LEFT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
e1.pack(side = LEFT)

b3 = Label(cf, text = _(' Black Line : X-axis'), fg = 'black')
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _(' RED Line : Y-axis'), fg = 'red')
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('    BLUE Line - Z-axis'), fg = 'blue') 
b3.pack(side = LEFT, anchor = SW)
b5 = Button(cf, text = _('QUIT'), command = pen.quit)
b5.pack(side = RIGHT, anchor = N)
b4 = Button(cf, text = _('CLEAR'), command = pen.clear)
b4.pack(side = RIGHT, anchor = N)
b1 = Button(cf, text = _('STOP'), command = pen.stop)
b1.pack(side = RIGHT, anchor = N)
b1 = Button(cf, text = _('START'), command = pen.start)
b1.pack(side = RIGHT, anchor = N)


mf = Frame(root, width = WIDTH, height = 10)
mf.pack(side=TOP)
msgwin = Label(mf,text=_('Message'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)

root.title(_('EYESJUN: Accelerometer ADXL 335'))
root.mainloop()
