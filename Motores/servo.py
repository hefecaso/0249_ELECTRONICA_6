import RPi.GPIO as GPIO
import time
import os


GPIO.setmode(GPIO.BOARD) # Use Board numerotation mode
GPIO.setwarnings(False) # Disable warnings

# Use pin 11 for PWM signal
servo = 11
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)


#C onvirtiendo ángulos a ciclos de trabajo
def angulo_giro(angulo):
    giro = (angulo)/18 +2
    return giro


# Iniciando pwm en 0
pwm.start(0)

#Limpiando terminal
os.system ("clear")

# Iniciando loop
while True:
    angulo = float(input("\nIngrese un águlo: "))

    if 180 >= angulo >= 0:
        pwm.start(angulo_giro(angulo))
        pwm.stop()
        GPIO.cleanup()
        print("Saliendo al menú principal")
        break

    elif angulo > 180 and 0 < angulo:
        print("\nIngrese un ángulo entre 180° y 190°")


''''
        DC 7% | neut | 90°
        DC 2% | min  | 0°
        DC 12%| max  | 180°
'''

#################
#   Referencias #
#################

# Tutorial: https://raspberrypi-espana.es/servo-frambuesa-pi/

# Referencias importantes
# Teória y cálculos: https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/?utm_source=youtube&utm_medium=description&utm_campaign=link_in_description_FYb7Pr2XNxE#Step-3-Calculate-duty-cycle-to-degrees-formula-for-the-Servo-Motor
# Teoría youtube: https://www.youtube.com/watch?v=ddlDgUymbxc&ab_channel=GavenMacDonald
