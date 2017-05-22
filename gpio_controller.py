import RPi.GPIO as GPIO

##This looks at the Raspberry Pi's GPIO ports for inputs.
class GPIO_Controller:
	def __init__(self, input_ports):
		self.input_ports = input_ports
		GPIO.setmode(GPIO.BCM)
		#optimisation
		self.range_ten = range(10)
		for port in input_ports:
			#Pull up all the ports
			GPIO.setup(port, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		
	#Checks to see if a button is pressed
	def poll(self):
		b=0
		#Charlieplex Scanning, only needs squrt(N) ports
		for i in self.range_ten:
			#Drive each port to low
			GPIO.setup(self.input_ports[i], GPIO.OUT, initial=GPIO.LOW)
			#See what the effcts are on the other ports
			for j in self.range_ten:
				#We don't want it to be the same port as before
				if (not i == j):
					#See if the port was driven Low						
					if not GPIO.input(self.input_ports[j]):
						#reset the first port as input
						GPIO.setup(self.input_ports[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
						#these are the coordinates of the input!
						return [i, j]

			GPIO.setup(self.input_ports[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

		"""
		#For 19 input port scanning, Regular multiplexing

		for port in self.input_ports:
			try:
				if GPIO.input(port):
					ports_on += [self.input_ports.index(port)]
			except:
				pass

		return ports_on
		"""