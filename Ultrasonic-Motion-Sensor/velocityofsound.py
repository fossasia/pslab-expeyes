'''
Program for measuring velocity of sound using ExpEYES
License : GNU GPL
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import expeyes.eyes as eyes, expeyes.eyeplot as eyeplot, expeyes.eyemath as eyemath, time, sys, math

TIMER = 100
WIDTH  = 800        # width of drawing canvas
HEIGHT = 400        # height 
delay = 10		    # Time interval between samples
NP = 200			# Number of samples
data = [] 		    # Of the form, [ [x1,y1], [x2,y2],....] where x and y are vectors
outmask = 1
looping = False

def fset(f):
	s = '%5.1f'%f
	Freq.delete(0,END)
	Freq.insert(0,s)

def update():
	global data, looping, NP, delay
	data = []
	if looping == False:
		return
	t,v,tt,vv = p.capture01(NP,delay)
	for k in range(len(vv)): vv[k] -= 2.5
	g.delete_lines()
	g.line(t,v)
	g.line(tt,vv,1)
	data.append([t,v])
	data.append([tt,vv])
	fa = eyemath.fit_sine(t, v)
	if fa != None:
		#g.line(t,fa[0], 8)
		rms = p.rms(v)
		f0 = fa[1][1] * 1000
		s = _('Phase = %5.0f deg')%(fa[1][2]*180/math.pi)
	else:
		s = _('No Signal')
	msgwin.config(text=s)			# CRO part over	
	root.after(TIMER, update)	


def start():
	global looping, NP, delay
	if A1.get() == 1:
		p.set_upv(5)
		f1 = float(Freq.get())
		fr = p.set_sqr1(f1)
		fset(fr)
		looping = True
		p.adc2cmp(7)
		p.enable_wait_rising(4)
		root.after(TIMER, update)
	else:
		looping = False
		p.set_sqr1(0)

def do_fft():
	global data, delay, NP
	if data == []: return
	fr,tr = eyemath.fft(data[0][1], delay * 0.001)
	p.save([ [fr,tr] ], 'FFT.dat')
	p.grace([ [fr,tr] ], _('freq'), _('power'))
	msgwin.config(text = _('Fourier transform Saved to FFT.dat.'))

def save():
	global data
	s = fn.get()
	if s == '':
		return
	p.save(data, s)
	msgwin.config(text = _('Data saved to file ')+s)

def xmgrace():		# Send the data to Xmgrace
	global data
	p.grace(data, _('milliSeconds'), _('Volts'))

def quit():
	p.write_outputs(0)
	sys.exit()

p = eyes.open()
p.loadall_calib()
p.set_sqr1(0)

root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT)	# make plot objects using draw.disp
g.setWorld(0,-5, NP * delay * 0.001, 5,_('mS'),_('V'))

if p == None:
	g.text(0, 0,_('EYES Hardware Not Found. Check Connections and restart the program'),1)
	root.mainloop()
	sys.exit()
p.set_voltage(1,5)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

A1 = IntVar()
cb1 = Checkbutton(cf,text =_('ON/OFF'), command = start, variable=A1, fg = 'blue')
cb1.pack(side=LEFT, anchor = SW)
A1.set(0)

l = Label(cf,text=_('Freq='))
l.pack(side=LEFT, anchor= SW)
Freq = Entry(cf,width = 10, bg = 'white')
Freq.pack(side=LEFT, anchor = SW)
Freq.insert(END,'4000')

b = Button(cf,text =_('Xmgrace'), command=xmgrace)
b.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('FFT'), command=do_fft)
b.pack(side=LEFT, anchor = SW)

b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
fn = Entry(cf,width = 10, bg = 'white')
fn.pack(side=LEFT, anchor = SW)
fn.insert(END,'sound.dat')
b = Button(cf,text =_('QUIT'), command=quit)
b.pack(side=RIGHT, anchor = SW)


mf = Frame(root)				# Message Frame below command frame.
mf.pack(side=TOP, anchor = SW)
msgwin = Label(mf,text = _('Messages'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = SW)

eyeplot.pop_image('pics/sound-vel.png', _('Velocity of Sound'))
root.title(_('EYES: Velocity of Sound'))
root.mainloop()
