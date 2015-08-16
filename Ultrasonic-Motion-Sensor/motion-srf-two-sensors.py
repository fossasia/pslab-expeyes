'''
ExpEYES program developed as a part of GSoC-2015 project 
(Modified from the program developed for GSoC-14)

Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3

this program allows user to use TWO motion sensors (srf-05 modules) and plot both the graphs
in real-time.
This can be used for studying collisions, conservation of momentum etc...
'''

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import expeyes.eyesj as eyes, expeyes.eyeplot as eyeplot,  time, sys, math

WIDTH  = 600   # width of drawing canvas
HEIGHT = 400   # height    
vs = 0.034000

class SRF2:
	tv = [ [], [], [] ]		# Lists for Readings
	TIMER = 10			# Time interval between reads
	MINY = 0		
	MAXY = 80
	running = False
	MAXTIME = 10

	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		self.running = True
		self.index = 0
		self.tv = [ [], [], [] ]
		try:
			self.MAXTIME = int(DURATION.get())
			self.MAXY = int(MAXDIST.get())
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('cm'))
			Dur.config(state=DISABLED)
			self.msg(_('Starting the Measurements'))
			root.after(self.TIMER, self.update)
		except:
			self.msg(_('Failed to Start'))

	def stop(self):
		self.running = False
		Dur.config(state=NORMAL)
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		tt = p.srfechotime(9,0)
		dist = (tt-400) *vs/2
		tt2 = p.srfechotime(8,3)
		dist2 = (tt2-400) *vs/2
		if len(self.tv[0]) == 0:
			self.start_time = time.time()
			elapsed = 0
		else:
			elapsed = time.time() - self.start_time
		self.tv[0].append(elapsed)
		self.tv[1].append(dist)
		self.tv[2].append(dist2)
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			g.line(self.tv[0], self.tv[1])
			g.line(self.tv[0], self.tv[2],1)
		if elapsed > self.MAXTIME:
			self.running = False
			Dur.config(state=NORMAL)
			self.msg(_('Completed the Measurements'))
			return 
		root.after(self.TIMER, self.update)

	def save(self):
		try:
			fn = filename.get()
		except:
			fn = 'motion2.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s')%fn)

	def clear(self):
		if self.running == True:
			return
		self.tv = [ [], [] ]
		g.delete_lines()
		self.msg(_('Cleared Data and Trace'))

	def msg(self,s, col = 'blue'):
		msgwin.config(text=s, fg=col)

p = eyes.open()
p.disable_actions()
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)	# make plot objects using draw.disp
pen = SRF2()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)


b3 = Label(cf, text = _('Digitize for'))
b3.pack(side = LEFT, anchor = SW)
DURATION = StringVar()
Dur =Entry(cf, width=5, bg = 'white', textvariable = DURATION)
DURATION.set('10')
Dur.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Seconds.'))
b3.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Max Dist='))
b3.pack(side = LEFT, anchor = SW)
MAXDIST = StringVar()
Dis =Entry(cf, width=5, bg = 'white', textvariable = MAXDIST)
MAXDIST.set('60')
Dis.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('cm'))
b3.pack(side = LEFT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b1 = Button(cf, text = _('START'), command = pen.start)
b1.pack(side = LEFT, anchor = N)
b1 = Button(cf, text = _('STOP'), command = pen.stop)
b1.pack(side = LEFT, anchor = N)
b4 = Button(cf, text = _('CLEAR'), command = pen.clear)
b4.pack(side = LEFT, anchor = N)
b1 = Button(cf, text = _('Xmgrace'), command = pen.xmgrace)
b1.pack(side = LEFT, anchor = N)
b3 = Button(cf, text = _('SAVE to'), command = pen.save)
b3.pack(side = LEFT, anchor = N)
filename = StringVar()
e1 =Entry(cf, width=15, bg = 'white', textvariable = filename)
filename.set('motion2.dat')
e1.pack(side = LEFT)
b5 = Button(cf, text = _('QUIT'), command = sys.exit)
b5.pack(side = RIGHT, anchor = N)

mf = Frame(root, width = WIDTH, height = 10)
mf.pack(side=TOP)
msgwin = Label(mf,text=_('Message'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)


#eyeplot.pop_image('pics/imagename.png', _('write the name of expt setup image'))
root.title(_('Motion Graphs Using Two Position Sensors'))
root.mainloop()
