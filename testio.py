#!/usr/bin/python
# coding=utf-8
# 本段代码实现树莓派智能小车的红外避障效果
# 代码使用的树莓派GPIO是用的BOARD编码方式。
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