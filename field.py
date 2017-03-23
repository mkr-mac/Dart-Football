from image import Image
from sound import Sound
from scoreboard import Scoreboard

class Field:
	def __init__(self):
		self.ground_image_url = 'field.png'
		self.ground_image = Image(ground_image_url, 0, 0)
		scoreboard = Scoreboard()
		drawables = [self.ground_image]
		
	def move_ball(self, distance):
		#this is one way of moving the ball
		pass
		
	def update(self, action):
		if not action == 0:
			pass
		if isinstance(action, int):
			move_ball(action)
		elif isinstance(action, str):
			pass
			
	def draw(self, DS):
		for d in self.drawables:
			d.draw(DS)
		scoreboard.draw(DS)
		