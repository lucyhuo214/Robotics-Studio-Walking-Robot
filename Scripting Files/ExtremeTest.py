#from lx16a import *
from pylx16a.lx16a import *
from math import sin, cos
import time
# This is the port that the controller board is connected to
# # This will be different for different computers Raspbian
# # On Windows, try the ports COM1, COM2, COM3, etc...
# # On , try each port in /dev/

port = 'COM5'
LX16A.initialize(port)

# There should two servos connected, with IDs 1 and 2
try:
    servo1 = LX16A(1)
    servo2 = LX16A(2)
    servo3 = LX16A(3)
    servo4 = LX16A(4)
except ServoTimeoutError:
    print('Servo is not responding. Exiting.')
    exit()

print(servo1.get_physical_angle())
print(servo2.get_physical_angle())
print(servo3.get_physical_angle())
print(servo4.get_physical_angle())




