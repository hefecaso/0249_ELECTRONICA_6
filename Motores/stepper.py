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



GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
#print("Ingrese el valor de azimut (0-360°)")
#deg = int(input())
#def deg-re

def stepper():
    GPIO.output(out1,GPIO.LOW)
    GPIO.output(out2,GPIO.LOW)
    GPIO.output(out3,GPIO.LOW)
    GPIO.output(out4,GPIO.LOW)
    print("ingrese un valor para rotar un angulo de 0 a 360")
    deg = int(input())
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

stepper()
#except KeyboardInterrupt:
    #GPIO.cleanup()
