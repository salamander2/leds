#!/usr/bin/env python
##### This program makes two LEDS blink.  It does not use the switch ####

import RPi.GPIO as GPIO
import time

# pins for LEDs
L1 = 25
L2 = 20
SW1 = 6

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
#GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#turn on LED
GPIO.output(L1, GPIO.HIGH)
GPIO.output(L2, GPIO.HIGH)
while True:
    GPIO.output(L1,GPIO.HIGH)
    GPIO.output(L2,GPIO.LOW)
    time.sleep (0.5)
    GPIO.output(L1,GPIO.LOW)
    GPIO.output(L2,GPIO.HIGH)
    time.sleep (0.5)
