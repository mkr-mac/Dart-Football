import RPi.GPIO as GPIO

##This looks at the Raspberry Pi's GPIO ports for inputs.
class GPIO_Controller:
	def __init__(self, input_ports):
		self.input_ports = input_ports
		GPIO.setmode(GPIO.BCM)
		for port in input_ports:
			GPIO.setup(port, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
		
	def poll(self):
		ports_on = []
		for port in input_ports:
			if GPIO.input(port):
				ports_on += [port]
		
		return ports_on