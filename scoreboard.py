from text import Text

class Scoreboard:
	def __init__(self):
		self.font = 'advanced_led_board-7.ttf'
		self.board_image = Image('board.png', 0, 0)
		
		self.home_score = 0
		home_score_text_x = 0
		home_score_text_y = 0
		self.home_score_text = Text(str(self.home_score), self.home_score_text_x, self.home_score_text_y, self.font, 54, (255,255,255))
		
		self.away_score = 0
		away_score_text_x = 100
		away_score_text_y = 0
		self.away_score_text = Text(str(self.away_score), self.away_score_text_x, self.away_score_text_y, self.font, 54, (255,255,255))
		
		self.yardline = 40
		yardline_text_x = 0
		yardline_text_y = 100
		self.yardline_text = Text(str(self.yardline), self.yardline_text_x, self.yardline_text_y, self.font, 54, (255,255,255))
		
		self.down = 1
		down_x = 0
		down_y = 100
		self.down_text = Text(str(self.down), self.down_x, self.down_y, self.font, 54, (255,255,255))
		
		self.possession = 'home'
		possession_x = 0
		possession_y = 100
		self.possession_indicator = Image('possession_indicator.png', possession_x, possession_y)
		self.home_init_dir = 'right'
		
		self.objects_to_draw = [self.board_image, self.home_score_text, 
								self.away_score_text, self.yardline_text, self.down_text,
								possession_indicator]
								
	def draw(self, DS):
		for o in objects_to_draw:
			o.draw(DS)
	
	def move_yards(self, gain):
		if self.possession == 'home' and 
		