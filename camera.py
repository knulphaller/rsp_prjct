import picamera
from time import *
timestamp = strftime("%Y%m%d-%H%M%S")
camera = picamera.PiCamera()
while True:
	timestamp = strftime("%Y%m%d%H%M%S")
	camera.start_recording('mediafiles/video%s.h264' %timestamp)
	sleep(5)
	camera.stop_recording()
	camera.capture('mediafiles/image%s.jpg' %timestamp)
