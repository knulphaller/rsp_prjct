# WebServer1.py

import socket 
import time
import math

host = "www.knulp.dx.am"
port = 80


startTime = time.time()
device_id=001234532
sensor_name='obd'
sensor_code='c342'
sensor_value=250
date_time=startTime
additional_notes='testing from pi'
additional_notes = additional_notes.replace(" ", "%20") # don't use space in url
print "data: ",device_id, sensor_name, sensor_code, sensor_value, date_time, additional_notes
print "Sending HTTP request..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host , port))
request = "GET /insert.php?device_id=" + str(device_id) + "&sensor_name=" + sensor_name + "&sensor_code=" + sensor_code + "&sensor_value=" + str(sensor_value) + "&date_time=" + str(date_time) + "&additional_notes=" + additional_notes + \
            " HTTP/1.1\r\nHost: " + host + "\r\n\r\n" 
s.send(request)
s.shutdown(1)
s.close()
time.sleep(5)
print "Done"

