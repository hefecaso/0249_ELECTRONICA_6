import RPi.GPIO as GPIO
from time import sleep

servo = 111

GPIO.setmode(GPIO.BOARD)

def main():
    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)

    while True:
        angulo = float(input('Ingrese ángulo: '))
        if angulo >= 0 and  angulo <= 180:
            duty = int(12.346*angulo**2 + 7777.8*angulo + 700000)
            servo.duty_ns(duty)

        else:
            print("Digite un ángulo entre 0 y 180")

if __name__ == '__main__':
    main()
