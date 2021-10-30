from tkinter import Tk, BOTH
from src import age_page, start_page, match_page, leaderboard_page, result_page
from src.base_page import BasePage

class Program(Tk):
	def start(self, initial_page: BasePage) -> None:
		"""Starting of the program that accepts an inital page"""
		self.pages: list[BasePage] = []

		if initial_page is not None:
			self.append_page(age_page)
		
		self.geometry("1200x700")
		self.mainloop()
	
	def append_page(self, page: BasePage, *args, **kwargs) -> None:
		"""Places page on top"""
		# An empty list is implicitly false
		if self.pages:
			self.pages[-1].pack_forget()
		
		page = page.Page(master=self, *args, **kwargs)
		page.pack(fill=BOTH, expand=True)
		self.pages.append(page)
	
	def pop_page(self) -> BasePage:
		"""Removes the top most page"""
		page = self.pages.pop()
		page.pack_forget()
		if self.pages:
			self.pages[-1].pack(fill=BOTH, expand=True)
		return page
	
	def show_page(self, wanted_page: str, *args, **kwargs) -> None:
		"""
		Shows a specific defined page:
			start
			leaderboard
			match
			result
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
		elif wanted_page == "result":
			page = result_page
		
		self.append_page(page, *args, **kwargs)

def main() -> None:
	root = Program().start(start_page)

if __name__ == "__main__":
	main()
