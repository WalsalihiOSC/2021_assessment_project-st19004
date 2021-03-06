from tkinter import Button, Frame, IntVar, Label, NSEW, LEFT, StringVar
from .custom_widget import HoverButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title = Frame(self, bg=self.COLOURSCHEME[3])
		title.grid(column=0, row=0, sticky=NSEW)

		title.label = Label(title, text="Ormiston Computing", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
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
		self.level=IntVar(value=1)
		# Variable copied inside function
		def create_difficulty_button(x: int) -> HoverButton:
			button = HoverButton(
				header.level,
				text=x,
				font=self.HEADER_FONT,
				bg=self.COLOURSCHEME[1],
				fg=self.COLOURSCHEME[0],
				relief="flat",
				command=lambda: self.level.set(x)
			)
			def update(a, b, c) -> None:
				if x == self.level.get():
					button.activated = True
					button.config(bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
				else:
					button.activated = False
					button.config(bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])
			update(None, None, None) # Guarantees to update the colour and state
			self.level.trace_add("write", update)
			return button
		# Range between 1 - 4 to represent Year level
		for i in range(1, 5):
			difficulty_button = create_difficulty_button(i)
			difficulty_button.grid(column=i, row=0, sticky=NSEW)

		# Content section
		content = Frame(self, bg=self.COLOURSCHEME[1])
		content.grid(column=0, row=2, sticky=NSEW)
		content.columnconfigure(0, weight=1)

		content.level = Frame(content, bg=self.COLOURSCHEME[1])
		content.level.grid(column=0, row=0, sticky=NSEW)
		content.level.columnconfigure(0, weight=1)

		# Variables contained instead of global
		def create_level_button(name: int, operator: str) -> HoverButton:
			return HoverButton(
				content.level,
				text=name,
				font=self.CONTENT_FONT,
				bg=self.COLOURSCHEME[1],
				fg=self.COLOURSCHEME[0],
				relief="flat",
				anchor="w",
				command=lambda: self.show_match((
					self.level.get(),
					operator
				))
			)

		def create_leaderboard_button(operator: str) -> HoverButton:
			return HoverButton(
				content.level,
				text="????",
				font=self.CONTENT_FONT,
				bg=self.COLOURSCHEME[1],
				fg=self.COLOURSCHEME[0],
				relief="flat",
				anchor="center",
				command=lambda: self.show_leaderboard(
					self.level.get(),
					operator
				)
			)

		# Initialises levels
		for i, (difficulty, operator) in enumerate(zip(["???Addition", "???Subtraction", "???Multiplication"], ["+", "-", "*"])):
			content.level.rowconfigure(i, weight=1) # Row to take all horizontal space
			content.level.columnconfigure(0, weight=1) # Difficutly column
			content.level.columnconfigure(1, weight=0) # Leaderboard column
			difficultly_button = create_level_button(difficulty, operator)
			difficultly_button.grid(column=0, row=i, sticky=NSEW)
			leaderboard_button = create_leaderboard_button(operator)
			leaderboard_button.grid(column=1, row=i, sticky=NSEW)
