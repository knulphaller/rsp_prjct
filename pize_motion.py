from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(24)

while True:
	pir.when_motion = print('Motion detected')
	pir.when_no_motion = print('No motion')
pause()
