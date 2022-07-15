#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wheel import Wheel

wheel_left_front_enb = 18
wheel_left_front_in3 = 23
wheel_left_front_in4 = 24

wheel_left_rear_ena = 13
wheel_left_rear_in1 = 17
wheel_left_rear_in2 = 27

wheel_right_front_ena = 12
wheel_right_front_in1 = 5
wheel_right_front_in2 = 6

wheel_right_rear_enb = 19
wheel_right_rear_in4 = 20
wheel_right_rear_in3 = 21


class Car:
    GO_FORWARD = "goForward"
    GO_BACKWARD = "goBackward"
    TURN_RATIO_MIN = 0
    TURN_RATIO_MAX = 1
    TURN_RATIO_DEFAULT = 0.25

    def __init__(self):
        self.go = {
            Car.GO_FORWARD: self.go_forward,
            Car.GO_BACKWARD: self.go_backward,
        }
        self.wheel_left_front = Wheel(wheel_left_front_enb, wheel_left_front_in3, wheel_left_front_in4)
        self.wheel_left_rear = Wheel(wheel_left_rear_ena, wheel_left_rear_in1, wheel_left_rear_in2)
        self.wheel_right_front = Wheel(wheel_right_front_ena, wheel_right_front_in1, wheel_right_front_in2)
        self.wheel_right_rear = Wheel(wheel_right_rear_enb, wheel_right_rear_in4, wheel_right_rear_in3)

    def cleanup(self):
        print("car cleanup.")
        self.wheel_left_front.cleanup()
        self.wheel_left_rear.cleanup()
        self.wheel_right_front.cleanup()
        self.wheel_right_rear.cleanup()

    def all_suspend(self):
        self.wheel_left_front.suspend()
        self.wheel_left_rear.suspend()
        self.wheel_right_front.suspend()
        self.wheel_right_rear.suspend()

    def go_forward(self, speed):
        car_direction = Car.GO_FORWARD
        wheel_left_front_direction = Wheel.FORWARD
        wheel_left_rear_direction = Wheel.FORWARD
        wheel_right_front_direction = Wheel.FORWARD
        wheel_right_rear_direction = Wheel.FORWARD
        left_speed = speed
        right_speed = speed
        self.__go(car_direction, wheel_left_front_direction, wheel_left_rear_direction, wheel_right_front_direction, wheel_right_rear_direction, left_speed, right_speed)

    def go_backward(self, speed):
        car_direction = Car.GO_BACKWARD
        wheel_left_front_direction = Wheel.BACKWARD
        wheel_left_rear_direction = Wheel.BACKWARD
        wheel_right_front_direction = Wheel.BACKWARD
        wheel_right_rear_direction = Wheel.BACKWARD
        left_speed = speed
        right_speed = speed
        self.__go(car_direction, wheel_left_front_direction, wheel_left_rear_direction, wheel_right_front_direction, wheel_right_rear_direction, left_speed, right_speed)

    def __go(self, car_direction, wheel_left_front_direction, wheel_left_rear_direction, wheel_right_front_direction, wheel_right_rear_direction, left_speed, right_speed):
        print(car_direction, ", left_speed: ", left_speed, ", right_speed: ", right_speed)
        self.wheel_left_front.go[wheel_left_front_direction](left_speed)
        self.wheel_left_rear.go[wheel_left_rear_direction](left_speed)
        self.wheel_right_front.go[wheel_right_front_direction](right_speed)
        self.wheel_right_rear.go[wheel_right_rear_direction](right_speed)
