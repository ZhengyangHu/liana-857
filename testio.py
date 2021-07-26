#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
import time
import sys
testio=13
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
GPIO.setup(testio, GPIO.IN)
while True:
    g=GPIO.input(testio)
    print(g)