from field import Field
from gpio_controller import GPIO_Controller
from pygame.locals import *
import pygame, sys, os, time, threading

#Screen size constants
SCREENWIDTH = 720
SCREENHEIGHT = 480
FULLSCREEN = False

def quit():
	pygame.quit()
	sys.exit()

def port_scan():
	global ports_on
	gp = GPIO_Controller(input_ports)
	ports_on = []

	while True:
		if not thread_stop:
			ports_on += gp.poll()
		
#Start Pygame
pygame.init()
FPS = 30
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")

input_ports = [4, 17, 27, 11, 5, 6, 13, 19, 26,
				18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
				
action_chart = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10],
				['touchdown', 'fumble', 'interception', 'penalty5', 'penalty5ldl', 'penalty10ldl', 'breakaway2', 'breakaway3', 0, 0],
				['yellow', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0 ,0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				['yesgood', 'nonotgood', 'kick', 'punt', 'offboard', 'undo', 0, 0, 0, 0]]
				
field = Field()

action_delay = 0

thread_stop = False
t = threading.Thread(target=port_scan, args = ())
t.daemon = True
t.start()

while True:
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
		if p[n] < 9 and p[n+1] >= 9 and p[n+1] < 19:
			action = action_chart[p[n]][p[n+1]-10]
			print ("action = " + str(action))
			thread_stop = True
			time.sleep(.01)
			ports_on = []
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

	
quit()
