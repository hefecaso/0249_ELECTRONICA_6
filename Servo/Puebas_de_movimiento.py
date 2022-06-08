import RPi.GPIO as GPIO

servo = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)

pwm = GPIO.PWM(servo, 50)
pwm.start(5)
pwm.ChangeDutyCycle(2)
GPIO.cleanup()
