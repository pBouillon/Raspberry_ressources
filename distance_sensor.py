# -*- coding: utf-8 -*-

'''
    Small code sample using the HC-SR04 sensor
    printing distance between the sensor and an object
    every ~2 seconds (TIMESTAMP_SETUP + TIMESTAMP_EXEC)
'''

import RPi.GPIO
from RPi.GPIO import output
from RPi.GPIO import input
from RPi.GPIO import setmode
from RPi.GPIO import setup
from RPi.GPIO import cleanup
from RPi.GPIO import IN
from RPi.GPIO import OUT
from RPi.GPIO import BCM

import time
from time import sleep 
from time import time

CM_CONVERTOR  = 17150
PIN_TRIGGER   = 8
PIN_ECHO      = 7
TIMESTAMP_SETUP = .5
TIMESTAMP_EXEC  = 0.00001


def loop ():
    '''Infinity loop
    Setup the trigger
    get the echo
    calculate and prints distance
    prints out of range if the distance is incorrect
    '''
    pulse_start = 0
    pulse_end   = 0
    
    while True:
        output (PIN_TRIGGER, False)
        sleep  (TIMESTAMP_SETUP)

        output (PIN_TRIGGER, True)
        sleep  (TIMESTAMP_EXEC)
        output (PIN_TRIGGER, False)

        while not input (PIN_ECHO):
            pulse_start = time()

        while input (PIN_ECHO):
            pulse_end  = time()

        distance = (pulse_end - pulse_start) * CM_CONVERTOR
        distance = round (distance, 2)
        distance-= 0.5 
        
        if 2 < distance < 250 :
            print ("Distance: ", distance, "cm")
        else:
            print ("Out Of Range (",distance,")")
        


def setup_sensor ():
    '''Setup the environment
    mode BCM
    using TRIGGER as output
    using ECHO    as input
    '''
    setmode (BCM)
    setup (PIN_TRIGGER, OUT)
    setup (PIN_ECHO,    IN )

if __name__ == '__main__':
    try:
        setup_sensor ()
        loop ()
    except (KeyboardInterrupt, SystemExit):
        cleanup ()
        exit ("\nProgram was ended and pins cleaned up     \n")
