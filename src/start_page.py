from tkinter import Button, Frame, Label, NSEW, LEFT
from .custom_widget import HoverButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title = Frame(self, bg=self.COLOURSCHEME[3])
		title.grid(column=0, row=0, sticky=NSEW)

		title.label = Label(title, text="Untitled Math Program", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.label.grid(column=0, row=0)

		# Header section
		header = Frame(self, bg=self.COLOURSCHEME[2])
		header.grid(column=0, row=1, sticky=NSEW)
		header.columnconfigure(0, weight=4)
		header.columnconfigure(1, weight=1)

		header.level = Frame(header, bg=self.COLOURSCHEME[2])
		header.level.grid(column=0, row=0, sticky=NSEW)

		header.level.label = Label(header.level, text="Year Level:", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		header.level.label.grid(column=0, row=0, sticky=NSEW)

		# Initialises difficultly
		for i, difficulty in enumerate(["1", "2", "3", "4"], 1):
			difficulty_button = HoverButton(header.level, text=difficulty, font=self.HEADER_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], relief="flat")
			difficulty_button.grid(column=i, row=0, sticky=NSEW)

		# Content section
		content = Frame(self, bg=self.COLOURSCHEME[1])
		content.grid(column=0, row=2, sticky=NSEW)
		content.columnconfigure(0, weight=1)

		content.level = Frame(content, bg=self.COLOURSCHEME[1])
		content.level.grid(column=0, row=0, sticky=NSEW)
		content.level.columnconfigure(0, weight=1)

		# TEMP: Hardcode
		level=1
		operator="+"

		# Initialises levels
		for i, difficulty in enumerate(["Addition", "Subtraction", "Multiplication"]):
			content.level.rowconfigure(i, weight=1)
			content.level.columnconfigure(0, weight=1)
			content.level.columnconfigure(1, weight=0)
			difficultly_button = HoverButton(
				content.level,
				text=difficulty,
				font=self.CONTENT_FONT,
				bg=self.COLOURSCHEME[1],
				fg=self.COLOURSCHEME[0],
				relief="flat", anchor="w",
				command=lambda: self.show_match((level, operator))
			)
			difficultly_button.grid(column=0, row=i, sticky=NSEW)

			leaderboard_button = HoverButton(content.level, text="T", font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], relief="flat", anchor="center", command=self.show_leaderboard)
			leaderboard_button.grid(column=1, row=i, sticky=NSEW)
