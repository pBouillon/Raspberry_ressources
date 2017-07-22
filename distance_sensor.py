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
PIN_TRIGGER   = 23
PIN_ECHO      = 24
TIMESTAMP_SETUP = 2
TIMESTAMP_EXEC  = 0.00001


def loop ():
	pulse_start = 0
	pulse_end   = 0
	while True:
		output (PIN_TRIGGER, False)
		sleep  (TIMESTAMP_SETUP)

		output (PIN_TRIGGER, True)
		sleep  (TIMESTAMP_EXEC)
		output (PIN_TRIGGER, False)

		while input (PIN_ECHO) == 0:
			pulse_start = time()

		while input (PIN_ECHO) == 1:
			pulse_end  = time()

		distance = (pulse_end - pulse_start) * CM_CONVERTOR
		distance = round (distance, 2)
		distance-= 0.5 
		
		if 2 < distance < 250 :
			print ("Distance: ", distance, "cm")
		else:
			print ("Out Of Range (",distance,")")
		


def setup_sensor ():
	setmode (BCM)
	
	setup (PIN_TRIGGER, OUT)
	setup (PIN_ECHO,    IN )
	

if __name__ == '__main__':
	try:
		setup_sensor ()
		loop ()
	except (KeyboardInterrupt, SystemExit):
		cleanup ()
		exit ("\nProgram was ended and pins cleaned up 	\n")
