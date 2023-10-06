# from lx16a import *
from pylx16a.lx16a import *
from math import sin, cos
import time

port = 'COM5'
LX16A.initialize(port)
# LX16A.initialize("/dev/ttyUSB0", 0.1)

# There should four servos connected, with IDs 1, 2, 3, 4
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

gts = 0.05


def calcStep1(curr, goal, ts):
    step = (goal - curr) / ts
    for i in range(0, ts):
        servo1.move(curr + step)
        curr = servo1.get_physical_angle()
        time.sleep(gts)


def calcStep2(curr, goal, ts):
    step = (goal - curr) / ts
    for i in range(0, ts):
        servo2.move(curr + step)
        curr = servo2.get_physical_angle()
        time.sleep(gts)


def calcStep3(curr, goal, ts):
    step = (goal - curr) / ts
    for i in range(0, ts):
        servo3.move(curr + step)
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
    step = (goal - curr) / ts
    for i in range(0, ts):
        servo4.move(curr + step)
        curr = servo4.get_physical_angle()
        time.sleep(gts)


time.sleep(2)

try:
    x1 = servo1.get_physical_angle()
    x2 = servo2.get_physical_angle()
    x3 = servo3.get_physical_angle()
    x4 = servo4.get_physical_angle()
except ServoTimeoutError:
    print('Servo is not responding. Exiting.')
    exit()

t = 15
calcStep1(servo1.get_physical_angle(), home1, t)
calcStep2(servo2.get_physical_angle(), home2, t)
calcStep3(servo3.get_physical_angle(), home3, t)
calcStep4(servo4.get_physical_angle(), home4, t)

import pylx16a
import time

servo1 = LX16A(1)
servo2 = LX16A(2)
servo3 = LX16A(3)
servo4 = LX16A(4)


def healthCheck():
    # query servo positions
    try:
        x1 = servo1.get_physical_angle()
        x2 = servo2.get_physical_angle()
        x3 = servo3.get_physical_angle()
        x4 = servo4.get_physical_angle()
    except ServoTimeoutError:
        print('Servo is not responding. Exiting.')
        exit()

    # query voltage inputs to each servo
    v1 = servo1.get_vin()
    v2 = servo1.get_vin()
    v3 = servo1.get_vin()
    v4 = servo1.get_vin()
    print(v1, v2, v3, v4)

    # flash servo LEDs 3 times to confirm health check complete
    for i in range(3):
        servo1.led_power_on()
        time.sleep(0.1)
        servo1.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo2.led_power_on()
        time.sleep(0.1)
        servo2.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo3.led_power_on()
        time.sleep(0.1)
        servo3.led_power_off()
        time.sleep(0.1)

    for i in range(3):
        servo4.led_power_on()
        time.sleep(0.1)
        servo4.led_power_off()
        time.sleep(0.1)
