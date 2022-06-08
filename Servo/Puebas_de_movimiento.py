import RPi.GPIO as GPIO

servo = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo. GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(5)
pwm.ChangeDutyCucle(2)
