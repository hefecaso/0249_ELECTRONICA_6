import RPI.GPIO as GPIO
from gpiozero import AngularServo
from time import sleep

servo = AngularServo(11, min_pulse_width=0.0006, max_pulse_width=0.0023)

while True:
    servo.angle = 90.0
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = -90.0
    sleep(2)
