from image import Image
from sound import Sound
from scoreboard import Scoreboard

##This class mostly exists for  A E S T E T I C  reasons
##Like cute animations, or maybe full-fledged gameplay playback.
class Field:
	def __init__(self):
		self.ground_image_url = 'field.png'
		self.ground_image = Image(self.ground_image_url, 0, 0)
		self.scoreboard = Scoreboard()
		self.drawables = [self.ground_image, self.scoreboard]
		self.game_history = []
		self.save_number = 0
			
	def draw(self, DS):
		for d in self.drawables:
			d.draw(DS)
		
		self.scoreboard.draw(DS)
			
	def update(self, action):
		if not action == None:
			self.game_history.append(self.scoreboard)
			self.save_number+=1

			if isinstance(action, int):
				self.scoreboard.move_ball(action)
			elif isinstance(action, str):
				self.get_action(action)

		self.scoreboard.update()
		
	def undo(self):
		if save_number > 0:
			self.save_number -= 1
			self.scoreboard = self.game_history[self.save_number]
		
	def get_action(self, a):
		#a is for action, which poems are hard
		if a == 'touchdown':
			self.scoreboard.touchdown()
		elif a == 'interception':
			self.scoreboard.interception()
		elif a == 'fumble':
			self.scoreboard.fumble()
		elif a == 'yellow':
			self.scoreboard.yellow()
		elif a == 'penalty5':
			self.scoreboard.penalty(5)
		elif a == 'penalty5LDL':
			self.scoreboard.low_dart_penalty(5)
		elif a == 'penalty10LDL':
			self.scoreboard.low_dart_penalty(10)
		elif a == 'breakaway2':
			self.scoreboard.breakaway(2)
		elif a == 'breakaway3':
			self.scoreboard.breakaway(3)
		elif a == 'punt':
			self.scoreboard.punt()
		elif a == 'kick':
			self.scoreboard.kick()
		elif a == 'offboard':
			self.scoreboard.offboard()
		elif a == 'yesgood':
			self.scoreboard.yes_good()
		elif a == 'nonotgood':
			self.scoreboard.no_notgood()
		elif a == 'undo':
			self.undo()
			