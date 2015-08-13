'''
Program to control PVS programable voltage source in ExpEYES
Useful in voltametry and other applications where voltage needs to be changed
'''




import sys

if sys.version_info.major==3:
        from tkinter import *
else:
        from Tkinter import *

sys.path=[".."] + sys.path
import expeyes.eyesj, expeyes.eyeplot as eyeplot

p=expeyes.eyesj.open()

import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

def set_pvs(w):
	state = int(Pvs.get())
	iv = int(Pvs.get())
	p.write_dac(iv)
	v = p.get_voltage(12)
	Res.config(text=_('PVS = %5.3f volts')%v)
w = Tk()
Label(text=_('To change PVS drag the slider. For fine adjustment, click on its left or right')).pack(side=TOP)
Pvs = Scale(w,command = set_pvs, orient=HORIZONTAL, length=500, showvalue=False, from_ = 0, to=4095, resolution=1)
Pvs.pack(side=TOP)
Res = Label(text = '', fg = 'blue')
Res.pack(side=TOP)
Button(text=_('QUIT'), command=sys.exit).pack(side=TOP)
w.title(_('EYES Junior: Adjust PVS'))
w.mainloop()

