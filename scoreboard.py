from text import Text
from image import Image

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
	
	def move_yards(self, gain):
		if self.home_init_dir == 'left':
			gain = -gain
		if self.half == 2:
			gain = -gain
		if self.possession == 'away':
			gain = -gain
			
		yardline += gain
		
		if yardline >= 100 or yardline <= 0:
			score()
		else:
			check_first_down()
			yardline_text.set_text(str(yardline))
			
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
