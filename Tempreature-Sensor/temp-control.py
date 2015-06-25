'''
from Tkinter import *
import expeyes.eyes as eyes, expeyes.eyeplot as eyeplot, expeyes.eyemath as eyemath, time, sys, math

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

WIDTH  = 600   # width of drawing canvas
HEIGHT = 400   # height    
MINTEMP = 0
MAXTEMP = 70


class LM35:
	tv = [ [], [] ]			# Lists for Readings
	TIMER = 500				# Time interval between reads
	MINY = 0				# Temperature range
	MAXY = 100
	running = False
	ccs_current = 1.0		# .5 mA
	Rg = 2388.0				# 2.4k resistor
	setpoint = 50.0			
	upv = 2.0				# voltage applied to the base through 10 kOhm

	def v2t(self, v):			# Convert Voltage to Temperature for LM35
		gain = 1.0 + 10000./self.Rg
		temp = v/gain*100 
		return temp

	def xmgrace(self):
		if self.running == True:
			return
		p.grace([self.tv])

	def start(self):
		self.index = 0
		self.tv = [ [], [] ]
		try:
			self.MAXTIME = int(DURATION.get())
			self.Rg = float(RG.get())
			self.TIMER = int(TGAP.get())
			tmp = float(SETP.get())
			if MINTEMP < tmp < MAXTEMP:
				self.setpoint = tmp
			else:
				self.msg(_('temperature setpoint out of range'))
				return
			self.MINY = 0
			self.MAXY = self.setpoint + 10
			upv = float(UPV.get())
			if .7 < upv <= 5.0:
				self.upv = tmp
			else:
				self.msg(_('UPV setpoint out of range'))
				return
			g.setWorld(0, self.MINY, self.MAXTIME, self.MAXY,_('Time'),_('Volt'))
			SetP.config(state=DISABLED)
			Total.config(state=DISABLED)
			Dur.config(state=DISABLED)
			self.msg(_('Starting the Controller'))
			self.running = True
			p.write_outputs(1)
			root.after(self.TIMER, self.update)
		except:
			self.msg(_('Failed to Start'))

	def stop(self):
		self.running = False
		Total.config(state=NORMAL)
		Dur.config(state=NORMAL)
		SetP.config(state=NORMAL)
		p.set_upv(0)
		Tlab.config(bg='green')
		self.msg(_('User Stopped the measurements'))

	def update(self):
		if self.running == False:
			return
		t,v = p.get_voltage_time(2)  # Read A2
		if len(self.tv[0]) == 0:
			self.start_time = t
			elapsed = 0
		else:
			elapsed = t - self.start_time
		self.tv[0].append(elapsed)
		temp = self.v2t(v)
		if temp >= self.setpoint:
			p.set_upv(0)
			Tlab.config(bg='green')
		elif temp <= self.setpoint - 0.2:
			Tlab.config(bg='red')
			p.set_upv(self.upv)
		self.tv[1].append(temp)
		if len(self.tv[0]) >= 2:
			g.delete_lines()
			g.line(self.tv[0], self.tv[1])
		if elapsed > self.MAXTIME:
			self.running = False
			Total.config(state=NORMAL)
			Dur.config(state=NORMAL)
			SetP.config(state=NORMAL)
			self.msg(_('Completed the Measurements'))
			p.set_upv(0)
			Tlab.config(bg='green')
			return 
		root.after(self.TIMER, self.update)

	def save(self):
		try:
			fn = filename.get()
		except:
			fn = 'pt100.dat'
		p.save([self.tv],fn)
		self.msg(_('Data saved to %s') %fn)

	def clear(self):
		if self.running == True:
			return
		self.nt = [ [], [] ]
		g.delete_lines()
		self.msg(_('Cleared Data and Trace'))

	def msg(self,s, col = 'blue'):
		msgwin.config(text=s, fg=col)

p = eyes.open()
p.loadall_calib()
p.disable_actions()
p.set_upv(0)
root = Tk()
Canvas(root, width = WIDTH, height = 5).pack(side=TOP)  		# Some space at the top
g = eyeplot.graph(root, width=WIDTH, height=HEIGHT, bip=False)	# make plot objects using draw.disp
pt = LM35()

cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b3 = Label(cf, text = _('Rg='))
b3.pack(side = LEFT, anchor = SW)
RG = StringVar()
RG.set('2388')
Rg =Entry(cf, width=5, bg = 'white', textvariable = RG)
Rg.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('Ohm. '))
b3.pack(side = LEFT, anchor = SW)

b3 = Label(cf, text = _('UPV='))
b3.pack(side = LEFT, anchor = SW)
UPV = StringVar()
UPV.set('2.0')
Upv =Entry(cf, width=5, bg = 'white', textvariable = UPV)
Upv.pack(side = LEFT, anchor = SW)
b3 = Label(cf, text = _('V. '))
b3.pack(side = LEFT, anchor = SW)

b3 = Label(cf, text = _('Read Every'))
b3.pack(side = LEFT, anchor = SW)
TGAP = StringVar()
Dur =Entry(cf, width=5, bg = 'white', textvariable = TGAP)
TGAP.set('500')
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


cf = Frame(root, width = WIDTH, height = 10)
cf.pack(side=TOP,  fill = BOTH, expand = 1)
b3 = Label(cf, text = _('Set at'))
b3.pack(side = LEFT, anchor = SW)
SETP = StringVar()
SETP.set('50.0')
SetP =Entry(cf, width=6, bg = 'white', textvariable = SETP)
SetP.pack(side = LEFT, anchor = SW)
Tlab = Label(cf, text = _('deg C'))
Tlab.pack(side = LEFT, anchor = SW)

b1 = Button(cf, text = _('START'), command = pt.start)
b1.pack(side = LEFT, anchor = N)
b1 = Button(cf, text = _('STOP'), command = pt.stop)
b1.pack(side = LEFT, anchor = N)
b4 = Button(cf, text = _('CLEAR'), command = pt.clear)
b4.pack(side = LEFT, anchor = N)
b1 = Button(cf, text = _('Xmgrace'), command = pt.xmgrace)
b1.pack(side = LEFT, anchor = N)
b3 = Button(cf, text = _('SAVE to'), command = pt.save)
b3.pack(side = LEFT, anchor = N)
filename = StringVar()
e1 =Entry(cf, width=15, bg = 'white', textvariable = filename)
filename.set('tempcon.dat')
e1.pack(side = LEFT)
b5 = Button(cf, text = _('QUIT'), command = sys.exit)
b5.pack(side = RIGHT, anchor = N)


mf = Frame(root, width = WIDTH, height = 10)
mf.pack(side=TOP)
msgwin = Label(mf,text=_('Message'), fg = 'blue')
msgwin.pack(side=LEFT, anchor = S, fill=BOTH, expand=1)

eyeplot.pop_image('pics/temp-control.png', _('Temperature Controller (LM35)'))
root.title(_('Temperature controller using LM35'))
root.mainloop()
