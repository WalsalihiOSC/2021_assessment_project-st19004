from tkinter import Tk, BOTH
from src import start_page, match_page, leaderboard_page

class Program(Tk):
	def __init__(self) -> None:
		super().__init__()

		self.geometry("1920x1080")
		self.state("zoomed") # Maximize window

root = Program()
start_page.Page(root).pack(fill=BOTH, expand=True)
root.mainloop()
