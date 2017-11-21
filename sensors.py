from ConfigParser import SafeConfigParser
'''
def pir_info():
	import time
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO_PIR = cfg.pir.pin
	print ("PIR Module Holding Time Test (CTRL-C to exit)")
	# Set pin as input
	GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
	Current_State  = 0
	Previous_State = 0
	# Loop until PIR output is 0
	while GPIO.input(GPIO_PIR)==1:
		Current_State  = 0
		print ("  Ready")
	# Loop until users quits with CTRL-C
	while True :
		# Read PIR state
		Current_State = GPIO.input(GPIO_PIR)
		if Current_State==1 and Previous_State==0:
			# PIR is triggered
			start_time=time.time()
			print ("  Motion detected!")
			# Record previous state
			Previous_State=1
		elif Current_State==0 and Previous_State==1:
			# PIR has returned to ready state
			stop_time=time.time()
			print ("  Ready ")
			elapsed_time=int(stop_time-start_time)
			print (" (Elapsed time : " + str(elapsed_time) + " secs)")
			Previous_State=0
		# Reset GPIO settings
		GPIO.cleanup()

def lightsensor():
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

def fire():
	import RPi.GPIO as GPIO

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.IN)

	while GPIO.input(4) ==1:
		print ('Yangin')

	while GPIO.input(4) ==0:
		print ('Yangin sonub')

def distance():
	import RPi.GPIO as GPIO
	import time
	GPIO.setmode(GPIO.BCM)

	TRIG = 23 
	ECHO = 24

	print("Distance Measurement In Progress")

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print("Waiting For Sensor To Settle")
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print("Distance:",distance,"cm")
	GPIO.cleanup()

def celcius():
	from gpiozero import MCP3008
	from time import sleep
	for value in gen:
		yield (value * 3.3 - 0.5) * 100
	
	adc = MCP3008(channel=1)
	
	for temp in convert_temp(adc.values):
		print('The temperature is', temp, 'C')
		sleep(1)

'''
def test_data(a,b,c,d):
	a=100
	b=200
	c=300
	parser = SafeConfigParser()
	parser.read('config.ini')
	d = float(parser.get('moist','time')) * 100
	return a,b,c,d
	#print(a,b,c)
#print(test_data())

