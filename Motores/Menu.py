import RPi.GPIO as GPIO
import time
import os
#import stepper
import servo


def menu():
    print('#############################')
    print('#    Control de la antena   #')
    print('#############################')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Servo.")
    print("2. Stepper.")
    print("3. Ambos.")
    print("4. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('====================================================================')
        servo.servo()
        print('====================================================================')

    elif opc == '2':
        print('====================================================================')
        #stepper.stepper()
        print('====================================================================')

    elif opc == '3':
        print('====================================================================')

        while True:
            angulo = float(input("\nIngrese un águlo: "))
            if 180 >= angulo >= 0:
                servo.movimiento()
                time.sleep(1.5)

        print('====================================================================')

    elif opc == '4':
        print('====================================================================')
        print("Saliendo del programa.")
        print('====================================================================')
        break

    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")


#Chekpoint 13/7/2022
