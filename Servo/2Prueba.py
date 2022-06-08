import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 11 for PWM signal
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)
pwm.start(0)

print("90 derecha")
pwm.ChangeDutyCycle(1.5)
sleep(3)

print("-90 derecha")
pwm.ChangeDutyCycle(12.5)
sleep(3)

print("0")
pwm.ChangeDutyCycle(0)
sleep(3)
