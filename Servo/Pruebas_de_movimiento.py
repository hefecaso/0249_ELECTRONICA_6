#!/usr/bin/python
#coding:utf-8-*
import RPi.GPIO as GPIO #Importamos la libreria RPi.GPIO
import time #Importamos la libreria time para los delays
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,50)
p.start(2.5)
time.sleep(0.5)
                    #Ponemos la Raspberry en modo BOARD(Los pines fisicos)
                    #Indicamos el pin 11 como salida,el1Vccyel3GND
                    #Ponemos el pin 11 en modo PWMyenviamos 50 pulsos por
                    #Necesario para comenzar el PWM en el dutycicle 2.5 equi
                    #Un delay de medio segundo
input("Pulse un númeroyenter para comenzar")
try:
   while True:#Iniciamos un loop infinito
      grados=float(input("Introduzca un valor en grados,entre0y180:"))
      if grados<=90:
         Nms=grados*0.01+0.5#Calculamos el numero de ms,los grados por0
         dc=(Nms*100)/20#Calculamos el DutyCycle,haciendo una regla
         p.ChangeDutyCycle(dc)
      elif grados<=180:
         Nms=grados*0.0105+0.5#Son 0.94 ms(2,34-1,4)no 0.873(apuntes)lo
         dc(Nms*100)/20
         p.Change DutyCycle(dc)
      else:
         print("El dato introducido es erróneo")
         print("Debe introducir un valor entre0y180")
except KeyboardInterrupt:
except:
finally:
                #2,5 dc equivalea0grados,7son 90y11,95 son 180,son0
   p.stop()#Termina el PWM
   print("Error Inesperado")
   GPIO.cleanup()#Limpia las entradas
