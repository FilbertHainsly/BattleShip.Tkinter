import tkinter as tk
from PIL import Image, ImageTk

class Board(tk.Frame):

	def __init__(self, parent, Game):

		self.game = Game
		self.config = Game.config

		#CONFIG FRAME
		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		#CONFIG BUTTON
		#self.buttonPixel = tk.PhotoImage(width=1, height=1)

		self.create_mainframe()
		self.create_subframe()
		self.update_board()

	def update_board(self):
		self.create_board()
		self.show_board()
		self.create_button_board()
		self.show_button_board()

	def create_mainframe(self):
		self.mainframe = tk.Frame(self, height=(self.config.side+150), width=self.config.side, bg="black")
		self.mainframe.pack(expand=True)

		self.gameTitle = tk.Label(self.mainframe, font = ("Arial", 36, "bold"), text = "BATTLESHIP", fg = "white", bg = "black")
		self.gameTitle.pack(side = 'top', fill = "x")

	def create_board(self):
		self.frame_rows = [] # [0, 1, 2, 3, 4]
		color = 756867 #hexadecimal code

		n_row, n_column = self.config.row, self.config.column
		row_height, row_width = self.config.side//n_row, self.config.side

		for i in range(n_row):
			row_color = f"#{color}"
			frame = tk.Frame(self.mainframe, height=row_height, width=row_width, bg=row_color)
			self.frame_rows.append(frame)
			color += 500

	def show_board(self):
		for frame in self.frame_rows:
			frame.pack()

	def put_and_resize_photo(self, oriImg, scaler):
		n_row, n_column = self.config.row, self.config.column
		self.button_height, self.button_width = (self.config.side)//n_row - 6, self.config.side//n_column - 6
		
		image = Image.open(oriImg)
		image_w, image_h = image.size
		ratio = image_w/self.button_height
		image = image.resize((int(image_w//ratio + scaler), int(image_h//ratio + scaler)))
		return ImageTk.PhotoImage(image)

	def change_image_button(self, win, pos_x, pos_y):
		if win:
			img = self.win_img_btn
		else:
			img = self.final_img_btn
		self.button_board[pos_x][pos_y].configure(image = img)

	def create_button_board(self):
		self.button_board = []
		n_row, n_column = self.config.row, self.config.column
		self.button_height, self.button_width = (self.config.side)//n_row - 6, self.config.side//n_column - 6

		self.init_img_btn = self.put_and_resize_photo(oriImg = self.config.init_img_btn, scaler = 10)

		self.final_img_btn = self.put_and_resize_photo(oriImg = self.config.final_img_btn, scaler = 30)
	
		self.win_img_btn = self.put_and_resize_photo(oriImg = self.config.win_img_btn, scaler = 15)

		for i in range(n_row):
			row = []
			for j in range(n_column):
				button = tk.Button(self.frame_rows[i], bg="black", image=self.init_img_btn, height=self.button_height, width=self.button_width, command = lambda x = i, y = j:self.game.button_clicked(x, y))
				row.append(button)
			self.button_board.append(row)

	def show_button_board(self):
		n_row, n_column = self.config.row, self.config.column
		for i in range(n_row):
			for j in range(n_column):
				self.button_board[i][j].pack(side="left")

	def create_subframe(self):
		self.subframe = tk.Frame(self.mainframe, height=(self.config.side+150)/7.5, width=self.config.side, bg="black")
		self.subframe.pack(fill = "x", side = "bottom")

		self.steps_taken = tk.Label(self.subframe, font = ("Arial", 18, "bold"), text = 'Attempts = 0', pady = 2, padx = 2, bg = "black", fg = "white")
		self.steps_taken.pack(fill = 'x', side = 'left')

		self.reset_button = tk.Button(self.subframe, font = ("Arial", 18, "bold"), text = "Try Again", command = self.game.reset, padx = 2, pady = 2)
		self.reset_button.pack(fill = 'x', side = 'right')