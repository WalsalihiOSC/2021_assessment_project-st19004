from tkinter import Tk, BOTH
from src import start_page, match_page, leaderboard_page

class Program(Tk):
	def __init__(self) -> None:
		super().__init__()

		self.geometry("1920x1080")
		start_page.Page(self).pack(fill=BOTH, expand=True)

root = Program()
root.mainloop()
