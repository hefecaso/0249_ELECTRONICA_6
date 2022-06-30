import RPi.GPIO as GPIO
import time
import os
from os import system
import sys
import ISS_Info
import turtle
import time
import threading
import math
#from mpl_toolkits.basemap import Basemap
#librerias predicciones
import urllib.request as url
import json
#import folium

import urllib.request as url
import json
import ephem
from datetime import datetime, timezone
#import stepper
#import servo

# Latitud y Logitud de Guatemala
latitud=15.783471
longitud=-90.230759
n=6
 #número de veces que pasará la ISS
Pass=url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud,longitud,n))
response_Pass= url.urlopen(Pass)

def pasoISS():
    Pass_obj = json.loads(response_Pass.read())
    #print (Pass_obj)
    pass_list=[]

    for count,item in enumerate(Pass_obj["response"], start=0):
        pass_list.append(Pass_obj['response'][count]['risetime'])

def tracker():
    pasoISS()
    while True:
        location = ISS_Info.iss_current_loc()
        lat = location['iss_position']['latitude']
        lon = location['iss_position']['longitude']


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
        system(f"lxterminal -e python3 servo.py")
        print('====================================================================')

    elif opc == '2':
        print('====================================================================')
        system(f"lxterminal -e python3 stepper.py")
        print('====================================================================')

    elif opc == '3':
        print('====================================================================')

        system(f"lxterminal -e python3 servo.py")
        system(f"lxterminal -e python3 stepper.py")

        #system("lxterminal -e python3 isschris2.py")

        print('====================================================================')

    elif opc == '4':


        print('====================================================================')


        # Abriendo mapa
        system("lxterminal -e python3 isschris2.py")

        while True:
            if 6.09958 < lat < 20.143828 and -109.107194 < lon < -76.671761:

                #system(f"python3 servo_origin.py")
                #exec(open("stepper_origin.py").read())
                #GPIO.cleanup()
                #time.sleep(5)
            # Moviendo dirección a la ISS
                system(f"lxterminal -e python3 servotarget.py")
                system(f"lxterminal -e python3 steppertarget.py")
                continue

            else:
                print("ISSS fuera de rango")
                time.sleep(5)

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
