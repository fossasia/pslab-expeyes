'''
Connect pickup coil to A1 and Fit the sine wave for getting frequency.
From frequency of rotation of anemometer wind speed can be calculated
'''

import expeyes.eyemath as em
p = expeyes.eyesj.open()
t,v= p.capture(1,400,100)
vfit, par = em.fit_sine(t,v)
print par[1] # second parameter is frequency
print(t,v)
plot(t, vfit)
show()
plot(ta,da)
show()
