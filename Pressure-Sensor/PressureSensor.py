
import pylab
import expeyes.eyesj
p=expeyes.eyesj.open()
print p.set_voltage(5.0) 
print p.get_voltage(1)   
t,v = p.capture(1,300,100)
plot(t,v)
show()
