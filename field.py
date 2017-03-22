from image import Image
from sound import Sound
from scoreboard import Scoreboard

class Field:
	def __init__(self):
		self.ground_image_url = 'field.png'
		self.ground_image = Image(ground_image_url, 0, 0)
		scoreboard = Scoreboard()
	
	def move_ball(self, distance)