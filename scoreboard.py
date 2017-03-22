from text import Text

class Scoreboard:
	def __init__(self):
		self.font = 'advanced_led_board-7.ttf'
		self.board_image = Image('board.png', 0, 0)
		
		self.home_score = 0
		self.home_score_text = Text(str(self.home_score), 0, 0, self.font, 54, (255,255,255))
		
		self.away_score = 0
		self.away_score_text = Text(str(self.away_score), 100, 0, self.font, 54, (255,255,255))
		
		self.yardline = 40
		self.yardline_text = Text(str(self.yardline), 0, 100, self.font, 54, (255,255,255))
		
		self.first_down_yardline = 50
		self.first_down_to_go = 10
		self.first_down_text = Text(str(self.first_down_to_go), 200, 100, self.font, 54, (255,255,255))
		
		self.down = 1
		self.down_text = Text(str(self.down), 100, 100, self.font, 54, (255,255,255))
		
		self.half = 1
		self.half_text = Text(str(self.half), 100, 200, self.font, 54, (255,255,255))
		
		self.possession = 'home'
		self.possession_indicator = Image('possession_indicator.png', 200, 200)
		self.home_init_dir = 'right'
		
		self.objects_to_draw = [self.board_image, self.home_score_text, 
							self.away_score_text, self.yardline_text, self.down_text,
							self.first_down_text, self.possession_indicator]
								
	def draw(self, DS):
		for o in objects_to_draw:
			o.draw(DS)
	
	def move_yards(self, gain):
		if self.home_init_dir = 'left':
			gain = -gain
		if self.half = 2:
			gain = -gain
		if self.possession = 'away'
			gain = -gain
			
		yardline += gain
		
		if yardline >= 100 or yardline <= 0:
			__score()
		else:
			__check_first_down()
			yardline_text.set_text(str(yardline))
			
	def __score(self):
		
		
		pass
	
	def __check_first_down(self):
		pass