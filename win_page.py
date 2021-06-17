import tkinter as tk

class WinPage(tk.Frame):
	def __init__(self, parent, Game):
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg = "light blue")
		
		self.grid(row = 0, column = 0, sticky = "nsew")
		parent.grid_columnconfigure(0, weight = 1)
		parent.grid_rowconfigure(0, weight = 1)

		self.main_frame = tk.Frame(self, height = self.config.side + 150, width = self.config.side, bg = 'light blue')
		self.main_frame.pack(expand = True)

		self.congrats_msg01 = tk.Label(self.main_frame, text = "CONGRATULATIONS", font = ("Arial", 32, "bold"), bg = "light blue", fg = "purple")
		self.congrats_msg01.pack(fill = "x")

		self.congrats_msg02 = tk.Label(self.main_frame, text = "YOU WIN !!", font = ("Arial", 32, "bold"), bg = "light blue", fg = "purple")
		self.congrats_msg02.pack(fill = 'x')

		self.attempts_msg = tk.Label(self.main_frame, text = f"Attempts = {self.game.game_stats.steps}", font = ("Arial", 18, "bold"), bg = "light blue", fg = "purple")
		self.attempts_msg.pack(fill = "x")

		self.score_msg = tk.Label(self.main_frame, text = f"Score = {self.game.game_stats.score}", font = ("Arial", 18, "bold"), bg = "light blue", fg = "purple")
		self.score_msg.pack(fill = "x")

		self.try_again = tk.Button(self.main_frame, text = "Play Again", font = ("Arial", 18, 'bold'), command = self.game.play_again, bg = "blue", fg = "white")
		self.try_again.pack(fill = 'x')

