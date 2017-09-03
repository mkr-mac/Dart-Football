from field import Field
from gpio_controller import GPIO_Controller
from pygame.locals import *
import pygame, sys, os, time, threading

#Screen size constants
SCREENWIDTH = 720
SCREENHEIGHT = 480
FULLSCREEN = False

def check_quit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				quit()

def quit():
	pygame.quit()
	sys.exit()

def port_scan():
	global ports_on
	gp = GPIO_Controller(input_ports)
	ports_on = [11,11]

	while True:
		if not thread_stop:
			ports_on = gp.poll()

def thread_control():	
	if thread_stop:
		action_delay -= 1
		if action_delay <= 0:
			thread_stop = False

def check_input():
	action = None

	try:
		p = ports_on		
	except:
		p = [11,11]
		
	if p[0] < 10 and p[1] < 10:
		action = action_chart[p[0]][p[1]]
		print ("action = " + str(action))
		thread_stop = True
		time.sleep(.01)
		ports_on = []
		action_delay = 23
		break
	else:
		action = None
		
#Start Pygame
pygame.init()
FPS = 30
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")

#The GPIO ports in use by the Pi
input_ports = [4, 17, 9, 5, 13, 26, 21, 16, 12, 8]

#The action lookup chart
#Spots at [x][x] are unreachable		
action_chart = [['NA', 2, 3, 4, 5, 6, 7, 8, 9, 10],
				[-1, 'NA', -3, -4, -5, -6, -7, -8, -9, -10],
				['touchdown', 'fumble', 'NA', 'interception', 'penalty5', 'penalty5ldl', 'penalty10ldl', 'breakaway2', 'breakaway3', 0],
				['yellow', 0, 0, 'NA', 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 'NA', 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 'NA', 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 'NA', 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 'NA', 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0 , 'NA', 0],
				['yesgood', 'nonotgood', 'kick', 'punt', 'offboard', 'undo', 0, 0, 0, 'NA']]

#The playing field			
field = Field()
#A buffer so the
action_delay = 0

#Threading for Port Scanner
thread_stop = False
t = threading.Thread(target=port_scan, args = ())
t.daemon = True
t.start()

#Draw once to get started!
field.draw(DS)

#Main Loop
while True:
	#Look to see if we pushed a button to quit
	check_quit()
	#Look through the inputs for Actions
	check_input()
	#Controls whether the input scanner is going
	thread_control()
	
	#Update the screen and logic if we had an action
	if not (action == None):
		field.update(action)
		field.draw(DS)
	
	#bLIT
	pygame.display.update()
	fpsClock.tick(FPS)
	
#You shouln't be here... But just in case-
quit()
