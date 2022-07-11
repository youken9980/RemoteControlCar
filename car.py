#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from wheel import Wheel

class Car:

    GO_FORWARD = "goForward"
    TURN_LEFT_FORWARD = "turnLeftForward"
    TURN_RIGHT_FORWARD = "turnRightForward"
    GO_BACKWARD = "goBackward"
    TURN_LEFT_BACKWARD = "turnLeftBackward"
    TURN_RIGHT_BACKWARD = "turnRightBackward"
    TURN_RATIO_MIN = 0
    TURN_RATIO_MAX = 1
    TURN_RATIO_DEFAULT = 0.25

    def __init__(self, enA, inA1, inA2, enB, inB1, inB2, turnRatio):
        self.go = {
            Car.GO_FORWARD: self.goForward,
            Car.TURN_LEFT_FORWARD: self.turnLeftForward,
            Car.TURN_RIGHT_FORWARD: self.turnRightForward,
            Car.GO_BACKWARD: self.goBackward,
            Car.TURN_LEFT_BACKWARD: self.turnLeftBackward,
            Car.TURN_RIGHT_BACKWARD: self.turnRightBackward
        }
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.leftWheel = Wheel(enA, inA1, inA2)
        self.rightWheel = Wheel(enB, inB1, inB2)
        self.turnRatio = turnRatio if turnRatio >= Car.TURN_RATIO_MIN else Car.TURN_RATIO_DEFAULT
        self.turnRatio = turnRatio if turnRatio < Car.TURN_RATIO_MAX else Car.TURN_RATIO_DEFAULT

    def cleanup(self):
        print("clearup.")
        self.leftWheel.stop()
        self.rightWheel.stop()
        GPIO.cleanup()

    def allReset(self):
        self.leftWheel.reset()
        self.rightWheel.reset()

    def goForward(self, speed):
        self.go(Car.GO_FORWARD, Wheel.FORWARD, speed, speed)

    def turnLeftForward(self, speed):
        ratioSpeed = float(speed) * self.turnRatio
        self.go(Car.TURN_LEFT_FORWARD, Wheel.FORWARD, ratioSpeed, speed)

    def turnRightForward(self, speed):
        ratioSpeed = float(speed) * self.turnRatio
        self.go(Car.TURN_RIGHT_FORWARD, Wheel.FORWARD, speed, ratioSpeed)

    def goBackward(self, speed):
        self.go(Car.GO_BACKWARD, Wheel.BACKWARD, speed, speed)

    def turnLeftBackward(self, speed):
        ratioSpeed = float(speed) * self.turnRatio
        self.go(Car.TURN_LEFT_BACKWARD, Wheel.BACKWARD, ratioSpeed, speed)

    def turnRightBackward(self, speed):
        ratioSpeed = float(speed) * self.turnRatio
        self.go(Car.TURN_RIGHT_BACKWARD, Wheel.BACKWARD, speed, ratioSpeed)

    def go(self, carDirection, wheelDirection, leftSpeed, rightSpeed):
        print(carDirection, ", leftSpeed: ", leftSpeed, ", rightSpeed: ", rightSpeed)
        self.leftWheel.go[wheelDirection](leftSpeed)
        self.rightWheel.go[wheelDirection](rightSpeed)
