from Tkinter import *
import expeyes.eyesj, time, sys

p=expeyes.eyesj.open()
if p == None: sys.exit()
p.set_state(10,1)

TIMER = 100
WIDTH = 200
HEIGHT = 500
X = WIDTH/2
vs = 0.034000

def action():
	global pos, txt,strt
	t = p.srfechotime(9,0)
	if t > 10000: 
		p.set_sqr1(-1)
		w.after(20,action)
		return
	s = (t-400) *vs/2
	ss = 'Reflector at %5.1f cm'%s
	print time.time()-strt, s
	y = HEIGHT - s*10
	c.delete(pos)
	c.delete(txt)
	pos = c.create_rectangle([X,y,X+20, y + 5], outline='red')
	txt = c.create_text(X,20,text=ss)
	p.set_sqr1(t)
	w.after(TIMER,action)

w = Tk()
c = Canvas(w, width=WIDTH, height=HEIGHT)
c.pack()
pos = c.create_rectangle([X,0,X+20, 5], outline='red')
txt = c.create_text(X,50,text='')
w.after(0,action)
strt = time.time()
w.mainloop()
