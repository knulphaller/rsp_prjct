# WebServer2.py

import serial
import time, sys
import datetime
from gsmmodem import *
import random
import sensors as s

APN = "nar"
HOST = "www.knulp.dx.am"
PORT = 80

SERIAL_PORT = "/dev/serial0"  # Raspberry Pi 2

print "Resetting modem..."
#print 'Powering on GSM modem'
#togglePower()
resetModem()
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
if not isReady(ser):
    print "Modem not ready."
#    print "Trying to powering on modem..."
#    togglePower()
#    ser=ser
#    sys.exit(0)

print "Connecting to GSM net..."
connectGSM(ser, APN)
while True:
    startTime = time.time()
    device_id=001234532
    sensor_name='obd'
    sensor_code='c342'
    sensor_value=250
    date_time=startTime
    additional_notes='testing from pi gsm_'
    additional_notes = additional_notes.replace(" ", "%20") # don't use space in url
    print "data: ",device_id, sensor_name, sensor_code, sensor_value, date_time, additional_notes
    a='Salam bexruz nedjesen?'
    reply = connectTCP(ser, HOST, PORT)
    if "CONNECT OK" not in reply:
        print "Connection failed"
        sys.exit(0)
	print "Sending HTTP request..."
    sendHTTPRequest(ser, HOST, "/insert.php?device_id=" + str(device_id) + "&sensor_name=" + sensor_name + "&sensor_code=" + sensor_code +
	"&sensor_value=" + str(sensor_value) + "&date_time=" + str(date_time) + "&additional_notes=" + additional_notes) 
    print "Closing. Waiting for next transfer"
    closeTCP(ser)
    isRunning = True
    while time.time() - startTime < 60:
      time.sleep(0.1)


