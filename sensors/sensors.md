### List of Sensor Plug-ins

####1. Accelerometer 
Sensor Used:    ADXL 335 - Three axis
####2. Magnetic Field Sensor
Sensors Used:   KY 003, 3144 Hall Effect Sensor
####3. Infra-red Object Sensor
Sensor Used:    Locally Made using IC LM-358N
####4. Ultrasonic Position Sensor
Sensor Used:    SRF-05 HY, SRF-04
####5. Temperature Sensor
Sensor Used:    PT-100 and LM-35
####6. Humidity Sensor
Sensor Used:    DHT-11, HS-1101
####7. Pressure- Barometric 
Sensor Used:    BMP180 Digital sensor
####8. Pressure
Sensor Used:    Pizzo Electric sensor
####9. Gas Sensors
Sensor Used:    MQ-4 for Methane
                MQ-6 for LPG
                MQ-7 for Carbon Monoxide
####10. Colour Sensor ( in progress)
Sensor Used:    IC-TCS3200D-SOP8
####11. Anemometer- Wind Speed
Sensor Used:    Home-made 
####12. Wind Direction
Sensor Used:    Home-made
####13. Rotatory Motion Sensor
Sensor Used:    DC Motor and a pick-up coil
####14. Motion Sensor-Photo Gate
Sensor Used:    Photo Gate using Photo Diode
####15. Other devices used as sensors
                Solar Cells
                Induction coil
                condensor mic
                ATTINY-85 MCU used for sine wave generation
                Raspberry Pi 2 Model B for stand-alone weather station



Details of sensor modules
(To be updated...)

####Accelerometer Sensor :  ADXL-335

An accelerometer is a device that measures proper acceleration ("g-force"). Proper acceleration is not the same as coordinate acceleration (rate of change of velocity). For example, an accelerometer at rest on the surface of the Earth will measure an acceleration g= 9.81 m/s2 straight upwards. By contrast, accelerometers in free fall orbiting and accelerating due to the gravity of Earth will measure zero.

**ADXL 335-GY-61** is a small, thin, low power, complete three-axis accelerometer voltage output through the signal conditioning at a minimum of full scale ± 3 g measurement range acceleration. It can measure the  acceleration of gravity,and movement, shock or vibration due to dynamic acceleration.


####Relative Humidity Sensor : HS-1101

Relative humidity is an important metric used in weather forecasts and reports, as it is an indicator of the likelihood of precipitation, dew, or fog. In hot summer weather, a rise in relative humidity increases the apparent temperature to humans (and other animals) by hindering the evaporation of perspiration from the skin. Ref: wikipedia.org


**HS1101 sensor** consists of a capacitor which varies with relative humidity and is used in a 555 circuit to generate a pulse train of frequency related to relative humidity. The number of pulses over a one second period are counted and the RH is then calculated.

Based on a unique capacitive cell, this relative humidity sensor is designed for high volume, cost sensitive applications such as office automation, automotive cabin air control, home appliances, and industrial process control systems. They are also useful in all applications where humidity compensation is needed.

####Temeprature Sensors : LM-35 and PT-100

Platinum resistance thermometers (PRTs) offer excellent accuracy over a wide temperature range (from –200 to +850 °C). Standard sensors are are available from many manufacturers with various accuracy specifications and numerous packaging options to suit most applications. Unlike thermocouples, it is not necessary to use special cables to connect to the sensor. 

For **LM-35**  temperature sensor the output voltage is linearly proportional to the Celsius (Centigrade) temperature. LM35 does not require any external calibration or trimming to provide typical accuracies of ±1⁄4̊ C  at room temperature and ±3⁄4̊C over a full −55 to +150 ̊C temperature range.  Another temperature sensor PT100 is previously  tested with ExpEYES.  It offers excellent accuracy over a wide temperature range (from –200 to +850 °C). 

The LM35 series are precision integrated-circuit temperature sensors, whose output voltage is linearly proportional to the Celsius (Centigrade) temperature. The LM35 thus has an advantage over linear temperature sensors calibrated in ̊ Kelvin, as the user is not required to subtract a large constant voltage from its output to obtain convenient Centi- grade scaling. 

####Hall Magnetic Sensor : Hall Sensor -3144 and Module KY-003

Exploring  the use of this magnetic sensor for measuring rotational speed of anemometer and other measurements was quiet interesting experience.  Tried Hall sensor 3144 and KY-003 module.

The KY-003 is a magnetic switch. If no magnetic field is present, the signal line of the sensor is HIGH (3.5 V). If a magnetic field is presented to the sensor, the signal line goes LOW, at the same time the LED on the sensor lights up. The polarity of the magnetic field is of influence to the switching action. The front side of the sensor needs the opposite polarity as the back of the sensor to switch on.


####Gas Sensors

**Methane Gas Sensor MQ-4** This semiconductor gas sensor detects the presence of methane (CNG) gas at concentrations from 300 ppm to 10,000 ppm, a range suitable for detecting gas leaks. 

**LPG Gas Sensor MQ-6** This sensor detects the presence of LPG, isobutane, and propane at concentrations from 300 to 10,000 ppm. 

**Carbon Monoxide** Gas Sensor MQ-7 This gas sensor detects the presence of Carbon Monoxide at concentrations from 10 to 10,000 ppm.


####Piezielectric Transducer

A piezoelectric sensor is a device that uses the piezoelectric effect, to measure changes in pressure, acceleration, temperature, strain, or force by converting them to an electrical charge. The prefix piezo- is Greek for 'press' or 'squeeze'.

Cheap piezoceramic membrane used in piezoelectric ‘buzzers’ can be used as a very inexpensive, accurate and sensitive pressure sensor. These devices can be used both as sensors and actuators, so they’re referred to as transducers, a term applied to any device that can convert one form of energy to another. The sensor turns mechanical energy into electric potential, and the actuator converts electrical energy into mechanical force or motion.

### Barometric Pressure Sensor BMP 180

BMP-180Tested BMP180 Digital Barometric Pressure Sensor Board Module :This precision sensor from Bosch is the best low-cost sensing solution for measuring barometric pressure and temperature.  
