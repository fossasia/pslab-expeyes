'''
ExpEYES program for voltammetric studies.
Voltammetric studies to plot voltammograms are done using costly apparatus in research labs. 
ExpEYES can be effectly used for this purpose.


ExpEYES program developed as a part of GSoC-2015 project
Project Tilte: Sensor Plug-ins, Add-on devices and GUI Improvements for ExpEYES
Mentor Organization:FOSSASIA
Mentors: Hong Phuc, Mario Behling, Rebentisch
Author: Praveen Patil
License : GNU GPL version 3


# Modifications needed to change voltage from +1 to -1 volt 
'''
# Connections : PVS to main electrode,Ref. Electrode to GND
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



TIMER = 100
WIDTH  = 500   # width of drawing canvas
HEIGHT = 350   # height 
VPERDIV = 0.25		# Volts per division, vertical scale
delay = 500			# Time interval between samples
NP = 400			# Number of samples
data = [ [], [] ]
history = []		# Data store
trial = 0			# trial number
data = [ [], [] ]	# Current & Voltage


# to find peaks of the curve...

def find_peaks(ta,va):   # returns the index of the peaks found
	vmin = 5.0
	vmax = -5.0
	p1 = 0		# index of the peaks
	p2 = 0
	t1 = t2 = 0
	size = len(ta)
	for i in range(size):
		if va[i] < vmin:
			vmin = va[i]
			p1 = i
		if va[i] > vmax:
			vmax = va[i]
			p2 = i
	#print p1,p2,vmin, vmax
	if p1 < p2:			# return left side peak first
		return p1,p2
	else:
		return p2,p1


def base_scan():
	global data, history, trial, NP, delay, noise
	t, v = p.capture_hr(1,NP,delay)
	g.delete_lines()
	g.line(t,v,trial)
	running = True
	data = [ [], [] ]
	p1,p2 = find_peaks(t,v)
	noise = abs(v[p1])
	msgwin.config(text = _('Voltage Scan on Coil Done. Noise Voltage = %5.3f V')%noise)
	root.after(TIMER, update)

def update():
	global data, history, trial, NP, delay, noise
	p.set_voltage(1.0) # set voltage on PVS
        t, v= p.capture_hr(1,NP,delay)		# Scan for 5 times more
	p1,p2 = find_peaks(t,v)
	#print v[p1], v[p2]
	if abs(v[p1] - noise) > 0.5 and p1 < .9*NP:  # Signal at least 0.5 volts above noise
		index = p1-50
		tbeg = t[index]
		'''
		tn = []
		vn = []
		while index < p1 + 150:
			#print index
			tn.append(t[index]-tbeg)
			vn.append(v[index])
			index += 1
		'''
		g.delete_lines()
		g.line(t,v,trial)
		data = [t,v]
		s = _('Peak voltages %5.2f and %5.3f separated by %5.3f msec') %(v[p1], v[p2], t[p2]-t[p1])
		msgwin.config(text = s)
		#print len(tn), len(vn), v[p1], v[p2]
		history.append(data)
		trial += 1
		return				
	root.after(TIMER, update)

def clear():
	global history, trial
	g.delete_lines()
	history = []
	trial = 0

def save():
	global history
	s = fn.get()
	if s == '':
		return
	p.save(history, s)
	msgwin.config(text = _('Data saved to file ')+s)

def viewall():		# Send the data to Xmgrace
	global history
	g.delete_lines()	
	i = 0
	for t,v in history:
		g.line(t,v,i)
		i += 1

p = eyes.open()
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT)	# make plot objects using draw.disp
g.setWorld(0,-5*VPERDIV, NP * delay * 0.001, 5*VPERDIV,_('mS'),_('V'))

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b = Button(cf,text =_('Start Scanning'), command= base_scan)
b.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
fn = Entry(cf,width = 10, bg = 'white')
fn.pack(side=LEFT, anchor = SW)
fn.insert(END,'ind.dat')
b = Button(cf,text =_('QUIT'), command=sys.exit)
b.pack(side=RIGHT, anchor = SW)
b = Button(cf,text =_('VIEW'), command=viewall)
b.pack(side=RIGHT, anchor = SW)
b4 = Button(cf, text = _('CLEAR'), command = clear)
b4.pack(side = RIGHT, anchor = N)

mf = Frame(root)				# Message Frame below command frame.
mf.pack(side=TOP, anchor = SW)
msgwin = Label(mf,text = _('Messages'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = SW)


root.title(_('EYESJUN: Voltamogram'))
root.mainloop()
