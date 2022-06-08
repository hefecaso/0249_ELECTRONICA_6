#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 11 for PWM signal
pwm_gpio = 11
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

while True:
    #Init at 0°
    angulo = int(input("Ingrese un águlo: "))
    pwm.start(angle_to_percent(angulo))
    time.sleep(1)


    #Close GPIO & cleanup
    #pwm.stop()
    #GPIO.cleanup()

else:
    pwm.stop()
    GPIO.cleanup()

#https://raspberrypi-espana.es/servo-frambuesa-pi/
