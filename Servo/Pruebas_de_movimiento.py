
import utime


# Importamos librerías de python
import RPi.GPIO as GPIO

# Pondemos en sleep los pines por un tiempo determinado
import time

#Nompramos el númmero de pin físico
servoPIN = 11

# Con este vamos a definir por enumeración de GPIO
#GPIO.setmode(GPIO.BCM)

# Con este vamos a definir por enmeración física de pines
GPIO.setmode(GPIO.BOARD)

# Indicamos si el servo será de salida o entrada de señal
GPIO.setup(servoPIN, GPIO.OUT)


def main():
    #Configura el Servo de 180
    servo_180 = PWM(servoPIN)
    servo_180.freq(50)


    while True:
        angulo = float(input('Ingrese un ángulo: '))
        if angulo >= 0 and angulo <= 180:
            duty = int((12.346*angulo**2 + 7777.8*angulo + 700000))
            servo_180.duty_16(duty)
        else:
            print('Digite un ángulo entre 0 y 180')


if __name__ == '__main__':
    main()
