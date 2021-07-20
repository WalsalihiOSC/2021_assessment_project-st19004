from tkinter import Frame, Label, NSEW

class Page(Frame):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1)

		# Title section
		title_section = Frame(self, bg="#28C538")
		title_section.grid(column=0, row=0, sticky=NSEW)
		self.rowconfigure(0, weight=25)

		# Header section
		header_section = Frame(self, bg="#1FB500")
		header_section.grid(column=0, row=1, sticky=NSEW)
		self.rowconfigure(1, weight=10)

		# Content section
		content_section = Frame(self, bg="#FFFFFF")
		content_section.grid(column=0, row=2, sticky=NSEW)
		self.rowconfigure(2, weight=65)
