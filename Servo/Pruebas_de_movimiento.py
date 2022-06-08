#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################
#                                               #
# Servos control module                         #
# Authors: Ismael Tobar and Raquel Muñoz        #
#                                               #
#################################################
#----Libraries
import RPi.GPIO as GPIO
import threading from time
import sleep
# Constants:
T = 20 #signal period (ms).
STEPS = 50 #Number of iteration that the signal is repeated. This is necesary to the servo has time to change.
MIN_PULSE = 0.83 #Min width of pulse. (ms)
MAX_PULSE = 2.2 #Max width of pulse. (ms) #2.6
MIN_DEGREE = 0 MAX_DEGREE = 180 DEGREE_MS = (MAX_PULSE-MIN_PULSE)/180 #Transform the degree to applicate into a time (in ms) variable
INITIAL_PULSE = 1.74

#Variables
servo_stopped = True
#Servos' pins
S1 = 11

# Raspberry Pi GPIO Configuration:
def setup():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(S1,GPIO.OUT)

  GPIO.output(S1, False)

  print('Servo: Setup')

def thread_servo(d,s): #The pwm signal is done through Software global servo_stopped
  h = d/1000
  l = (T-d)/1000
  if MIN_PULSE <= d <= MAX_PULSE:
    for i in range (0,STEPS):
      GPIO.output(s, True)
      sleep(h)
      GPIO.output(s, False)
      sleep(l)
      servo_stopped = True
  clean()
  #Each time you finish moving the servo is necessary to clean the pins so they do not move with noise

  #move the selected servo (n=1 or n=2) to the degree indicated (between 0 and 180)
def moveServo(degree,n):
  print('moveServo',degree,n)
  global servo_stopped
  try:
    if servo_stopped:
      if MIN_DEGREE <= degree <= MAX_DEGREE:
        setup()
        print(degree)
        if n == 1:
          thread_s = threading.Thread(target=thread_servo, args=((degree * DEGREE_MS) + MIN_PULSE, S1, ))
          servo_stopped = False
          thread_s.start()

  except Exception as e:
    print("Servo: Error starting servo thread")
    print(e)

def clean():
  GPIO.cleanup(S1)


def stop_servo():
  global servo_stopped
  servo_stopped = True

if __name__ == "__main__":
  terminate = False #finish the while()
  # if run directly we'll just create an instance of the class and output
  setup()
  ser = 3
  while terminate == False:
    sleep(0.1)
    ser = 3
    ser = input('Enter servo 1 or 2: (0 to exit) : ')
    if ser == 0:
      terminate = True
    else:
      deg = input('Enter degree (0 to 180) : ') #The degrees are asked
      if 1<= ser <= 2:
        moveServo(deg,ser)
  GPIO.cleanup() print('Servo: Exit servo')
