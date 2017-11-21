import time
import RPi.GPIO as GPIO
import time 
import socket
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.88.237'
port = 5454
# Define GPIO to use on Pi
GPIO_PIR = 4
s.connect((host, port)) 
print ("PIR Module Holding Time Test (CTRL-C to exit)")
 
# Set pin as input
while True:
    GPIO.setup(GPIO_PIR,GPIO.IN) 
    print(GPIO.input(GPIO_PIR))
    time.sleep(0.5)
    if GPIO.input(GPIO_PIR)==1:
        s.sendall(b'Motion detected')
    else:
        s.sendall(b'No motion')
    #s.sendall(bytes(GPIO.input(GPIO_PIR)))

