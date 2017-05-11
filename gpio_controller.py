import RPi.GPIO as GPIO

##This looks at the Raspberry Pi's GPIO ports for inputs.
class GPIO_Controller:
	def __init__(self, input_ports):
		self.input_ports = input_ports
		GPIO.setmode(GPIO.BCM)
		self.range_nine = range(9)
		self.range_ten = range(10)
		for port in input_ports:
			GPIO.setup(port, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		
	def poll(self):
		ports_on = []
		
		#Charlieplex Scanning, only needs 10 ports
		for i in self.range_ten:
			GPIO.setup(self.input_ports[i], GPIO.OUT, initial=GPIO.LOW)
			for j in range_ten:
				try:
					if (not i == j) and (not GPIO.input(j)):
						ports_on = [i, j]
				except:
					print ("Could not get input")
		"""
		#For 19 input port scanning

		for port in self.input_ports:
			try:
				if GPIO.input(port):
					ports_on += [self.input_ports.index(port)]
			except:
				pass

		"""
		print ports_on		
		return ports_on
		