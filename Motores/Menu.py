import RPi.GPIO as GPIO
import time
import os
from os import system
#import stepper
#import servo


def menu():
    print('#############################')
    print('#    Control de la antena   #')
    print('#############################')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Elevación.")
    print("2. Azimut.")
    print("3. Azimut y elevación.")
    print("4. Salir.\n")


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
        print("Saliendo del programa.")
        pwm.stop()
        GPIO.cleanup()
        print('====================================================================')
        break

    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")


#Chekpoint 13/7/2022
