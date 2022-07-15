#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from car import Car

my_car = Car()

try:
    speed = 100

    my_car.go_forward(speed)
    time.sleep(5)
    my_car.all_suspend()
    time.sleep(1.5)

    my_car.go_backward(speed)
    time.sleep(5)
    my_car.all_suspend()
    time.sleep(1.5)

except KeyboardInterrupt:
    pass
finally:
    my_car.cleanup()
