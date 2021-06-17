import tkinter as tk

from config import Config
from game_stats import Game_Stats
from board import Board
from ship import Ship
from player import Player
from win_page import WinPage
from login_page import LoginPage
from register_page import RegisterPage

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game  # battleship obj
		self.config = Game.config #config di battleship obj

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_winPage()
		self.create_board()
		self.creater_registerPage()
		self.create_loginPage()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

	def create_winPage(self):
		self.pages["win_page"] = WinPage(self.container, self.game)

	def create_loginPage(self):
		self.pages["login_page"] = LoginPage(self.container, self.game)

	def creater_registerPage(self):
		self.pages["register_page"] = RegisterPage(self.container, self.game)

class Battleship:

	def __init__(self):
		self.config = Config()

		self.loaded_data = self.config.load_data()
		self.loaded_users = self.config.load_data_user()

		self.game_stats = Game_Stats()
		self.window = Window(self)
		self.ship = Ship(self)

	def switch_page(self, page):
		self.window.pages[page].tkraise()

	def auth_login(self):
		username = self.window.pages['login_page'].var_username.get()
		password = self.window.pages['login_page'].var_password.get()

		granted = self.config.login(username, password)
		if granted:
			self.switch_page('board')
		else:
			self.window.pages['login_page'].false_msg.pack(pady= 5)
		self.player = Player(self, username)

	def login(self):
		self.username = self.window.pages['login_page'].var_username.get()
		self.switch_page("board")
		self.player = Player(self, self.username)

	def register(self):
		self.switch_page('register_page')

	def auth_register(self):
		username = self.window.pages['register_page'].var_username.get()
		password = self.window.pages['register_page'].var_password.get()
		confirmed_password = self.window.pages['register_page'].var_confirmPassword.get()

		if password == confirmed_password:
			self.loaded_users[username] = {
				"password" : password,
				"level" : "player"
			}
			self.switch_page("login_page")
			self.window.pages["login_page"].success_register.pack(pady = 3)
			self.config.save_data_user(self.loaded_users)
		else:
			self.window.pages["register_page"].error_msg.pack(pady = 3)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location

		if ship == player:
			self.game_stats.set_finish_time()
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		self.player.raise_steps()
		self.game_stats.raise_steps()
		win = self.check_answer()
		self.window.pages["board"].change_image_button(win, pos_x, pos_y)
		if win:
			print("You Win!!!")
			self.switch_page("win_page")
			self.save()

	def reset(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.window.pages["board"].button_board[i][j].configure(image = self.window.pages["board"].init_img_btn)
		self.player.reset_steps()
		self.game_stats.reset_steps()
		self.game_stats.set_start_time()
		self.ship.setup_location()

	def play_again(self):
		self.switch_page("board")
		self.reset()

	def save(self):
		if self.player.name in self.loaded_data:
			if self.player.score >= self.loaded_data[self.player.name]["Score"]:
				self.loaded_data[self.player.name] = {
					"Score" : self.game_stats.score,
					"Steps" : self.game_stats.steps,
					"Start" : f"{self.game_stats.start[0]}:{self.game_stats.start[1]}:{self.game_stats.start[2]}",
					"Finish" :  f"{self.game_stats.finish[0]}:{self.game_stats.finish[1]}:{self.game_stats.finish[2]}"
				}
			else:
				self.loaded_data[self.player.name] = {
					"Score" : self.loaded_data[self.player.name]["Score"],
					"Steps" : self.loaded_data[self.player.name]["Steps"],
					"Start" : self.loaded_data[self.player.name]["Start"],
					"Finish" : self.loaded_data[self.player.name]["Finish"]
				}
		else:
			self.loaded_data[self.player.name] = {
				"Score" : self.game_stats.score,
				"Steps" : self.game_stats.steps,
				"Start" : f"{self.game_stats.start[0]}:{self.game_stats.start[1]}:{self.game_stats.start[2]}",
				"Finish" :  f"{self.game_stats.finish[0]}:{self.game_stats.finish[1]}:{self.game_stats.finish[2]}"
			}
		self.config.save_data(self.loaded_data)

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()