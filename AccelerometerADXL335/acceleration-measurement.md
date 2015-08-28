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


Unfortunately, this is rarely the case. There is a heuristic technique that may be useful for estimating
a_dynamic in cases where the orientation of the accelerometer is unknown and movement is sporadic.
The magnitude of
a_sensor is calculated as

a_sensor= sqrt [(a_sensorX)^2 + (a_sensorY)^2 + (a_sensorZ)^2]



If the magnitude of
a_sensor is very close to 1g for prolonged periods of time, it is likely that a_dynamic is zero during these “rest times”
(though they may also correspond to periods of movement at a constant velocity). 

If we assume that a_sensor is equal to a_gravity during these periods, then the orientation of the sensor may be updated to a new value. This 
estimate of a_gravity is then subtracted from all accelerometer readings until the next “rest time” where it can be
reassessed.


