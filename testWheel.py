#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from wheel import Wheel

en = 12
in1 = 5
in2 = 6

# en = 13
# in1 = 17
# in2 = 27

# en = 18
# in1 = 23
# in2 = 24

# en = 19
# in1 = 20
# in2 = 21

my_wheel = Wheel(en, in1, in2)

try:
    speed = 100

    my_wheel.forward(speed)
    time.sleep(2)
    my_wheel.forward(75)
    time.sleep(2)
    my_wheel.forward(50)
    time.sleep(2)
    my_wheel.forward(25)
    time.sleep(2)
    my_wheel.suspend()
    time.sleep(1.5)

    # my_wheel.backward(speed)
    # time.sleep(5)
    # my_wheel.suspend()
    # time.sleep(1.5)

    # my_wheel.brake()
    # time.sleep(5)
    # my_wheel.suspend()
    # time.sleep(1.5)

except KeyboardInterrupt:
    pass
finally:
    my_wheel.cleanup()
