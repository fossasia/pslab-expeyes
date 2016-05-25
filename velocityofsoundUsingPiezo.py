'''
ExpEYES Program
GSoC- 2016
Author: Praveen Patil
License : GPL
'''



import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext


from Tkinter import *
import expeyes.eyes as eyes, expeyes.eyeplot as eyeplot


def get_tof():
	t = p.pulse2rtime(1,2)
	if t > 0:
		res.config(text = _('%8.6f sec')%(t*1.0e-6))
	else:
		res.config(text = _('Error..'))

p = eyes.open()
p.disable_actions()

root = Tk()
cf = Frame(root)
cf.pack(side=TOP,  fill = BOTH, expand = 1)

Label(cf,text = _('Connect Transmitter from OD1 to Ground')).pack()
Label(cf,text = _('Connect Receiver from T15 to Ground')).pack()
Label(cf,text = _('Keep them facing each other, at a known distance')).pack()

b1 = Button(cf, text = _('Measure Time of Travel'), command = get_tof)
b1.pack(side = TOP, anchor = N)
res = Label(cf, text = '')
res.pack(side = TOP, anchor = N)
b5 = Button(cf, text = _('QUIT'), command = sys.exit)
b5.pack(side = TOP, anchor = N)

eyeplot.pop_image('pics/xxxxx.png', _('Velocity of Sound, 40kHz'))
root.title(_('Velocity of Sound'))
root.mainloop()

