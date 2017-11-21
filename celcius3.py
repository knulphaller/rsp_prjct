import RPi.GPIO as GPIO
import time

def bin2dec(string_num): # define a function to convert a binary number t$
    return str(int(string_num, 2)) # return the string representing the i$

data = [] # define a data array

GPIO.setmode(GPIO.BCM) # use the Broadcom numbers instead of the WiringPi$

GPIO.setup(4,GPIO.OUT)  # Set it as an output so that we can:
GPIO.output(4,GPIO.HIGH) # write a 1
time.sleep(0.025) # for 25 ms
GPIO.output(4,GPIO.LOW) # then write a 0
time.sleep(0.02) # for 20 ms.
# I assume that the preceding sequence is the method to get the DHT senso$

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change the pin to read$

for i in range(0,500): # 501 times
    data.append(GPIO.input(4))
    print (data)

