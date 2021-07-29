from tkinter import Frame

class BasePage(Frame):
	"""Methods and attribute that are common to all pages"""
	COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]
	TITLE_FONT = ("Arial", 100)
	HEADER_FONT = ("Arial", 32)
	CONTENT_FONT = ("Arial", 32)

	def show_leaderboard(self):
		"""Tells program to show leaderboard"""
		self.master.show_page("leaderboard")

	def show_match(self):
		"""Tells program to show match"""
		self.master.show_page("match")
	
	def page_back(self):
		"""Tells program to go back one page"""
		self.master.pop_page()
