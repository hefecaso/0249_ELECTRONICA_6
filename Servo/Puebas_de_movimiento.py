# Importamos librerías de python
import RPi.GPIO as GPIO

# Pondemos en sleep los pines por un tiempo determinado
import time

#Nompramos el númmero de pin físico
servoPIN = 11
GPIO.setwarnings(False)
# Con este vamos a definir por enumeración de GPIO
#GPIO.setmode(GPIO.BCM)

# Con este vamos a definir por enmeración física de pines
GPIO.setmode(GPIO.BOARD)

# Indicamos si el servo será de salida o entrada de señal
GPIO.setup(servoPIN, GPIO.OUT)

# Indicamos que el pin servirá como pwm
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

# Inicamos punto de inicio
p.start(7.5)#2.5

try:

	while True:

		p.ChangeDutyCycle(7.8)

		time.sleep(5)

		p.ChangeDutyCycle(14)

		time.sleep(1)

		break;

except KeyboardInterrupt:

	p.stop()

	#break;

	'''Restablece todos los puertos que haya utilizado
	en este programa al modo de entrada'''

	GPIO.cleanup()

	#break;
