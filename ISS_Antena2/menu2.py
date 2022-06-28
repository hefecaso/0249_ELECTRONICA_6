import RPi.GPIO as GPIO
import time
import os
from os import system
#import stepper
#import servo

import ISS_Info

#################################
#   Agregando librerías motores #
#################################

import RPi.GPIO as GPIO
import time

#   **Stepper** #
out1 = 24
out2 = 25
out3 = 8
out4 = 7

i=0
positive=0
negative=0
y=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)


#   **Servo**   #

GPIO.setwarnings(False) # Disable warnings

# Use pin 11 for PWM signal
servo = 17
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)


#C onvirtiendo ángulos a ciclos de trabajo
def angulo_giro(angulo):
    giro = abs(float(angulo)/18 +2)
    return giro

def movimiento():
    pwm.start(angulo_giro(angulo))

#############################################################
#   Agregando librerías y funciones de pruebas virtuales    #
#############################################################

import ephem
import math
from datetime import datetime, timezone

#   **Configuración de azimut y elevación**   #

location = ISS_Info.iss_current_loc()
lat = location['iss_position']['latitude']
lon = location['iss_position']['longitude']
degrees_per_radian = 180.0 / math.pi
home = ephem.Observer()
home.lon = '-90.51327'
home.lat = '14.64072'
home.elevation = 1729
iss_1 = ephem.readtle('ISS',
    '1 25544U 98067A   22162.52439360  .00005833  00000+0  11028-3 0  9998',
    '2 25544  51.6455   4.6361 0004468 222.6641 220.6469 15.49954017344301'
)
home.date = datetime.utcnow()
iss_1.compute(home)
#Angulo_Elevacion = int(iss_1.alt * degrees_per_radian)
#Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
#Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
#Azimut =  int(iss_1.az * degrees_per_radian)



def angulo_giro(angulo):
    giro = float(angulo)/18 +2
    return giro

####################################################
def menu():
    print('#############################')
    print('#    Control de la antena   #')
    print('#############################')
    exec(open("ascii.py").read())
    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Elevación.")
    print("2. Azimut.")
    print("3. Azimut y elevación.")
    print("4. Target ISS.")
    print("5. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('====================================================================')
        pwm.start(0)
        exec(open("servo.py").read())
        GPIO.cleanup()
        print('====================================================================')

    elif opc == '2':
        print('====================================================================')
        exec(open("stepper.py").read())
        GPIO.cleanup()
        print('====================================================================')

    elif opc == '3':
        print('====================================================================')

        system("lxterminal -e python3 isschris2.py")

        while True:
            #exec(open("servo.py").read())

            system(f"python3 servo.py")
            exec(open("stepper.py").read())
            GPIO.cleanup()
            opc2 = input("\nEjecutar otra instrucción? y/n: ")

            if opc2 == "n":
                break
        print('====================================================================')

    elif opc == '4':
        print('====================================================================')

        #Limpiando terminal
        #os.system ("clear")

        system("lxterminal -e python3 isschris2.py")

        # Iniciando loop
        #while True:

        while True:
            #exec(open("servo.py").read())
            system(f"python3 servotarget.py")
            time.sleep(2)
            exec(open("steppertarget.py").read())
            GPIO.cleanup()
            time.sleep(2)


        print('====================================================================')

    elif opc == '5':
        print('====================================================================')
        print("Saliendo del programa.")
        pwm.stop()
        GPIO.cleanup()
        print('====================================================================')
        break

    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")


#Chekpoin menú, falta target ISS
