import RPi.GPIO as GPIO
import time

out1 = 24
out2 = 25
out3 = 8
out4 = 7

i=0
positive=0
negative=0
y=0

GPIO.setwarnings(False) # Disable warnings

# Use pin 11 for PWM signal
servo = 17
frequence = 50
GPIO.setup(servo, GPIO.OUT)
pwm = GPIO.PWM(servo, frequence)


#C onvirtiendo ángulos a ciclos de trabajo
def angulo_giro(angulo):
    if angulo > 180 or angulo < 0 :
        return False
    giro = (angulo)/18 +2
    return giro

# Ingreso del ángulo por el usuario
def movimiento(angulo):
    pwm.start(angulo_giro(angulo))

# Iniciando pwm en 0
pwm.start(0)

#Limpiando terminal
os.system ("clear")

GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
#print("Ingrese el valor de azimut (0-360°)")
#deg = int(input())
#def deg-re

try:
   while(1):
      GPIO.output(out1,GPIO.LOW)
      GPIO.output(out2,GPIO.LOW)
      GPIO.output(out3,GPIO.LOW)
      GPIO.output(out4,GPIO.LOW)
      print("ingrese un valor para rotar un angulo de 0 a 360")
      deg = int(input())
      angulo = float(input("\nIngrese un águlo: "))
      x = int(-1*(deg*4096)/(360))
      if x>0 and x<=4096:
          #x=x*-1
          for y in range(x,0,-1):
              if negative==1:
                  if i==7:
                      i=0
                  else:
                      i=i+1
                  y=y+2
                  negative=0
              positive=1
              #print((x+1)-y)
              if i==0:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==1:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==2:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==3:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==4:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==5:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==6:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==7:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              if i==7:
                  i=0
                  continue
              i=i+1


        if 180 >= angulo >= 0:
            movimiento(angulo)

        elif angulo > 180 and 0 < angulo:
            print("Debe de ingresar un ángulo entre 180° y 0°")
            selec = input("Desea regresar al menú principal? Y/N: ")

            if selec == "N":
                print("Recuerde ingresar un ángulo entre 180° y 0°")

            else:
                #Close GPIO & cleanup
                print("\nRegresando a punto de origen ángulo 0°")
                pwm.start(angulo_giro(0))
                time.sleep(2)
                pwm.stop()
                GPIO.cleanup()
                print("Saliendo al menú principal")
                break

      elif x<0 and x>=-4096:
          x=x*-1
          for y in range(x,0,-1):
              if positive==1:
                  if i==0:
                      i=7
                  else:
                      i=i-1
                  y=y+3
                  positive=0
              negative=1
              #print((x+1)-y)
              if i==0:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==1:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==2:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==3:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.HIGH)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==4:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.LOW)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==5:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.HIGH)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==6:
                  GPIO.output(out1,GPIO.LOW)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              elif i==7:
                  GPIO.output(out1,GPIO.HIGH)
                  GPIO.output(out2,GPIO.LOW)
                  GPIO.output(out3,GPIO.LOW)
                  GPIO.output(out4,GPIO.HIGH)
                  time.sleep(0.003)
                  #time.sleep(1)
              if i==0:
                  i=7
                  continue
              i=i-1


        if 180 >= angulo >= 0:
            movimiento(angulo)

        elif angulo > 180 and 0 < angulo:
            print("Debe de ingresar un ángulo entre 180° y 0°")
            selec = input("Desea regresar al menú principal? Y/N: ")

            if selec == "N":
                print("Recuerde ingresar un ángulo entre 180° y 0°")

            else:
                #Close GPIO & cleanup
                print("\nRegresando a punto de origen ángulo 0°")
                pwm.start(angulo_giro(0))
                time.sleep(2)
                pwm.stop()
                GPIO.cleanup()
                print("Saliendo al menú principal")
                break

except KeyboardInterrupt:
    GPIO.cleanup()
