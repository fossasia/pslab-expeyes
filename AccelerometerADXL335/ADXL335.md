## Analog acceleration sensor module using ADXL335 - GY-61
GY-61 is a small, thin, low power, complete three-axis accelerometer voltage output through the signal conditioning at a minimum of full scale ± 3 g measurement range acceleration. It can measure the tilt-sensing applications in the static acceleration of gravity, and movement, shock or vibration due to dynamic acceleration. 


Data Sheet: https://www.sparkfun.com/datasheets/Components/SMD/adxl335.pdf


#### Accelerometer

Accelerometers measure acceleration. That is acceleration due to movement and also acceleration due to gravity. Accelerometers are often used to calculate a tilt angle. They can only do this reliably when they are static and not moving. To get an accurate angle of tilt they are often combined with one or more gyro's and the combination of data is used to calculate the angle.

Digital accelerometers will give you information using a serial protocol like I2C , SPI or USART, while analog accelerometers will output a voltage level within a predefined range that you have to convert to a digital value using an ADC (analog to digital converter) module.

####What does an accelerometer measure?

Accelerometers measure acceleration. For a static object that is the acceleration due to gravity (1g). Note also, that the output from accelerometers is not linear but is a sinewave, so you cannot take the direct output as a proportional representation of an angle of tilt based on gravity.

Normally an accelerometer's x and y output voltages will be half the supply voltage when measuring zero g (i.e. the device is perpendicular to gravity - horizontal). Tilt it one way and the voltage will increase, tilt it the other way and it will decrease. With a Triple axis accelerometer the z axis will be measuring 1g with the device horizontal. The output of an accelerometer is a sinewave of the acceleration measured. Accelerometers are more sensitive to small changes in tilt when they are perpendicular to gravity. I.e. when horizontal, small changes in tilt give useful readings. Past about 45 degrees of tilt they become increasingly less sensitive. For this reason it is common to use more than one axis value when determining the angle of tilt as will be seen below.

