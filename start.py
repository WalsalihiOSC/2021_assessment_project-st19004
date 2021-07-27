from tkinter import Tk, BOTH
from src import start_page, match_page, leaderboard_page

class Program(Tk):
	def __init__(self, initial_page) -> None:
		super().__init__()

		if initial_page is not None:
			initial_page.Page(self).pack(fill=BOTH, expand=True)

		self.geometry("1920x1080")
		self.state("zoomed") # Maximize window

root = Program(match_page)
root.mainloop()
