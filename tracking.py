#!/usr/bin/python
# coding=utf-8
# 本段代码实现树莓派智能小车的红外避障效果
# 代码使用的树莓派GPIO是用的BOARD编码方式。
import RPi.GPIO as GPIO
import time
import sys

T_SensorRight = 13
T_SensorLeft = 26

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin = 19
Gpin = 5
Rpin = 6


def t_up(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)  # BIN1
    time.sleep(t_time)


def t_stop(t_time):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_down(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)


def t_left(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)  # BIN1
    time.sleep(t_time)


def t_right(speed, t_time):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(t_time)





def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
    GPIO.setup(T_SensorRight, GPIO.IN)
    GPIO.setup(T_SensorLeft, GPIO.IN)

    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)


if __name__ == '__main__':
    setup()
    L_Motor = GPIO.PWM(PWMA, 100)
    L_Motor.start(0)
    R_Motor = GPIO.PWM(PWMB, 100)
    R_Motor.start(0)
    GPIO.setup(T_SensorRight,GPIO.IN)
    GPIO.setup(T_SensorLeft,GPIO.IN)
    try:
        while True:
            SR = GPIO.input(T_SensorRight)
            SL = GPIO.input(T_SensorLeft)

            if SL == False and SR == False:
                print("t_up")
                t_up(50, 0)
            elif SL == True and SR == False:
                print("Left")
                t_left(50, 0)
            elif SL == False and SR == True:
                print("Right")
                t_right(50, 0)
            else:
                print("stop")
                t_stop(0)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        #t_stop(0)
        GPIO.cleanup()