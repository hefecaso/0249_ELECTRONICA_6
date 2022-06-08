#//////////////////////////////////////////////////////////////////////
#/  INTERPRETE  ///////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

#!/usr/bin/python3
#es una ruta del interprete, en este caso el de python3

#//////////////////////////////////////////////////////////////////////
#/  LIBRERIAS  ////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

#importar las librerias
import time
import pigpio
import RPi.GPIO as GPIO
import math

#//////////////////////////////////////////////////////////////////////
#/  CONFIGURACION  ///////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

GPIO.setmode(GPIO.BOARD) #utilizar el sistema de numeracion fisica
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #configurar el pin 13 como entrada e internamente una resistencia pull down

#//////////////////////////////////////////////////////////////////////
#/  VARIABLES GLOBALES  ///////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

pi = pigpio.pi() #inicializar la variable pi

#//////////////////////////////////////////////////////////////////////
#/  PRINCIPAL  ///////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////

pi.set_servo_pulsewidth(11,2390) #girar el servo hasta 0 grados como inicio
time.sleep(0.5) #esperar medio segundo
#input('Pulse la tecla enter para seguir el paso ')

try:
        print('Pulse el boton de interrupcion para comenzar')
        GPIO.wait_for_edge(11, GPIO.RISING, timeout=5000) #configurar el pin 13 una interrupcion de tipo espera, con un maximo tiempo de 5 segundos
        while True:
                #se espera a que el usuario introduzca un valor de grado
                grados = float(input('Introducza el valor en grados, entre 0 y 180: '))
                radianes = ((2 * math.pi) / 360) * grados
                print("El angulo introducido es", radianes, "radianes")
                grados = 180 - grados
                #conversion de grados a radianes y lo imprime
                #compara los grados y dependiendo de la condicion realiza la funcion utilizando valores de microsegundos empiricamente
                if grados < 0 or grados >180:
                    #imprime cuando el usuario introduce un valor fuera del rango
                    print("El dato introducido es erroneo")
                    print("Debe de introducir entre 0 y 180 grados")
                elif grados == 0:
                    pi.set_servo_pulsewidth(11,510)
                elif grados < 10:
                        Nms = grados*4+515
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 10:
                        pi.set_servo_pulsewidth(11,555)
                elif grados < 20:
                        Nms = (grados-10)*8+555
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 20:
                        pi.set_servo_pulsewidth(11,635)
                elif grados < 30:
                        Nms = (grados-20)*9+635
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 30:
                        pi.set_servo_pulsewidth(11,725)
                elif grados < 40:
                        Nms = (grados-30)*9.5+725
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 40:
                        pi.set_servo_pulsewidth(11,820)
                elif grados < 45:
                        Nms = (grados-40)*1+820
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 45:
                        pi.set_servo_pulsewidth(11,825)
                elif grados < 50:
                        Nms = (grados-45)*25+825
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 50:
                        pi.set_servo_pulsewidth(11,950)
                elif grados < 60:
                        Nms = (grados-40)*10+950
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 60:
                        pi.set_servo_pulsewidth(11,1050)
                elif grados < 70:
                        Nms = (grados-60)*8+1050
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 70:
                        pi.set_servo_pulsewidth(11,1130)
                elif grados < 80:
                        Nms = (grados-70)*12+1130
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 80:
                        pi.set_servo_pulsewidth(11,1250)
                elif grados < 90:
                        Nms = (grados-80)*5+1250
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 90:
                        pi.set_servo_pulsewidth(11,1300)
                elif grados < 100:
                        Nms = (grados-90)*12.5+1300
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 100:
                        pi.set_servo_pulsewidth(11,1425)
                elif grados < 110:
                        Nms = (grados-100)*16.5+1425
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 110:
                        pi.set_servo_pulsewidth(11,1590)
                elif grados == 122:
                        pi.set_servo_pulsewidth(11,1750)
                elif grados < 120:
                        Nms = (grados-110)*11+1590
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 120:
                        pi.set_servo_pulsewidth(11,1700)
                elif grados < 130:
                        Nms = (grados-120)*12.5+1700
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 130:
                        pi.set_servo_pulsewidth(11,1825)
                elif grados < 140:
                        Nms = (grados-130)*11.5+1825
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 140:
                        pi.set_servo_pulsewidth(11,1940)
                elif grados < 150:
                        Nms = (grados-140)*11+1940
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 150:
                        pi.set_servo_pulsewidth(11,2050)
                elif grados < 160:
                        Nms = (grados-150)*12+2050
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 160:
                        pi.set_servo_pulsewidth(11,2170)
                elif grados < 170:
                        Nms = (grados-160)*11+2170
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 170:
                        pi.set_servo_pulsewidth(11,2280)
                elif grados < 180:
                        Nms = (grados-170)*10+2280
                        pi.set_servo_pulsewidth(11,Nms)
                elif grados == 180:
                        pi.set_servo_pulsewidth(11,2390)
                time.sleep(1)
except KeyboardInterrupt: #si el usuario pulsa CONTROL + C entonces imprime lo siguiente
    print("")
    print("Salir de programa")
except:
    print("Otros problemas ocurridos")
finally:
    pi.stop()
    GPIO.cleanup() #limpiamos los pines GPIO y paramos el servo en cualquier caso aunque ocurra una excepcion
