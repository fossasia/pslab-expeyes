'''
These are procedures for measuring various parameters using ExpEYES Jr
'''


'''
From croplus.py
'''

def measurecap():
    msg(_('Starting Capacitance Measurement..'))
    cap = p.measure_cap()
    if cap == None:
        msg(_('Error: Capacitance too high or short to ground'),'red')
        return
    g.disp(_('IN1: %6.1f pF')%cap)
    if p.socket_cap == 30.0 and p.cap_calib == 1.0:
        msg(_('IN1 Not Calibrated.'))
    else:
        msg(_('IN1: %6.1f pF')%cap)
        
        
'''
from eyesj.py
'''

def measure_cv(self, ch, ctime, i = 5.5):  
        '''
        Using the CTMU of PIC, charges a capacitor connected to IN1, IN2 or SEN,
        for 'ctime' microseconds and then mesures the voltage across it.
        The value of current can be set to .55uA, 5.5 uA, 55uA or 550 uA
        @param ch channel number
        @param ctime duration in microseconds
        @param i value of the current (defaults to 5.5 uA)
        '''
        if i > 500:		# 550 uA
            irange = 0
        elif i > 50:	#55 uA
            irange = 3
        elif i > 5:		#5.5 uA,  default value
            irange = 2
        else:			# 0.55 uA
            irange = 1
            
        if ch not in [3,4]:
            self.msg = _('Current to be set only on IN1(3) or IN2(4)')
            print (_('Current to be set only on IN1 or IN2'))
            return
        self.sendByte(MEASURECV)
        self.sendByte(chr(ch))
        self.sendByte(chr(irange))
        self.sendInt(ctime)
        res = self.fd.read(1)
        if res != b'D':
            self.msg = warningWithResult(_('MEASURECV ERROR '), res)
            print (warningWithResult(_('MEASURECV ERROR '), res))
            return 
        res = self.fd.read(2)
        if sys.version_info.major == 3:
            iv = res[0] | (res[1] << 8)
        else:
            iv = ord(res[0]) | (ord(res[1]) << 8)
        v = self.m12[ch] * iv + self.c[ch]
        return v

def measure_cap_raw(self, ctmin = 10):
        '''
        Measures the capacitance connected between IN1 and GND. Stray
        capacitance should be subtracted from the measured
        value. Measurement is done by charging the capacitor with 5.5 uA
        for a given time interval. Any error in the value of current
        is corrected by calibrating.
        '''
        for ctime in range(ctmin, 1000, 10):
            v = self.measure_cv(3, ctime, 5.5)   # 5.5 uA range is chosen
            if v > 2.0: break
            if (v > 4) or (v == 0):
                self.msg = _('Error measuring capacitance %5.3f') %v
                print (_('Error measuring capacitance'), v)
                return None
        return 5.5 * ctime / v    # returns value in pF 

def measure_cap(self, ctmin = 10):
        '''
        Measures the capacitance connected between IN1 and GND.
        Returns the value after applying corrections.
        '''
        cap = self.measure_cap_raw()
        if cap != None:
            return (cap - self.socket_cap) * self.cap_calib
        else:
            return None
 
