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
        system("lxterminal -- python isschris.py")
        cuenta = contador()
        for i in range(1000):
           print(f"Azimut {next(cuenta)}° | Elevación {next(cuenta)}°")
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
