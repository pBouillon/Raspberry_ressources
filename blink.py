# -*- coding: utf-8 -*-

'''
    Small code sample making a LED 
    on pin PIN_LED blinking each DELAY seconds
'''

import RPi.GPIO
from RPi.GPIO import cleanup
from RPi.GPIO import output
from RPi.GPIO import setup
from RPi.GPIO import setmode
from RPi.GPIO import BCM
from RPi.GPIO import HIGH
from RPi.GPIO import LOW
from RPi.GPIO import OUT

import time
from time import sleep

DELAY   = 1
PIN_LED = 18

if __name__ == '__main__':
    setmode (BCM)
    setup (PIN_LED, OUT)
    
    while True:
        try:
            output(PIN_LED, HIGH)
            sleep (DELAY)
            output(PIN_LED, LOW)
            sleep (DELAY)
        except (KeyboardInterrupt, SystemExit) as e:
            cleanup ()

