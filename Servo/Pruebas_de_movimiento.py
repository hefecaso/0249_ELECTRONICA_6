#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 11 for PWM signal
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)


#Convirtiendo ángulos a ciclos de trabajo
def angulo_giro(angulo):
    if angulo > 180 or angulo < 0 :
        return False
    giro = (angulo)/18 +2
    return giro

def movimiento():
    angulo = float(input("Ingrese un águlo: "))
    pwm.start(angulo_giro(angulo))

pwm.start(0)

while True:
    #Init at 0°
    movimiento()


''''
        DC 7% |neut | 90°
        DC 2% | min | 0°
        DC 12%| max | 180°
'''
# Tutorial: https://raspberrypi-espana.es/servo-frambuesa-pi/
# Teória y cálculos: https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/?utm_source=youtube&utm_medium=description&utm_campaign=link_in_description_FYb7Pr2XNxE#Step-3-Calculate-duty-cycle-to-degrees-formula-for-the-Servo-Motor
# Teoría youtube: https://www.youtube.com/watch?v=ddlDgUymbxc&ab_channel=GavenMacDonald
