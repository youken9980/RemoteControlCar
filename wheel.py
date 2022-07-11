#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class Wheel:

    FORWARD = "forward"
    BACKWARD = "backward"
    FREQUENCY = 50
    SPEED_MIN = 0
    SPEED_MAX = 100

    def __init__(self, en, in1, in2):
        self.go = {
            Wheel.FORWARD: self.forward,
            Wheel.BACKWARD: self.backward
        }
        self.en = en
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        self.pwmEn = GPIO.PWM(en, Wheel.FREQUENCY)
        self.pwmEn.start(0)

    def stop(self):
        self.pwmEn.stop()

    def reset(self):
        self.__changeStatus(0, GPIO.LOW, GPIO.LOW)

    def forward(self, speed):
        self.__changeStatus(speed, GPIO.HIGH, GPIO.LOW)

    def backward(self, speed):
        self.__changeStatus(speed, GPIO.LOW, GPIO.HIGH)

    def __changeStatus(self, speed, in1Status, in2Status):
        speed = int(speed)
        dc = Wheel.SPEED_MIN if speed < Wheel.SPEED_MIN else speed
        dc = Wheel.SPEED_MAX if speed > Wheel.SPEED_MAX else speed
        self.pwmEn.ChangeDutyCycle(dc)
        GPIO.output(self.in1, in1Status)
        GPIO.output(self.in2, in2Status)
