from text import Text
from image import Image

##Keeps track of the game and displays its properties.
class Scoreboard:
	def __init__(self):
		self.font = 'scoreboardfont.ttf'
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
		self.ldl_holder = 0
		
		self.home_name = Text("HOME", 24, 32, self.font, 24, (255,255,255))
		self.away_name = Text("AWAY", 382, 32, self.font, 24, (255,255,255))
		self.home_score_text = Text(str(self.home_score), 45, 95, self.font, 36, (255,255,255))
		self.away_score_text = Text(str(self.away_score), 425, 95, self.font, 36, (255,255,255))
		self.down_and_to_go = Text(str(self.down) + "RD & " + str(self.yardline), 170, 210, self.font, 24, (0,0,0))
		self.half_text = Text(str(self.half)+"ST", 222, 120, self.font, 24, (255,255,255))
		self.possession_indicator = Image('possession_indicator.png', 225, 44)
		
		self.drawables = [self.board_image, self.home_name, self.away_name,  
							self.home_score_text, self.away_score_text, self.down_and_to_go,
							self.half_text, self.possession_indicator]
	
	def move_ball(self, g):
		self.cooldown -= 1
		gain = self.get_gain(g)
		pos_gain = self.get_gain(abs(g))
		
		s = self.game_state
		if s == 'normal':
			self.yardline += gain
			self.first_down_to_go -= g
			print (self.yardline)
			self.down += 1
			if self.yardline >= 100 or self.yardline <= 0:
				self.score(gain)
			else:
				if self.check_first_down(gain):
					self.first_down()
				
			if self.down > 4:
				self.turnover()
				self.first_down()
				
		elif s == 'breakaway':
			self.yardline += pos_gain
			if self.yardline >= 100 or self.yardline <= 0:
				self.score(gain)
			elif not self.cooldown:
				if self.check_first_down(gain):
					self.first_down()
				else:
					down += 1
					if self.down > 4:
						self.turnover()
						self.first_down()
				
		elif s == 'punt':
			if pos_gain > 5:
				self.yardline += pos_gain
			else:
				self.yardline += 2*pos_gain
				
			if self.yardline >= 100:
				self.yardline = 80
				self.game_state = 'normal'
				self.cooldown = -1
			elif self.yardline <= 0:
				self.yardline = 20
				self.game_state = 'normal'
				self.cooldown = -1
				
		elif s == 'puntreturn':
			self.yardline += pos_gain
			if self.yardline >= 100 or self.yardline <= 0:
				self.score(gain)
			self.first_down()
				
				
		elif s == 'ldlpenalty':
			if self.cooldown:
				self.ldl_holder = g
			else:
				if g > self.ldl_holder:
					self.game_state = 'normal'
					self.down -= 1
					self.move_ball(10)
				elif g < self.ldl_holder:
					self.game_state = 'normal'
					self.down -= 1
					self.move_ball(-10)
				else:
					self.cooldown = 2
					
		if not self.cooldown:
			if self.game_state == 'punt':
				self.game_state == 'puntreturn'
				self.turnover()
			else:
				self.game_state == 'normal'	

	def get_gain(self, gain):
		if self.home_init_dir == 'left':
			gain = -gain
		if self.half == 2:
			gain = -gain
		if self.possession == 'away':
			gain = -gain
		return gain
		
	def score(self, gain):
		if self.yardline >= 100:
			if gain > 0:
				if self.possession == 'home':
					self.home_score += 6
				elif self.possession == 'away':
					self.away_score += 6
				self.yardline = 98
				self.game_state = 'PAT'
			else:
				if self.possession == 'home':
					self.away_score += 2
				elif self.possession == 'away':
					self.home_score += 2
				self.yardline = 35
				self.turnover()
				self.first_down()
		if self.yardline <= 0:
			if gain < 0:
				if self.possession == 'home':
					self.home_score += 6
				elif self.possession == 'away':
					self.away_score += 6
				self.yardline = 2
				self.game_state = 'PAT'
			else:
				if self.possession == 'home':
					self.away_score += 2
				elif self.possession == 'away':
					self.home_score += 2
				self.yardline = 65
				self.turnover()
				self.first_down()
	
	def check_first_down(self, gain):
		if self.yardline >= self.first_down_yardline and gain > 0:
			return True
		elif self.yardline <= self.first_down_yardline and gain < 0:
			return True
		else:
			return False
		
	def first_down(self):
		self.down = 1
		if self.get_gain(1) == 1:
			if self.yardline + 10 >= 100:
				self.first_down_to_go = 100-self.yardline
				self.first_down_yardline = 100
			else:
				self.first_down_to_go = 10
				self.first_down_yardline = self.yardline + 10
		else:
			if self.yardline - 10 <= 0:
				self.first_down_to_go = self.yardline
				self.first_down_yardline = 0
			else:
				self.first_down_to_go = 10
				self.first_down_yardline = self.yardline - 10
			
		
	def turnover(self):
		if self.possession == 'home':
			self.possession = 'away'
		else:
			self.possession = 'home'
			
	def punt(self):
		if self.game_state == 'normal':
			#punt.wmv
			self.game_state = 'punt'
			self.cooldown = 3
		
	def kick(self):
		if self.game_state == 'normal':
			self.game_state = 'kick'
			
	def yes_good(self):
		if self.game_state == 'kick':
			#kick_is_up_and_its_good.avi
			if possession == 'home':
				self.home_score += 3
			else:
				self.away_score += 3
				
			if self.get_gain(1) == 1:
				self.yardline = 25
			else:
				self.yardline = 75
			self.turnover()
			self.game_state = 'normal'
			
		elif self.game_state == 'XP':
			#kick_is_up_and_its_good.avi
			if possession == 'home':
				self.home_score += 1
			else:
				self.away_score += 1
			
			if self.get_gain(1) == 1:
				self.yardline = 25
			else:
				self.yardline = 75
			self.turnover()
			self.game_state = 'normal'
		
	def no_notgood(self):
		if self.game_state == 'kick':
			#nogood.mp4
			self.turnover()
			self.game_state = 'normal'
		elif self.game_state == 'XP':
			#nogood.mp4
			if self.get_gain(1) == 1:
				self.yardline = 25
			else:
				self.yardline = 75
			self.turnover()
			self.game_state = 'normal'
	
	def interception(self):
		self.turnover()
		gain = -20
		if self.home_init_dir == 'left':
			gain = -gain
		if self.half == 2:
			gain = -gain
		if self.possession == 'away':
			gain = -gain
			
		if self.yardline + gain >= 100:
			self.yardline = 80
		elif self.yardline + gain <= 0:
			self.yardline = 20
			
		self.first_down()
		
	def fumble(self):
		self.turnover()
		self.first_down()
	
	def touchdown(self):
		if self.game_state == 'punt':
			self.move_ball(50)
		elif not self.game_state == 'kick' or not 'XP':
			self.move_ball(100)
			
	def yellow(self):
		if self.game_state == 'normal' or self.game_state == 'breakaway' or self.game_state == 'ldlpenalty':
			self.move_ball(0)
		elif self.game_state == 'punt':
			self.move_ball(10)
		
	def offboard(self):
		if self.game_state == 'normal' or self.game_state == 'breakaway' or self.game_state == 'punt':
			self.move_ball(0)
		elif self.game_state == 'ldlpenalty':
			self.move_ball(-100)
		
	def breakaway(self, leng):
		if not self.game_state == 'kick' or not self.game_state == 'XP':
			self.game_state = 'breakaway'
			self.cooldown = leng

	def penalty(self, leng):
		if not self.game_state == 'kick' or not self.game_state == 'XP':
			self.down -= 1
			self.move_ball(-leng)
		
	def low_dart_penalty(self, leng):
		if self.game_state == 'normal':
			self.cooldown = 2
			self.game_state = 'ldlpenalty'
		elif self.game_state == 'breakaway' or self.game_state == 'puntreturn' or self.game_state == 'ldlpenalty':
			self.move_ball(0)
		elif self.game_state == 'punt':
			self.move_ball (10)
		
	def update(self):
		self.home_name = Text(str("HOME"), 24, 32, self.font, 48, (255,255,255))
		self.away_name = Text(str("AWAY"), 382, 32, self.font, 48, (255,255,255))
		self.home_score_text = Text(str(self.home_score), 45, 190, self.font, 36, (255,255,255))
		self.away_score_text = Text(str(self.away_score), 425, 190, self.font, 36, (255,255,255))
		if self.game_state == "PAT":
			self.down_and_to_go = Text("POINT AFTER ATTEMPT", 170, 210, self.font, 24, (0,0,0))
		elif self.down == 1:
			self.down_and_to_go = Text(str(self.down) + " ST & " + str(self.first_down_to_go), 170, 210, self.font, 24, (0,0,0))
		elif self.down == 2:
			self.down_and_to_go = Text(str(self.down) + " ND & " + str(self.first_down_to_go), 170, 210, self.font, 24, (0,0,0))
		elif self.down == 3:
			self.down_and_to_go = Text(str(self.down) + " RD & " + str(self.first_down_to_go), 170, 210, self.font, 24, (0,0,0))
		elif self.down == 4:
			self.down_and_to_go = Text(str(self.down) + " TH & " + str(self.first_down_to_go), 170, 210, self.font, 24, (0,0,0))
		else:
			self.down_and_to_go = Text(str(self.down) + " OH NO & " + str(self.first_down_to_go), 170, 210, self.font, 24, (0,0,0))

		if self.half == 1:
			self.half_text = Text(str(self.half)+" ST", 222, 120, self.font, 48, (255,255,255))
		elif self.half == 2:
			self.half_text = Text(str(self.half)+" ND", 222, 120, self.font, 48, (255,255,255))
		else:
			self.half_text = Text(str(self.half)+" NO", 222, 120, self.font, 48, (255,255,255))


		self.possession_indicator = Image('possession_indicator.png', 225, 44)
		self.drawables = [self.board_image, self.home_name, self.away_name,  
					self.home_score_text, self.away_score_text, self.down_and_to_go,
					self.half_text, self.possession_indicator]
		
	def draw(self, DS):
		for o in self.drawables:
			o.draw(DS)
		
	