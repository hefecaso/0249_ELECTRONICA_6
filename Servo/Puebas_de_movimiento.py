import RPi.GPIO as GPIO

servo = 111

GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(5)
pwm.ChangeDutyCucle(2)
