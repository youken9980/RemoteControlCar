#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from car import Car

ENA = 40
IN1 = 38
IN2 = 36
IN3 = 37
IN4 = 35
ENB = 33
mycar = Car(ENA, IN3, IN4, ENB, IN1, IN2, 0)

try:
    speed = 100
    interval = 1.5
    mycar.goForward(speed)
    time.sleep(interval)
    mycar.allReset()
    time.sleep(interval)
    mycar.turnLeftForward(speed)
    time.sleep(interval)
    mycar.allReset()
    time.sleep(interval)
    mycar.turnRightForward(speed)
    time.sleep(interval)
    mycar.allReset()
    time.sleep(interval)
    mycar.goBackward(speed)
    time.sleep(interval)
    mycar.allReset()
    time.sleep(interval)
    mycar.turnLeftBackward(speed)
    time.sleep(interval)
    mycar.allReset()
    time.sleep(interval)
    mycar.turnRightBackward(speed)
    time.sleep(interval)
    mycar.allReset()
except KeyboardInterrupt:
    pass
finally:
    mycar.cleanup()
