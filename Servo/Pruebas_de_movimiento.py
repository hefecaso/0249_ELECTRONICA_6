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
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)

while True:
    #Init at 0°
    angulo = int(input("Ingrese un águlo: "))

    if 180 >= angulo >=0:
        pwm.start(angle_to_percent(angulo))
        time.sleep(1)


    #Close GPIO & cleanup
    #pwm.stop()
    #GPIO.cleanup()

    else:
        print("Debe de ingresar un ángulo entre 0° y 180°")
        pwm.start(angle_to_percent(0))
        #pwm.stop()
        #GPIO.cleanup()

#https://raspberrypi-espana.es/servo-frambuesa-pi/
