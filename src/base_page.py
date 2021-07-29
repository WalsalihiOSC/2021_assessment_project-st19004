from tkinter import Frame

class BasePage(Frame):
	COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]
	TITLE_FONT = ("Arial", 100)
	HEADER_FONT = ("Arial", 32)
	CONTENT_FONT = ("Arial", 32)

	def show_leaderboard(self):
		self.master.show_page("leaderboard")

	def show_match(self):
		self.master.show_page("match")
	
	def page_back(self):
		self.master.pop_page()
