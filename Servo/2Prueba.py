import RPi.GPIO as GPIO
import time import sleep

GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 11 for PWM signal
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)
pwm.start(0)

pwm.ChangeDutyCycle(1.5)
sleep(3)

pwm.ChangeDutyCycle(12.5)
sleep(3)

pwm.ChangeDutyCycle(0)
sleep(3)
