from tkinter import Button, Frame, Image, Label, NSEW, LEFT, PhotoImage
from .custom_widget import BackButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title = Frame(self, bg=self.COLOURSCHEME[3])
		title.grid(column=0, row=0, sticky=NSEW)

		title.label = Label(title, text="Level {level} {difficulty}", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.label.grid(column=0, row=0)

		back_button = BackButton(title, command=self.page_back, bg=self.COLOURSCHEME[3], relief="flat")
		back_button.place(relx=1, rely=0, x=-10, y=10, anchor="ne")

		# Header section
		header = Frame(self, bg=self.COLOURSCHEME[2])
		header.grid(column=0, row=1, sticky=NSEW)
		header.columnconfigure(0, weight=4)
		header.columnconfigure(1, weight=1)

		header.user = Frame(header, bg=self.COLOURSCHEME[2])
		header.user.grid(column=0, row=0, sticky=NSEW)

		header.user.label = Label(header.user, text="User", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		header.user.label.pack(side=LEFT)

		header.score = Frame(header, bg=self.COLOURSCHEME[2])
		header.score.grid(column=1, row=0, sticky=NSEW)

		header.score.label = Label(header.score, text="Score", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		header.score.label.pack(side=LEFT)

		# Content section
		content = Frame(self, bg=self.COLOURSCHEME[1])
		content.grid(column=0, row=2, sticky=NSEW)
		content.columnconfigure(0, weight=4)
		content.columnconfigure(1, weight=1)

		content.user = Frame(content, bg=self.COLOURSCHEME[1])
		content.user.grid(column=0, row=0, sticky=NSEW)

		content.score = Frame(content, bg=self.COLOURSCHEME[1])
		content.score.grid(column=1, row=0, sticky=NSEW)
