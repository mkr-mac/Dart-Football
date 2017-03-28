from field import Field
#from gpio_controller import GPIO_Controller
from pygame.locals import *
#import RPi.GPIO as GPIO
import pygame, sys, os, threading

#Screen size constants
SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False
led_font = 'advanced_led_board-7.ttf'
current_milli_time = lambda: int(round(time.time() * 1000))

def quit():
	pygame.quit()
	sys.exit()
	
def port_scan():
		for port in input_ports:
			pass
			#if GPIO.input(port):
				#ports_on += [input_ports.index(port)]
#Start Pygame
pygame.init()
FPS = 30
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")

input_ports = [18, 23, 24, 25, 8, 7, 12, 16, 20, 21,
				4, 17, 27, 11, 5, 6, 13, 19, 26]
				
action_chart = [[1, 5, 10, 0, 0, 0, 0, 0, 0, 0],
				['yellow', -1, -5, 0, 0, 0, 0, 0, 0, 0],
				['touchdown', 'fumble', 'interception', 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0 ,0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
				
field = Field()
#gpio_controller = GPIO_Controller(input_ports)
exit = False
poll_cooldown = 0
i=0
ports_on = []

t = threading.Thread(target=port_scan, args = ())
t.daemon = True
t.start()

while not exit:
	#this needs to be in a separate thread
	#active_ports = gpio_controller.poll()
	action = None
	#This needs to look at more than the first 2 entries.
	"""
	for n in range(0, len(ports_on)-1):
		if not ports_on[n] == 0 and ports_on[n] < 10 and ports_on[n+1] >=10 and ports_on[n+1] < 19:
			action = action_chart[ports_on[n]][ports_on[n+1]-10]
		else:
			action = None
	"""
	
	ports_on = []
	
	field.update(action)
	field.draw(DS)
	
	pygame.display.update()
	fpsClock.tick(FPS)
	if i < 90:
		i+=1
	else:
		exit = True
	
quit()
