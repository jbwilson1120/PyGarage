print(" Control + C to exit Program")

import time
import pinconfig

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(pinconfig.DOOR1_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR1_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor
GPIO.setup(pinconfig.DOOR2_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR2_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor
GPIO.setup(pinconfig.DOOR3_CLOSED_SENSOR, GPIO.IN, GPIO.PUD_DOWN)  # Door is Closed sensor
GPIO.setup(pinconfig.DOOR3_OPEN_SENSOR, GPIO.IN, GPIO.PUD_DOWN)    # Door is Open sensor

try:
  while 1 >=0:
    print('DOOR1_CLOSED_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR1_CLOSED_SENSOR)))
    print('DOOR1_OPEN_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR1_OPEN_SENSOR)))
    print('DOOR2_CLOSED_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR1_CLOSED_SENSOR)))
    print('DOOR2_OPEN_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR2_OPEN_SENSOR)))
    print('DOOR3_CLOSED_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR1_CLOSED_SENSOR)))
    print('DOOR3_OPEN_SENSOR\t= '+str(GPIO.input(pinconfig.DOOR3_OPEN_SENSOR)))
    time.sleep(1)             # pauses system for 1 second

except KeyboardInterrupt:     # Stops program when "Control + C" is entered
  GPIO.cleanup()               # Turns OFF all relay switches
