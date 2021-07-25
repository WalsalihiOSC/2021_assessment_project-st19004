from tkinter import Tk, BOTH
from src import start_page, match_page, leaderboard_page
from src.base_page import BasePage

class Program(Tk):
	def __init__(self, initial_page: BasePage) -> None:
		super().__init__()

		self.pages: list[BasePage] = []

		if initial_page is not None:
			self.append_page(start_page)

		self.geometry("1920x1080")
		self.state("zoomed") # Maximize window
	
	def append_page(self, page: BasePage, *args, **kwargs) -> None:
		# An empty list is implicitly false
		if self.pages:
			self.pages[-1].pack_forget()

		page = page.Page(self, *args, **kwargs)
		page.pack(fill=BOTH, expand=True)
		self.pages.append(page)
		

root = Program(leaderboard_page)
root.mainloop()
