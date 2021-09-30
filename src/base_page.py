from tkinter import Frame

class BasePage(Frame):
	"""Methods and attribute that are common to all pages"""
	COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]
	TITLE_FONT = ("Arial", 64)
	HEADER_FONT = ("Arial", 32)
	CONTENT_FONT = ("Arial", 32)

	def show_leaderboard(self, *args, **kwargs) -> None:
		"""Tells program to show leaderboard"""
		self.master.show_page("leaderboard", *args, **kwargs)

	def show_match(self, *args, **kwargs) -> None:
		"""Tells program to show match"""
		self.master.show_page("match", *args, **kwargs)
	
	def show_result(self, *args, **kwargs) -> None:
		"""Tells program to show result"""
		self.master.show_page("result", *args, **kwargs)
	
	def page_back(self) -> None:
		"""Tells program to go back one page"""
		self.master.pop_page().destroy()
	
	def page_back_to_menu(self) -> None:
		"""Tells program to go back to main menu"""
		# The first page show always be the main menu
		for i in range(len(self.master.pages) - 1):
			self.master.pop_page().destroy()
