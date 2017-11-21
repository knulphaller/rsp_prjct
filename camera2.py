import picamera
import os
from time import *
timestamp = strftime("%Y%m%d-%H%M%S")
camera = picamera.PiCamera()
os.chdir("mediafiles/")
while True:
	timestamp = strftime("%Y%m%d%H%M%S")
	camera.start_recording('video%s.h264' %timestamp)
	sleep(5)
	camera.stop_recording()
	print("Video recorded! Duration: 5s")
	camera.capture('image%s.jpg' %timestamp)
	print("Image captured!")
	# dele files part
#	os.chdir('mediafiles/')  # Change this path to yours
#	p = os.getcwd()
	file_list = os.listdir('.')
	sorted_list = sorted(file_list, key=os.path.getmtime)
	# If file count more than 20 keep last 20 (this parameter can take from config.ini file )
	if len(sorted_list) > 50:
		for i in range(0, len(sorted_list) - 50):
			os.remove(sorted_list[i])
