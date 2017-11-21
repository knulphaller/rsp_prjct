import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
#a = GPIO.input(4)
#for i in range(0,5):
#    print(GPIO.input(4))
while  True:
    a = GPIO.input(4)
    
    if a == 1:
    	print("Qaranliqdi qaqa")
    elif a == 0:
        print("Hemishe ishiqliqda qaqa")
    time.sleep(1)
