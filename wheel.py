#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class Wheel:
    SUSPEND = "suspend"
    FORWARD = "forward"
    BACKWARD = "backward"
    BRAKE = "brake"
    FREQUENCY = 100
    SPEED_MIN = 0
    SPEED_MAX = 100

    def __init__(self, en, in1, in2):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.go = {
            Wheel.SUSPEND: self.suspend,
            Wheel.FORWARD: self.forward,
            Wheel.BACKWARD: self.backward,
            Wheel.BRAKE: self.brake,
        }
        self.en = en
        self.in1 = in1
        self.in2 = in2
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        self.pwm_en = GPIO.PWM(en, Wheel.FREQUENCY)
        self.pwm_en.start(0)

    def cleanup(self):
        print("wheel cleanup.")
        self.pwm_en.stop()
        GPIO.cleanup()

    def suspend(self):
        self.__change_status(0, GPIO.LOW, GPIO.LOW)

    def forward(self, speed):
        self.__change_status(speed, GPIO.HIGH, GPIO.LOW)

    def backward(self, speed):
        self.__change_status(speed, GPIO.LOW, GPIO.HIGH)

    def brake(self):
        self.__change_status(0, GPIO.HIGH, GPIO.HIGH)

    def __change_status(self, speed, in1_status, in2_status):
        print("speed", speed, ", in1_status: ", in1_status, ", in2_status: ", in2_status)
        dc = float(speed)
        dc = Wheel.SPEED_MIN if dc < Wheel.SPEED_MIN else dc
        dc = Wheel.SPEED_MAX if dc > Wheel.SPEED_MAX else dc
        self.pwm_en.ChangeDutyCycle(dc)
        GPIO.output(self.in1, in1_status)
        GPIO.output(self.in2, in2_status)
