#from lx16a import *
from pylx16a.lx16a import *
from math import sin, cos
import time

port = 'COM5'
LX16A.initialize(port)
# LX16A.initialize("/dev/ttyUSB0", 0.1)

# There should be four servos connected, with IDs 1, 2, 3, 4
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

servo1.move(home1)
servo2.move(home2)
servo3.move(home3)
servo4.move(home4)

# servo1.set_angle_limits(home1-60, home1+60)
# servo2.set_angle_limits(home2-60, home2+60)
# servo3.set_angle_limits(home3-60, home3+60)
# servo4.set_angle_limits(home4-60, home4+60)

servo1.set_angle_limits(0, 240)
servo2.set_angle_limits(0, 240)
servo3.set_angle_limits(0, 240)
servo4.set_angle_limits(0, 240)

gts = 0.05



def calcStep1(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo1.move(curr+step)
        curr = servo1.get_physical_angle()
        time.sleep(gts)

def calcStep2(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo2.move(curr+step)
        curr = servo2.get_physical_angle()
        time.sleep(gts)

def calcStep3(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo3.move(curr+step)
        curr = servo3.get_physical_angle()
        time.sleep(gts)

def calcHips(curr1, goal1, curr2, goal2, ts):
    step1 = (goal1 - curr1) / ts
    step2 = (goal2 - curr2) / ts
    for i in range(0, ts):
        servo2.move(curr1 + step1)
        curr1 = servo2.get_physical_angle()
        servo3.move(curr2 + step2)
        curr2 = servo3.get_physical_angle()
        time.sleep(gts)

def calcStep4(curr, goal, ts):
    step = (goal-curr)/ts
    for i in range(0,ts):
        servo4.move(curr+step)
        curr = servo4.get_physical_angle()
        time.sleep(gts)


time.sleep(2)

t = 10

while True:
    calcStep1(servo1.get_physical_angle(), 220, t)
    calcStep1(servo1.get_physical_angle(), 100, t)
    calcStep1(servo1.get_physical_angle(), 220, t)
    calcStep1(servo1.get_physical_angle(), 100, t)
    calcStep1(servo1.get_physical_angle(), 220, t)
    calcStep1(servo1.get_physical_angle(), 100, t)

    calcStep4(servo4.get_physical_angle(), 80, t)
    calcStep4(servo4.get_physical_angle(), 170, t)
    calcStep4(servo4.get_physical_angle(), 80, t)
    calcStep4(servo4.get_physical_angle(), 170, t)
    calcStep4(servo4.get_physical_angle(), 80, t)
    calcStep4(servo4.get_physical_angle(), 170, t)

    calcStep1(servo1.get_physical_angle(), 230, t)
    calcStep4(servo4.get_physical_angle(), 100, t)
    calcStep4(servo4.get_physical_angle(), 170, t)  # NOTE: changed from 190, 90
    calcStep1(servo1.get_physical_angle(), 110, t)
    calcStep1(servo1.get_physical_angle(), 220, t)
    calcStep1(servo1.get_physical_angle(), 100, t)

    calcHips(servo2.get_physical_angle(), 30, servo3.get_physical_angle(), 30, t)
    calcHips(servo2.get_physical_angle(), 220, servo3.get_physical_angle(), 220, t)
    calcHips(servo2.get_physical_angle(), 30, servo3.get_physical_angle(), 30, t)
    calcHips(servo2.get_physical_angle(), 220, servo3.get_physical_angle(), 220, t)
    calcHips(servo2.get_physical_angle(), 30, servo3.get_physical_angle(), 30, t)
    calcHips(servo2.get_physical_angle(), 220, servo3.get_physical_angle(), 220, t)

    servo1.move(home1)
    servo2.move(home2)
    servo3.move(home3)
    servo4.move(home4)

    time.sleep(0.5)