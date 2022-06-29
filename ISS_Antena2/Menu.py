import RPi.GPIO as GPIO
import time
import os
from os import system
import sys 


sys.path.append("/isschris2")
from isschris2 import lon, lat

#import stepper
#import servo



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

        # Abriendo mapa
        system("lxterminal -e python3 isschris2.py")

        # Colocando servo y stepper en punto de partida, dirección Norte
        print("\nRegrsando al origen: \n")

        if 6.09958 < lat < 20.143828 and -109.107194 < lon < -76.671761: 
            system(f"python3 servo_origin.py")
            exec(open("stepper_origin.py").read())
            GPIO.cleanup()
            time.sleep(5)

            # Moviendo dirección a la ISS
            system(f"lxterminal -e python3 servotarget.py")
            system(f"lxterminal -e python3 steppertarget.py")



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
