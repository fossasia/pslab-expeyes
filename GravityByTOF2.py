
import expeyes.eyesj
p= expeyes.eyesj.open()

hvals = [20.,25.,30.,35.,40.,45.,50.,55.,60.,65.,70.,75.,80.]       # List of heights
NP = len(hvals)
tvals = [-1.]*NP							# List of corresponding Time of Flight values
Hstrings = ['H']*NP
Results = [None]*NP							# List of Label Widgets

def calc_g():
	x = []
	y = []
	for k in range(NP):
		try:
			h = float(Hstrings[k].get())
			if tvals[k] > 0:
				t = tvals[k]
			else:
				continue
			x.append(t)
			y.append(h)
		except:
			continue
	print x , y
	if len(x) < 3:
		return
	y,p=em.fit_qdr(x,y)
	g = p[0] * 2
	msgwin.config(text = _('Value of "g" by fitting the data points = %5.2f') %g)

def save():
	x = []
	y = []
	for k in range(NP):
		try:
			h = float(Hstrings[k].get())
			if tvals[k] > 0:
				t = tvals[k]
			else:
				continue
			x.append(t)
			y.append(h)
		except:
			continue

	fname =Fn.get()
	f = open(fname,'w')
	for k in range(len(x)):
		f.write('%5.4f  %5.2f\n'%(x[k], y[k]))
	f.close()

def attach():
	p.write_outputs(1)

def get_tof(index):
	try:
		h = float(Hstrings[index].get())
	except:
		Results[index].config(text = _('Invalid H'))
		return
	print index, h
	if (p.read_inputs() & 4) == 0:    # ID2 is currently LOW
		t = p.clr2rtime(0,2)*1.0e-6
	else:
		t = p.clr2ftime(0,2)*1.0e-6
	if t > 0:
		tvals[index] = t
		g = 2*h/t**2
		print g
		Results[index].config(text = _('t=%6.4f g=%5.1f') %(t,g))
	else:
		Results[index].config(text = _('Timeout Err'))


p = eyes.open()
p.disable_actions()

root = Tk()
f1 = Frame(root)
f1.pack(side=TOP,  fill = BOTH, expand = 1)
for k in range(NP):
	cf = Frame(f1)
	cf.pack(side=TOP,  fill = BOTH, expand = 1)
	b = Button(cf, text = _('Attach Ball at H='), command = attach)
	b.pack(side = LEFT, anchor = N)
	Hstrings[k] = StringVar()
	h =Entry(cf, width=5, bg = 'white', textvariable = Hstrings[k])
	h.pack(side=LEFT)
	Hstrings[k].set(str(hvals[k]))
	l = Label(cf, text = _('cm'))
	l.pack(side = LEFT, anchor = SW)
	b = Button(cf, text = _('Measure TOF'), command = lambda i=k : get_tof(i))
	b.pack(side = LEFT, anchor = N)
	Results[k] = Label(cf, text = ' '*30)
	Results[k].pack(side = LEFT, anchor = SW)

mf = Frame(root)
mf.pack(side=TOP,  fill = BOTH, expand = 1)
msgwin = Label(mf,text=_('Acceleration due to gravity by Time of Flight'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)

cf = Frame(root)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b5 = Button(cf, text = _('FIT'), command = calc_g)
b5.pack(side = LEFT, anchor = N)
b = Button(cf,text =_('Save to'), command=save)
b.pack(side=LEFT, anchor = SW)
Fn = Entry(cf,width = 10, bg = 'white')
Fn.pack(side=LEFT, anchor = SW)
Fn.insert(END,'gravity.dat')
b5 = Button(cf, text = _('QUIT'), command = sys.exit)
b5.pack(side = RIGHT, anchor = N)

eyeplot.pop_image('pics/g-tof.png', _('Gravity by TOF'))
root.title(_('Gravity by Time of Flight'))
root.mainloop()
