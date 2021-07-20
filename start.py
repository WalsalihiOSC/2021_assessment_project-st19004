from tkinter import Tk
from src import start_page, match_page, leaderboard_page

class Program(Tk):
	def __init__(self) -> None:
		super().__init__()

		start_page.Page(self).pack()

Program().mainloop()
