import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while GPIO.input(4) ==1:
    print ('Yangin')

while GPIO.input(4) ==0:
    print ('Yangin sonub')

