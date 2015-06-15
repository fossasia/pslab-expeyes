import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

from Tkinter import *
import expeyes.eyesj as eyes, expeyes.eyeplot as eyeplot, expeyes.eyemath as eyemath, time, math

TIMER = 100
WIDTH  = 800        # width of drawing canvas
HEIGHT = 400        # height 
delay = 50		    # Time interval between samples
NP = 450			# Number of samples
data = [] 		    # Of the form, [ [x1,y1], [x2,y2],....] where x and y are vectors
outmask = 1
looping = False


def start():
	global data,looping, NP, delay
	p.disable_actions()
	msec = int(Nsam.get())
	if 1 <= msec <= 200:			# total time
		delay = msec * 1000/ NP	
	else:
		delay = 50 * 1000/NP
	print NP, delay, NP*delay
	g.setWorld(-5,-5, 5, 5,_('Volts'),_('Volts'))
	
	f = float(Freq0.get())
	fr = p.set_sqr1(f*32)
	f = float(Freq.get())
	fr = p.set_sqr2(f*32)
	data = []
	t,v,tt,vv = p.capture2_hr(3,4,NP,delay)
	g.delete_lines()
	g.line(v,vv)
	data.append([v,vv])

def save():
	global data
	s = fn.get()
	if s == '':
		return
	p.save(data, s)
	msgwin.config(text = _('Data saved to file ')+s)

def quit():
	sys.exit()

p = eyes.open()
p.set_sqr1(0)

root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT)	# make plot objects using draw.disp
g.setWorld(0,-5, NP * delay * 0.001, 5,_('mS'),_('V'))

if p == None:
	g.text(0, 0,_('EYES Hardware Not Found. Check Connections and restart the program'),1)
	root.mainloop()
	sys.exit()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

l = Label(cf,text='Sampling Time =')
l.pack(side=LEFT, anchor=SW)
Nsam = Entry(cf,width = 4, bg = 'white')
Nsam.pack(side=LEFT, anchor = SW)
Nsam.insert(END,'50')
l = Label(cf,text='mS')
l.pack(side=LEFT, anchor=SW)
l = Label(cf,text='SINE1=')
l.pack(side=LEFT, anchor=SW)
Freq0 = Entry(cf,width = 10, bg = 'white')
Freq0.pack(side=LEFT, anchor = SW)
Freq0.insert(END,'100')


l = Label(cf,text='SINE2=')
l.pack(side=LEFT, anchor=SW)
Freq = Entry(cf,width = 10, bg = 'white')
Freq.pack(side=LEFT, anchor = SW)
Freq.insert(END,'200')

Start = Button(cf,text =_('DRAW'), command = start, fg = 'blue')
Start.pack(side=LEFT, anchor = SW)


b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
fn = Entry(cf,width = 10, bg = 'white')
fn.pack(side=LEFT, anchor = SW)
fn.insert(END,'lissajous.dat')
b = Button(cf,text =_('QUIT'), command=quit)
b.pack(side=RIGHT, anchor = SW)


mf = Frame(root)				# Message Frame below command frame.
mf.pack(side=TOP, anchor = SW)
msgwin = Label(mf,text = _('Messages'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = SW)

eyeplot.pop_image('pics/lissa.png', _('Lissajous Figures'))
root.title(_('EYES: Lissajous Figures'))
root.mainloop()
