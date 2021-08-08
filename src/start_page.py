from tkinter import Button, Frame, Label, NSEW, LEFT
from .custom_widget import HoverButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title_section = Frame(self, bg=self.COLOURSCHEME[3])
		title_section.grid(column=0, row=0, sticky=NSEW)

		title = Label(title_section, text="Untitled Math Program", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.grid(column=0, row=0)

		# Header section
		header_section = Frame(self, bg=self.COLOURSCHEME[2])
		header_section.grid(column=0, row=1, sticky=NSEW)
		header_section.columnconfigure(0, weight=4)
		header_section.columnconfigure(1, weight=1)

		level_header = Frame(header_section, bg=self.COLOURSCHEME[2])
		level_header.grid(column=0, row=0, sticky=NSEW)

		level_header_label = Label(level_header, text="Level", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		level_header_label.grid(column=0, row=0, sticky=NSEW)

		# Initialises difficultly
		for i, difficulty in enumerate(["Easy", "Normal", "Hard"], 1):
			difficulty_button = HoverButton(level_header, text=difficulty, font=self.HEADER_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], relief="flat")
			difficulty_button.grid(column=i, row=0, sticky=NSEW)

		recent_match_header = Frame(header_section, bg=self.COLOURSCHEME[2])
		recent_match_header.grid(column=1, row=0, sticky=NSEW)

		recent_match_header_label = Label(recent_match_header, text="Recently played", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		recent_match_header_label.pack(side=LEFT)

		# Content section
		content_section = Frame(self, bg=self.COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=4)
		content_section.columnconfigure(1, weight=1)

		level_content = Frame(content_section, bg=self.COLOURSCHEME[1])
		level_content.grid(column=0, row=0, sticky=NSEW)
		level_content.columnconfigure(0, weight=1)

		# TEMP: Hardcode
		level=1
		operator="+"

		# Initialises levels
		for i, difficulty in enumerate(["Addition", "Subtraction", "Multiplication", "Division"]):
			level_content.rowconfigure(i, weight=1)
			level_button = HoverButton(level_content,text=difficulty, font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], relief="flat", anchor="w", command=lambda: self.show_match((level, operator)))
			level_button.grid(column=0, row=i, sticky=NSEW)

			match_button = HoverButton(level_content, text="T", font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], relief="flat", anchor="center", command=self.show_leaderboard)
			match_button.grid(column=1, row=i, sticky=NSEW)
		
		recent_match_content = Frame(content_section, bg=self.COLOURSCHEME[1])
		recent_match_content.grid(column=1, row=0, sticky=NSEW)
