import RPi.GPIO as GPIO
import time
import os
from os import system
#import stepper
#import servo





####################################################
def menu():
    print('\n        #############################')
    print('        #    Control de la antena   #')
    print('        #############################')
    exec(open("ascii.py").read())

    '''
    print("\nRegresando a elevación 0°: \n")

    print("Moviendo servo a 0°")

    system(f"python3 servo_origin.py")

    print("\nRegresando a azimut 0°: \n")

    exec(open("stepper_origin.py").read())
    GPIO.cleanup()
    time.sleep(5)
    print("\n")
    '''

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Elevación.")
    print("2. Azimut.")
    print("3. Azimut y elevación.")
    print("4. Target ISS.")
    print("5. Ver mapa.")
    print("6. Salir.\n")


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
        #import sys
        #sys.path.append("/isschris2")
        #from isschris2 import lat, lon

        #Punto 1 = valor
        #Punto 2 = valor
        #Punto 3 = valor
        #Punto 4 = valor

        print('====================================================================')

        #Ejecuntando motores

        system(f"lxterminal -e python3 servotarget.py")
        system(f"lxterminal -e python3 steppertarget.py")

        # Abriendo mapa
        system("lxterminal -e python3 isschris2.py")

        #while True:
            #if condicion 1 > latitud and condicion 1 > longitud:
                #print("La ISS no se encuentra en rango.")

            #if condicion 1 < latitud and condicion 1 < longitud:
                #print("La ISS está en rango")
                #Ejecutar todo lo que hay aquí abajo

        # Colocando servo y stepper en punto de partida, dirección Norte

        #if 6.09958 < lat < 20.143828 and -109.107194 < lon < -76.671761:

            #system(f"python3 servo_origin.py")
            #exec(open("stepper_origin.py").read())
            #GPIO.cleanup()
            #time.sleep(5)
        # Moviendo dirección a la ISS
            #system(f"lxterminal -e python3 servotarget.py")
            #system(f"lxterminal -e python3 steppertarget.py")



        print('====================================================================')

    elif opc == '5':
        print('====================================================================')
        print("\nAbriendo mapa.\n")
        # Abriendo mapa
        system("lxterminal -e python3 isschris2.py")

        print('====================================================================')

    elif opc == '6':
        print('====================================================================')

        print("\nRegresando a elevación 0°: \n")

        print("Moviendo servo a 0°")

        system(f"python3 servo_origin.py")

        print("\nRegresando a azimut 0°: \n")

        exec(open("stepper_origin.py").read())
        GPIO.cleanup()
        time.sleep(5)
        print("\n")

        print("Saliendo del programa.")
        #pwm.stop()
        GPIO.cleanup()
        print('====================================================================')
        break

    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")


#Chekpoin menú, falta target ISS
