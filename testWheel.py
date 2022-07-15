#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from wheel import Wheel

en = 12
in1 = 1
in2 = 2

my_wheel = Wheel(en, in1, in2)

try:
    speed = 100

    my_wheel.forward(speed)
    time.sleep(5)
    my_wheel.suspend()
    time.sleep(1.5)

    my_wheel.backward(speed)
    time.sleep(5)
    my_wheel.suspend()
    time.sleep(1.5)

    my_wheel.brake()
    time.sleep(5)
    my_wheel.suspend()
    time.sleep(1.5)

except KeyboardInterrupt:
    pass
finally:
    my_wheel.cleanup()
