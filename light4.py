#!/usr/bin/env python
##### This program makes two LEDS blink.  Pressing the switch changes the delay.

import RPi.GPIO as GPIO
import time

# pins for LEDs
L1 = 7
L2 = 8
SW1 = 22
delay = 0.8

#set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#turn on LED
GPIO.output(L1, GPIO.HIGH)
GPIO.output(L2, GPIO.HIGH)
while True:
    if (GPIO.input(SW1) == 0):     #switch is pressed
        delay = 0.1
    else:
        delay = 0.8
    GPIO.output(L1,GPIO.HIGH)
    GPIO.output(L2,GPIO.LOW)
    time.sleep (delay)
    GPIO.output(L1,GPIO.LOW)
    GPIO.output(L2,GPIO.HIGH)
    time.sleep (delay)
