#!/usr/bin/env python
#### This program just turns on one LED and exits ####
import RPi.GPIO as GPIO

# pins for LEDs
L1 = 7

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)

#turn on LED
GPIO.output(L1, GPIO.HIGH)

#GPIO.cleanup()
