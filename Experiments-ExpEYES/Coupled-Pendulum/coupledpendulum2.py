'''
GSoC ExpEYES program
License : GNU GPL version 3
Program to study oscillations of coupled pendulum. Store readings and then plot.
connect motor of pendulum1 to IN and GND, OUT to A1
Connect motor of pendulum2 to IN and GND of another ExpEYES box. Connect OUT to Channel A2 of the first ExpEYES box.
Note: Second ExpEYES box must be connected and detected by CROPLUS program, then run coupledpendula.py so that first ExpEYES box will be detected.
This experiment can be done in three different ways
1. both the pendula oscillating in-phase
2. Both the pendula oscillating out-of-phase
3. One pendulum at rest while other is set in to oscillations.
'''
import gettext
gettext.bindtextdomain("expeyes")
gettext.textdomain('expeyes')
_ = gettext.gettext
from pylab import *
import expeyes.eyesj, time
p = expeyes.eyesj.open()
DURATION = 15
ta = []
tb = []
va = []
vb = []
f = open('pend_wave.dat','w')
start = p.get_voltage_time(1)[0]
start2 = p.get_voltage_time(2)[0]
while 1:
res = p.get_voltage_time(1)
tm = res[0] - start # elapsed time
ta.append(tm)
va.append(res[1])
res2 = p.get_voltage_time(2)
tm2 = res2[0] - start # elapsed time
tb.append(tm2)
vb.append(res2[1])
ss = '%6.3f %6.3f %6.3f %6.3f'%(tm,res[1],tm2,res2[1])
print ss
f.write(ss+'\n')
if tm > DURATION:
break
subplot(3,1,1)
plot(ta,va,'r') #position Plot
title('Pendulum - 1')
xlabel('Time')
ylabel('Displacement')
subplot(3,1,2)
plot(tb,vb, 'b')
title('Pendulum - 2')
xlabel('Time')
ylabel('Displacement')
subplot(3,1,3)
plot(ta,va,'r', tb,vb, 'b')
title('Coupled Pendula')
xlabel('Time')
ylabel('Displacement')
plt.tight_layout() #this function from matplotlib provides spacing between subgraphs
show()
'''
# This code can be used to have plots in separate figures
figure(1)
plot(ta,va)
figure(2)
plot(tb,vb)
figure(3)
plot(ta,va, tb,vb)
show()
'''
