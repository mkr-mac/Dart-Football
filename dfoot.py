from field import Field
#from gpio_controller import GPIO_Controller
from pygame.locals import *
#import RPi.GPIO as GPIO
import pygame, sys, os, time, threading

#Screen size constants
SCREENWIDTH = 720
SCREENHEIGHT = 480
FULLSCREEN = True

def quit():
	pygame.quit()
	sys.exit()

def port_scan():
	global ports_on
	ports_on = [0]*105
	b=0
	#Test Scan plz ignore
	while True:
		if not thread_stop:
			ports_on[b] = 0
			ports_on[b+1] = 10
			b+=2
			if b>100:
				b=0
						
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
				
action_chart = [[1, 4, 10, 0, 0, 0, 0, 0, 0, 0],
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
i = 0
action_delay = 0

thread_stop = False
t = threading.Thread(target=port_scan, args = ())
t.daemon = True
t.start()

while not exit:
	action = None

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				quit()

	try:
		p = ports_on		
	except:
		p = []
		
	for n in range(0, len(p)-1):
		if p[n] < 10 and p[n+1] >= 10 and p[n+1] < 19:
			action = action_chart[p[n]][p[n+1]-10]
			print ("action = " + str(action))
			thread_stop = True
			time.sleep(.01)
			ports_on = [0]*105
			action_delay = 23
			break
		else:
			action = None

	if thread_stop:
		action_delay -= 1
		if action_delay <= 0:
			thread_stop = False
	
	if not (action == None):
		field.update(action)
		field.draw(DS)
	
	pygame.display.update()
	fpsClock.tick(FPS)

	#TESTING! Closes after some time automatically
	if i < 750:
		i+=1
	else:
		exit = True
	
quit()
