'''

'''


import expeyes.eyesj as eyes
import expeyes.eyeplot as eyeplot
import expeyes.eyemath as eyemath


TIMER = 100
WIDTH  = 500   # width of drawing canvas
HEIGHT = 350   # height 
VPERDIV = 1.0		# Volts per division, vertical scale
delay = 20			# Time interval between samples
NP = 100			# Number of samples
data = [ [], [] ]
history = []		# Data store
trial = 0			# trial number
data = [ [], [] ]	# Current & Voltage


def capture(i):
	global data, history, trial
	s = ''
	if i == 0:  # Take OD1 LOW. To HIGH before capture
		p.set_state(10,0)		# OD1 to LOW
		p.enable_set_high(10)	# enable HI on OD1
	elif i == 1:  # Take OD1 HI. To HIGH before capture
		p.set_state(10,1)		# OD1 to HI
		p.enable_set_low(10)	# enable LO on OD1
	else:
		p.set_state(11,0)		# CCS OFF
		time.sleep(0.5)
		p.enable_set_high(11)	# enable HI on CCS	
	time.sleep(0.5)
	t, v = p.capture_hr(1,NP,delay)
	g.line(t,v, trial)
	data = t,v
	history.append(data)
	trial += 1
	msgwin.config(text = _('Done'))

def view_all():
	global history
	g.delete_lines()
	c = 0
	for t,v in history:
		g.line(t,v,c)
		c += 1

def fit_curve():
	global data
	fa = eyemath.fit_exp(data[0], data[1])
	if fa != None:
		pa = fa[1]
		rc = abs(1.0 / pa[1])
		g.line(data[0],fa[0],1)
		dispmsg(_('RC = %5.2f mSec')%rc)
	else:
		dispmsg(_('Failed to fit the curve with V=Vo*exp(-t/RC)'))

def dispmsg(s):
	msgwin.config(text=s)

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

def xmgrace():		# Send the data to Xmgrace
	global history
	p.grace(history, _('milliSeconds'), _('Volts'))

def set_timebase(w):
	global delay, NP, NC, VPERDIV
	divs = [0.050, 0.100, 0.200, 0.500, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
	msperdiv = divs[int(timebase.get())]
	totalusec = int(msperdiv * 1000 * 10)
	NP = 100								# Assume 100 samples to start with
	delay = int(totalusec/100)				# Calculate delay
	if delay < 10:
		sf = 10/delay
		delay = 10
		NP = NP/sf
	elif delay > 1000:
		sf = delay/1000
		delay = 1000
		NP = NP * sf
	g.setWorld(0, 0*VPERDIV, NP * delay * 0.001, 5*VPERDIV,_('mS'),_('V'))

p = eyes.open()
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  # Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)	# make plot objects using draw.disp
g.setWorld(0, 0, 20,5,_('V'),_('mA'))
if p == None:
	g.text(0, 0,_('EYES Hardware Not Found. Check Connections and restart the program'),1)
	root.mainloop()
	sys.exit()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

l = Label(cf, text=_('mS/div'))
l.pack(side=LEFT, anchor = SW )
timebase = Scale(cf,command = set_timebase, orient=HORIZONTAL, length=50, showvalue=False,\
	from_ = 0, to=9, resolution=1)
timebase.pack(side=LEFT, anchor = SW)
timebase.set(3)
b = Button(cf,text =_('0 to 5V STEP'), command= lambda i=0:capture(i))
b.pack(side=LEFT, anchor = SW)
b = Button(cf,text =_('5 to 0V STEP'), command= lambda i=1:capture(i))
b.pack(side=LEFT, anchor = SW)
b = Button(cf,text =_('CC Charge'), command= lambda i=2:capture(i))
b.pack(side=LEFT, anchor = SW)
b = Button(cf,text =_('Calculate RC'), command=fit_curve)
b.pack(side=LEFT, anchor = SW)
b = Button(cf,text =_('QUIT'), command=sys.exit)
b.pack(side=RIGHT, anchor = SW)

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b = Button(cf,text =_('ViewAll'), command=view_all)
b.pack(side=LEFT, anchor = SW)
b = Button(cf,text =_('Xmgrace'), command=xmgrace)
b.pack(side=LEFT, anchor = SW)
b4 = Button(cf, text = _('CLEAR'), command = clear)
b4.pack(side = LEFT, anchor = N)
b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
fn = Entry(cf,width = 10, bg = 'white')
fn.pack(side=LEFT, anchor = SW)
fn.insert(END,'rc.dat')

mf = Frame(root)				# Message Frame below command frame.
mf.pack(side=TOP)
msgwin = Label(mf,text = '', fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH)

eyeplot.pop_image('pics/xxxx.png', _(''))
root.title(_('Battery Characteristics'))
root.mainloop()

