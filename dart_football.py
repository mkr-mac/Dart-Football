"""Dart Football for the Custom Electronic Board"""
"""Mickey McCargish - 2017"""

import sys, pygame, random, os, time
from sound import Sound
from image import Image
from text import Text
import RPi.GPIO as GPIO

def quit():
	pygame.quit()
	sys.exit()

def draw(DS, scene):
	for obj in scene:
		obj.draw(DS)
	pygame.display.update()

def move_ball(yards, team_with_posession, home_team_initial_direction, half):
	move = yards
	if team_with_posession == 'away':
		move = -move
	return move

def button_lookup(ports, input_ports, input_chart):
	if len(ports) == 2:
		port_1 = ports[0]
		port_2 = ports[1]
		return input_chart[input_ports.index(port_1) + (input_ports.index(port_2)-10)*10]
	return False

#Screen size constants
SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False
led_font = 'advanced_led_board-7.ttf'
current_milli_time = lambda: int(round(time.time() * 1000))

#Start Pygame
pygame.init()
FPS = 60
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")

GPIO.setmode(GPIO.BCM)

gpio_input_ports = [18, 23, 24, 25, 8, 7, 12, 16, 20, 21,
			4, 17, 27, 11, 5, 6, 13, 19, 26]
					
for port in gpio_input_ports:
	GPIO.setup(port, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	
input_chart = [ 1, 5, 10, 0, 0, 0, 0, 0, 0, 0,
				'yellow', -1, -5, 0, 0, 0, 0, 0, 0, 0,
				'touchdown', 'fumble', 'interception', 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0 ,0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
				
"""Initializing Variables"""
#Team scores
home_score = 0
away_score = 0
#Current yardline
yardline = 20
#Posession indicator
team_with_posession = 'home'
home_team_initial_direction = 'right'
##Images Here????



#yards gained on play
yards_gained = 0
#Displayed yardline (1-50)
posted_yardline = 0
#Yards required for a first down
first_down_to_go = 0
first_down_yard_line = 0
#Current down
down = 0
#Used to indicate a "Breakaway" Situation
breakaway_flag = 0
#Used to indicate a "Punt" Situation
punt_flag = 0
#Used to indicate a "Kick" Situation (No regular inputs)
kick_flag = 0
#The game is played in two halves
half = 1
#Team names
home_team_name = ""
away_team_name = ""

#Final score to play to
score_to_get = 0

##IMAGES!!!!!?!?!?!?!
background = Image('./Football_files/Scoreboard_Small.png', 0, 0)
current_yard_text = Text(str(posted_yardline), 670, 175, led_font, 54, (255,255,255))
entry_text = Text("0", 0, 0, led_font, 20, (255,255,255))
"""line_of_scrimmage = Image('./Football_files/los.png', 88, 462)
first_down_line = Image('./Football_files/firstdown.png', 88, 462)
posession_football = Image('./Football_files/football.png', 380, 1319)
touchdown_button = Image('./Football_files/3W26Hwh.png', 405, 150, True, 'touchdown')
kick_button = Image('./Football_files/uom20MK.png', 405, 150, True, 'kick')
punt_button = Image('./Football_files/SIpq8WT.png', 705, 350, True, 'punt')
undo_button = Image('./Football_files/fsXCCYl.png', 900, 0, True, 'undo')
fumble_button = Image('./Football_files/aDCYIoN.png', 405, 250, True, 'fumble')
interception_button = Image('./Football_files/hoAMDVE.png', 705, 250, True, 'interception')
penalty_button = Image('./Football_files/penalty.png', 1005, 150, True, 'penalty')
breakaway_button = Image('./Football_files/breakaway.png', 330, 150, True, 'breakaway')
yard_entry_button = Image('./Football_files/yards.png', 20, 370, True, 'enter_yards')
yellow_button = Image('./Football_files/yellow.png', 405, 350, True, 'yellow')
miss_button = Image('./Football_files/offboard.png', 405, 350, True, 'offboard')
"""
base_scene = [background, entry_text, current_yard_text]
"""line_of_scrimmage, first_down_line, posession_football,
touchdown_button, kick_button, punt_button, undo_button, fumble_button,
interception_button, penalty_button, breakaway_button, yard_entry_button, yellow_button"""
				

current_scene = base_scene

draw(DS, current_scene)

button_recently_clicked = False
button_recently_clicked_time = 0

while True:
	ports_on = []
	action = False
	if not button_recently_clicked:
		for port in gpio_input_ports:
			if GPIO.input(port):
				ports_on += [port]
				
		action = button_lookup(ports_on, gpio_input_ports, input_chart)
	
	else:
		if current_milli_time() - button_recently_clicked_time > 600:
			button_recently_clicked = False
	
	if action != False:
		button_recently_clicked = True
		button_recently_clicked_time = current_milli_time()
		entry_text.set_text(str(action))
		if str(action).isdigit():
			move_ball(action, team_with_posession, home_team_initial_direction, half)
		if action == 'fumble':
			if team_with_posession == 'home':
				team_with_posession = 'away'
			else:
				team_with_posession = 'home'
		
		