from text import Text
from image import Image

##Keeps track of the game and displays its properties.
class Scoreboard:
	def __init__(self):
		self.font = 'advanced_led_board-7.ttf'
		self.board_image = Image('board.png', 0, 0)
		
		self.home_score = 0
		self.away_score = 0
		
		self.yardline = 40
		
		self.first_down_yardline = 50
		self.first_down_to_go = 10
		self.down = 1
		
		self.half = 1
		self.possession = 'home'
		self.home_init_dir = 'right'
		self.game_state = 'normal'
		self.cooldown = 0
		
		self.home_score_text = Text(str(self.home_score), 0, 0, self.font, 54, (255,255,255))
		self.away_score_text = Text(str(self.away_score), 100, 0, self.font, 54, (255,255,255))
		self.yardline_text = Text(str(self.yardline), 0, 100, self.font, 54, (255,255,255))
		self.first_down_text = Text(str(self.first_down_to_go), 200, 100, self.font, 54, (255,255,255))
		self.down_text = Text(str(self.down), 100, 100, self.font, 54, (255,255,255))
		self.half_text = Text(str(self.half), 100, 200, self.font, 54, (255,255,255))
		self.possession_indicator = Image('possession_indicator.png', 200, 200)
		
		self.drawables = [self.board_image, self.home_score_text, 
							self.away_score_text, self.yardline_text, self.down_text,
							self.first_down_text, self.possession_indicator]
	
	def move_ball(self, gain):
		self.cooldown -= 1
		
		if self.home_init_dir == 'left':
			gain = -gain
		if self.half == 2:
			gain = -gain
		if self.possession == 'away':
			gain = -gain
		
		if self.game_state == 'normal':
			self.yardline += gain
		
			if self.yardline >= 100 or self.yardline <= 0:
				score()
			else:
				check_first_down()
				
		elif self.game_state == 'breakaway':
			self.yardline += gain
			
			if self.yardline >= 100 or self.yardline <= 0:
				score()
			elif not self.cooldown:
				check_first_down()
				
		if not self.cooldown 
			if self.game_state == 'punt':
				self.game_state == 'puntreturn'
			else:
				self.game_state == 'normal'				
			
	def score(self):
		pass
	
	def check_first_down(self):
		pass
		
	def first_down(self):
		self.down = 1
		self.first_down_to_go = 10
		
	def turnover(self):
		if self.possession == 'home':
			self.possession = 'away'
		else:
			self.possession = 'home'
			
	def punt(self):
		if self.game_state == 'normal':
			self.game_state = 'punt'
			self.cooldown = 3
		
	def kick(self):
		if self.game_state == 'normal':
			self.game_state = 'kick'
	
	def interception(self):
		turnover()
		gain = -20
		if self.home_init_dir == 'left':
			gain = -gain
		if self.half == 2:
			gain = -gain
		if self.possession == 'away':
			gain = -gain
			
		if self.yardline += gain >= 100:
			self.yardline = 80
		elif self.yardline += gain <= 0:
			self.yardline = 20
			
		first_down()
		
	def fumble(self):
		turnover()
		first_down()
		
	def yellow(self):
		if self.game_state == 'normal' or self.game_state == 'breakaway' or self.game_state == 'ldlpenalty':
			move_ball(0)
		elif self.game_state == 'punt':
			move_ball(10)
		
	def offboard(self):
		if self.game_state == 'normal' or self.game_state == 'breakaway' or self.game_state == 'punt':
			move_ball(0):
		elif self.game_state == 'ldlpenalty':
			move_ball(-100):
		
	def breakaway(self, leng):
		self.game_state = 'breakaway'
		self.cooldown = leng

	def penalty(self, leng):
		pass
		
	def low_dart_penalty(self, leng):
		pass
		
	def update(self):
		self.home_score_text = Text(str(self.home_score), 0, 0, self.font, 54, (255,255,255))
		self.away_score_text = Text(str(self.away_score), 100, 0, self.font, 54, (255,255,255))
		self.yardline_text = Text(str(self.yardline), 0, 100, self.font, 54, (255,255,255))
		self.first_down_text = Text(str(self.first_down_to_go), 200, 100, self.font, 54, (255,255,255))
		self.down_text = Text(str(self.down), 100, 100, self.font, 54, (255,255,255))
		self.half_text = Text(str(self.half), 100, 200, self.font, 54, (255,255,255))
		self.possession_indicator = Image('possession_indicator.png', 200, 200)
		
	def draw(self, DS):
		for o in self.drawables:
			o.draw(DS)
		
	