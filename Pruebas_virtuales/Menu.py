#import RPi.GPIO as GPIO
import time
import os
from os import system
#import stepper
import Servo_target_virtual as stv

import ISS_Info
import turtle
import time
import threading

import ephem
import math
from datetime import datetime, timezone


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
Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)


def angulo_giro(angulo):
    giro = (angulo)/18 +2
    return giro

def movimiento(angulo):
    print(f"girando {angulo_giro(angulo)}")

def contador():
  numero = 0
  while True:
    numero += 1
    yield numero

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
        #pwm.start(0)
        #exec(open("servo.py").read())
        #GPIO.cleanup()
        print('====================================================================')

    elif opc == '2':
        print('====================================================================')
        #exec(open("stepper.py").read())
        #GPIO.cleanup()
        print('====================================================================')

    elif opc == '3':
        print('====================================================================')
        #while True:
            #exec(open("servo.py").read())
            #system(f"python3 servo.py")
            ##GPIO.cleanup()
            #opc2 = input("\nEjecutar otra instrucción? y/n: ")

            #if opc2 == "n":
                #break
        print('====================================================================')

    elif opc == '4':
        print('====================================================================')
        #system("lxterminal -e python3 isschris.py")
        system("gnome-terminal -- python isschris.py")
        #azimut = isc2.azimut()
        #elevacion = isc2.elevacion()
        cuenta = contador()
        for i in range(1000):
           #print(f"Azimut {next(cuenta)}° | Elevación {next(cuenta)}°")
           print(f"Azimut {Azimut}° | Elevación {Angulo_Elevacion}°")
           time.sleep(2)
        #angulo = input(input("Ingrese un ángulo: "))
        #movimiento(angulo)
        print('====================================================================')

    elif opc == '5':
        print('====================================================================')
        print("Saliendo del programa.")
        #pwm.stop()
        #GPIO.cleanup()
        print('====================================================================')
        break

    else:
        continue


#Chekpoin menú, falta target ISS
