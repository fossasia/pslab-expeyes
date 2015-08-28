###Distinguishing Acceleration from Gravity

ADXL335 sensor sense both dynamic acceleration due to movement and static acceleration due to gravity. The sensor returns a vector
that can be written as:
a_sensor=a_dynamic+a_gravity.

When the accelerometer is at rest,
a_dynamic=0. 

In this case the angle of a_gravity, which will always have a magnitude of 1g, can be used to calculate the orientation or tilt of the sensor.


When the accelerometer is moving at a non-constant velocity,
a_dynamic will be added to the sensor reading. If the orientation of the accelerometer is known and fixed, then
a_gravity can be calculated (or measured when the sensor is  at rest) and subtracted from
a_sensor to isolate a_dynamic.


