import RPi.GPIO as GPIO
from time import sleep

servo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)

pwm=GPIO.PWM(servo, 50)
pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)

SetAngle(90)
pwm.stop()
GPIO.cleanup()
