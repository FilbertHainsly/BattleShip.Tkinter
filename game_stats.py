from datetime import datetime

class Game_Stats:

	def __init__(self):
		#SCORE BOARD
		self.win = False #FLAG / SIGN
		self.score = 104
		self.steps = 0
		self.start = None
		self.finish = None

		self.set_start_time()
	
	def raise_steps(self):
		self.steps += 1
		self.score -= 4
	
	def reset_steps(self):
		self.steps = 0
		self.score = 104

	def current_time(self):
		time = datetime.now().time()
		current_time = (int(time.hour), int(time.minute), int(time.second))
		return current_time

	def set_start_time(self):
		self.start = self.current_time()
		print(self.start)

	def set_finish_time(self):
		self.finish = self.current_time()
		print(self.finish)