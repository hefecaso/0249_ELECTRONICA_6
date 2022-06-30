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

screen = turtle.Screen()
screen.title("ISS TRACKER")
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("world.png")
screen.register_shape("iss.gif")
#screen.register_shape("gt.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

gt = turtle.Turtle()
#gt.shape("gt.gif")
gt.penup()
cerco = turtle.Turtle()
cerco.penup()
# Latitud y Logitud de Guatemala
latitud=15.783471
longitud=-90.230759
n=6 #número de veces que pasará la ISS
Pass=url.Request('http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n={}'.format(latitud,longitud,n))
response_Pass= url.urlopen(Pass)

def pasoISS():
    Pass_obj = json.loads(response_Pass.read())
    #print (Pass_obj)
    pass_list=[]
    for count,item in enumerate(Pass_obj["response"], start=0):
        pass_list.append(Pass_obj['response'][count]['risetime'])
        print("Proximos pases sobre Guatemala")
        print(datetime.fromtimestamp(pass_list[count]).strftime('%d-%m-%Y %H:%M:%S'))



def tracker():
    pasoISS()
    while True:

        try:

            location = ISS_Info.iss_current_loc()
            lat = location['iss_position']['latitude']
            lon = location['iss_position']['longitude']
            screen.title("ISS TRACKER: (Latitude: {},  Longitude: {})".format(lat,lon))
            iss.goto(float(lon),float(lat))
            iss.pencolor("red")
            iss.dot(iss.goto(float(lon),float(lat)))
            gt.pencolor("orange")
            gt.dot(gt.goto(float(longitud),float(latitud)))
            cerco.pencolor("magenta")
            cerco.dot(cerco.goto(float(-107.324236),float(19.819178)))
            cerco.forward(0.32465)
            cerco.left(90)
            cerco.forward(30.652475)
            cerco.left(90)
            cerco.forward(4.708913)
            cerco.left(90)
            cerco.forward(1.782958)
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
            print('Elevacion:', Angulo_Elevacion ,', Azimut:', Azimut)
            time.sleep(5)

        except Exception as e:
            print(str(e))
            break
t = threading.Thread(target=tracker())
t.start()
#pasoISS()


def elevacion():
    Angulo_Elevacion = '%4.1f' % (iss_1.alt * degrees_per_radian)
    return Angulo_Elevacion

def azimut():
    Azimut =  '%5.1f' % (iss_1.az * degrees_per_radian)
    return Azimut

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
            if 6.09958 < iss.lat < 20.143828 and -109.107194 < iss.lon < -76.671761:

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


#Chekpoin menú, falta target ISS
