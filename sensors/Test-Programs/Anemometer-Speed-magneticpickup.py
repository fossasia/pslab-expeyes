from __future__ import print_function

'''
Connect pickup coil to A1 and Fit the sine wave for getting frequency.
From frequency of rotation of anemometer wind speed can be calculated
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext

import expeyes.eyesj as ej
import expeyes.eyemath as em
from pylab import plot, show

p = ej.open()
t,v= p.capture(1,400,100)
try:
    vfit, par = em.fit_sine(t,v)
    print (par[1]) # second parameter is frequency
    print((t,v))
    plot(t, vfit)
    show()
except:
    print("No alternative signal, please make another try.")

