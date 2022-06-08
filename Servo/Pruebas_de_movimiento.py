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

def angulo_giro(angulo):
    if angulo > 180 or angulo < 0 :
        return False    
    giro = (angulo)/18 +2
    return giro

#pwm.start(7.5)
while True:
    #Init at 0°


    angulo = float(input("Ingrese un águlo: "))
    pwm.start(angulo_giro(angulo))


''''
        7 = 90
        2 = 0
        12 = 180
'''
#https://raspberrypi-espana.es/servo-frambuesa-pi/
