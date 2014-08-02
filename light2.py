#!/usr/bin/env python
#### This program turns on two LEDs and then turns one off it the switch is pressed.  ####
import RPi.GPIO as GPIO

# pins for LEDs
L1 = 7
L2 = 8
SW1 = 22

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#turn on LED
GPIO.output(L1, GPIO.HIGH)
GPIO.output(L2, GPIO.HIGH)
while True:
    if(GPIO.input(SW1) == 1):
        GPIO.output(L1,GPIO.HIGH)
    if(GPIO.input(SW1) == 0):
        GPIO.output(L1,GPIO.LOW)
