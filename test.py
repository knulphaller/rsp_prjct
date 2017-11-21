import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while GPIO.input(ECHO)==0:
  print('ok')

while GPIO.input(ECHO)==1:
  print('No')

