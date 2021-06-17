

class Player:

	def __init__(self, Game, name = "John"):
		self.game = Game
		self.name = name
		self.score = 104
		self.steps = 0

	def current_location(self, pos_x, pos_y):
		self.location = (pos_x, pos_y)

	def raise_steps(self):
		self.steps += 1
		self.score -= 4
		self.game.window.pages["board"].steps_taken.configure(text = f"Attempts = {self.steps}")
		self.game.window.pages["win_page"].attempts_msg.configure(text = f"Attempts = {self.steps}")
		self.game.window.pages["win_page"].score_msg.configure(text = f"Score = {self.score}")

	def reset_steps(self):
		self.steps = 0
		self.score = 104
		self.game.window.pages["board"].steps_taken.configure(text = f"Attempts = {self.steps}")
		self.game.window.pages["win_page"].attempts_msg.configure(text = f"Attempts = {self.steps}")
		self.game.window.pages["win_page"].score_msg.configure(text = f"Score = {self.score}")