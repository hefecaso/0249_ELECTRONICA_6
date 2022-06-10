import RPi.GPIO as GPIO
import time
import os
import stepper
import servo


def menu():
    print('\n##########################')
    print('#    Control de Github   #')
    print('##########################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Servo.")
    print("2. Stepper.")
    print("3. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        servo.servo()

    elif opc == '2':
        stepper.stepper()

    elif opc == '3':
        stepper.stepper()

    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")
