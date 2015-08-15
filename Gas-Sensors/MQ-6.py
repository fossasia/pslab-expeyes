'''
GUI for interfacing LPG Gas Sensor MQ-6 with ExpEYES
The GUI program is same for all gas sensors except the calibration factor 
to convert output voltage to gas concentartion in ppm.

ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES

Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3


'''

#Connections vcc to OD1, GND to GND and AD to IN2

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
	tv = [ [], [] ]			    # Lists for Readings
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
		self.tv = [ [], [] ]
		p.set_state (10,1)
		try:
			self.MAXTIME = int(DURATION.get())
			self.MINY = int(TMIN.get())
			self.MAXY = int(TMAX.get())
			
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_(''),_(''))
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
		p.set_state (10,0)

	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(4)  # Read IN2
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time
		self.tv[0].append(elapsed)
		self.tv[1].append(v)
		
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			
			g.line(self.tv[0], self.tv[1],1)   
			
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
			fn = 'MQ-6.dat'
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
filename.set('KY-003.dat')
e1.pack(side = LEFT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

b1 = Button(cf, text = _('Xmgrace'), command = pt.xmgrace)
b1.pack(side = LEFT, anchor = SW)


cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
e1.pack(side = LEFT)



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

root.title(_('MQ-6 LPG Gas Sensor'))
root.mainloop()
