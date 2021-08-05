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
		"""Places page on top"""
		# An empty list is implicitly false
		if self.pages:
			self.pages[-1].pack_forget()

		page = page.Page(self, *args, **kwargs)
		page.pack(fill=BOTH, expand=True)
		self.pages.append(page)
	
	def pop_page(self) -> BasePage:
		"""Removes the top most page"""
		page = self.pages.pop()
		page.pack_forget()
		if self.pages:
			self.pages[-1].pack(fill=BOTH, expand=True)
		return page
	
	def show_page(self, wanted_page: str, *args, **kwargs):
		"""
		Shows a specific defined page:
			start
			leaderboard
			match
		"""
		if wanted_page is None:
			raise ValueError("No page specified")

		page: BasePage
		if wanted_page == "start":
			page = start_page
		elif wanted_page == "leaderboard":
			page = leaderboard_page
		elif wanted_page == "match":
			page = match_page
		
		self.append_page(page, *args, **kwargs)

root = Program(start_page)
root.mainloop()
