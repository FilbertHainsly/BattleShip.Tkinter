import json

class Config:

	def __init__(self):

		self.app_title = "Battleship" 

		#GAME CONFIG
		self.row = 5
		self.column = 5

		#WINDOW CONFIG
		base = 100
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side+150}+450+0"

		#IMAGE PATH
		self.init_img_btn = "img/regular.png"
		self.final_img_btn = "img/wrong.jfif"
		self.win_img_btn = "img/win.jfif"
		self.logo_path = "img/logo.jpg"

		#JSON PATH
		self.json_path = "json/leaderboard.json"
		self.users_path = "json/users.json"

	def load_data(self):
		with open(self.json_path, "r") as json_data:
			data = json.load(json_data)
		return data

	def load_data_user(self):
		with open(self.users_path, "r") as json_data:
			data = json.load(json_data)
		return data

	def save_data(self, data):
		with open(self.json_path, 'w') as json_data:
			json.dump(data, json_data)

	def save_data_user(self, data):
		with open(self.users_path, 'w') as json_data:
			json.dump(data, json_data)

	def login(self, username, password):
		users = self.load_data_user()
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False


