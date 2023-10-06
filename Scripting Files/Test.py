#from lx16a import *
from pylx16a.lx16a import *
from math import sin, cos
import time
# This is the port that the controller board is connected to
# # This will be different for different computers Raspbian
# # On Windows, try the ports COM1, COM2, COM3, etc...
# # On , try each port in /dev/


def calcStep1(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo1.move(curr+step)
        curr = servo1.get_physical_angle()
        time.sleep(0.05)

def calcStep2(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo2.move(curr+step)
        curr = servo2.get_physical_angle()
        time.sleep(0.05)

def calcStep3(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo3.move(curr+step)
        curr = servo3.get_physical_angle()
        time.sleep(0.05)

def calcHips(curr1, goal1, curr2, goal2, ts):
    step1 = (goal1 - curr1) / ts
    step2 = (goal2 - curr2) / ts
    for i in range(0, ts):
        servo2.move(curr1 + step1)
        curr1 = servo2.get_physical_angle()
        servo3.move(curr2 + step2)
        curr2 = servo3.get_physical_angle()
        time.sleep(0.05)

def calcStep4(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo4.move(curr+step)
        curr = servo4.get_physical_angle()
        time.sleep(0.05)

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

home1 = 132.48
home2 = 138.0
home3 = 141.84
home4 = 154.08

# 161.28
# 138.48
# 141.84
# 154.8

servo1.move(home1)
servo2.move(home2)
servo3.move(home3)
servo4.move(home4)
time.sleep(2)
# servo1.move(161)
# while True:
    # calcHips(servo2.get_physical_angle(), 187, servo3.get_physical_angle(), 87, 10)
    # calcStep4(servo4.get_physical_angle(), 130, 10)
    # calcHips(servo2.get_physical_angle(), home1, servo3.get_physical_angle(), home2, 10)
    # calcStep4(servo4.get_physical_angle(), home4, 10)


# calcStep1(servo1.get_physical_angle(), 180, 10)
# calcStep2(servo2.get_physical_angle(), 50, 10)
# calcStep3(servo3.get_physical_angle(), 50, 10)
# calcStep4(servo4.get_physical_angle(), 151, 10)
# calcStep2(servo2.get_physical_angle(), 187, 10)
# calcStep3(servo3.get_physical_angle(), 215, 10)
#
# calcStep4(servo4.get_physical_angle(), 100, 10)

# calcStep2(servo2.get_physical_angle(), 114, 5)

# calcHips(servo2.get_physical_angle(), 187, servo3.get_physical_angle(), 215, 10)
# calcStep3(servo3.get_physical_angle(), 96, 5)
# calcStep2(servo2.get_physical_angle(), 99, 5)
# calcStep4(servo4.get_physical_angle(), 135, 3)

# calcStep1(servo1.get_physical_angle(), home1, 3)
# calcStep2(servo2.get_physical_angle(), home2, 3)

servo1.set_angle_limits(home1-60, home1+60)
servo2.set_angle_limits(home2-60, home2+60)
servo3.set_angle_limits(home3-60, home3+60)
servo4.set_angle_limits(home4-60, home4+60)

t = 0
# while True:
#     # Two sine waves out of phase
#     servo1.move(home1+sin(t)*20)
#     servo2.move(home2+sin(t)*20)
#     servo3.move(home3+sin(t)*20)
#     servo4.move(home4+sin(t)*20)

    # time.sleep(0.05)
    # t += 0.05


while False:
    servo1.move(120)
    servo4.move(120)
    time.sleep(0.5)

    servo2.move(120)
    servo3.move(120)
    time.sleep(0.5)

    servo1.move(home1)
    servo4.move(home2)
    time.sleep(0.5)

    servo2.move(home3)
    servo3.move(home4)
    time.sleep(0.5)


