
##DHT11 Temperature Humidity Sensor Module 
 
 
This sensor module includes resistive humidity sensing component and NTC temperature testing. 
 
Specification:

    Signal transmission range: 20m
    Humidity measuring range: 20 - 95% RH
    Humidity measurement error: + / -5%
    Temperature measurement range: 0 - 50°C
    Temperature measurement error: + / -2°C
    Operating voltage: 3.3 - 5V

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed). Its fairly simple to use, but requires careful timing to grab data. The only real downside of this sensor is you can only get new data from it once every 2 seconds.  

The DHT11 is chosen because it is lab calibrated, accurate and stable and its signal output is digital. Most important of all, it is relatively inexpensive for the given performance. Below is the pinout of the sensor. 
Datasheet

 
 Pin       	Name     	Description
 1 	 VDD 	 Power supply 3 - 5.5 V DC
 2 	 DATA 	 Serial data output
 3 	 NC 	 Not connected
 4 	 GND 	 Ground

Wiring:

Connect the sensor to the Arduino as shown below
 DHT11 	 Arduino
 Pin 1 	 Vcc
 Pin 2 	 Analog0
 Pin 4 	 Gnd
