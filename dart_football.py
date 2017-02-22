"""Dart Football for the Custom Electronic Board"""
"""Mickey McCargish - 2017"""

import sys, pygame, random, os
from sound import Sound
from image import Image
from text import Text

def quit():
	pygame.quit()
	sys.exit()

def draw(DS, scene):
	for obj in scene:
		obj.draw(DS)
	pygame.display.update()

#Screen size constants
SCREENWIDTH = 1080
SCREENHEIGHT = 1620
FULLSCREEN = False
led_font = 'advanced_led_board-7.ttf'

#Start Pygame
pygame.init()
FPS = 60
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")
	
"""Initializing Variables"""
#Team scores
home_score = 0
away_score = 0
#Current yardline
yardline = 20
#Posession indicator
home_team_has_ball = False
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
background = Image('./Football_files/Jeilm8H.png', 0, 0)
entry_text = Text("0", 30, 170, led_font, 165, (255,255,255))
line_of_scrimmage = Image('./Football_files/los.png', 88, 462)
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

base_scene = [
				background, entry_text, line_of_scrimmage, first_down_line, posession_football,
				touchdown_button, kick_button, punt_button, undo_button, fumble_button,
				interception_button, penalty_button, breakaway_button, yard_entry_button, yellow_button
				]

current_scene = base_scene

draw(DS, current_scene)

mouseclicked = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouseclicked = True
		elif event.type == pygame.MOUSEBUTTONUP:
			mouseclicked = False

	if mouseclicked == True:
			for obj in current_scene:
				if obj.clickable and obj.checkclick(mousex, mousey):
					action = obj.action
					if action == 'penalty':
						quit()
					entry_text.set_text(action)
					draw(DS, current_scene)
				