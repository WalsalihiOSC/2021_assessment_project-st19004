from src import leaderboard
from tkinter import Entry, Frame, Label, NSEW, LEFT
from tkinter.constants import CENTER
from .custom_widget import BackButton, HoverButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, level, operator, score, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title = Frame(self, bg=self.COLOURSCHEME[3])
		title.grid(column=0, row=0, sticky=NSEW)

		title.label = Label(title, text=f"Level {level}", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.label.grid(column=0, row=0)

		back_button = BackButton(title, command=self.page_back_to_menu, bg=self.COLOURSCHEME[3], relief="flat")
		back_button.place(relx=1, rely=0, x=-10, y=10, anchor="ne")

		# Header section
		header = Frame(self, bg=self.COLOURSCHEME[2])
		header.grid(column=0, row=1, sticky=NSEW)
		header.columnconfigure(0, weight=4)
		header.columnconfigure(1, weight=1)

		header.operator = Frame(header, bg=self.COLOURSCHEME[2])
		header.operator.grid(column=0, row=0, sticky=NSEW)

		header.operator.label = Label(header.operator, text=f"Operation: {operator}", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		header.operator.label.pack(side=LEFT)

		header.score = Frame(header, bg=self.COLOURSCHEME[2])
		header.score.grid(column=1, row=0, sticky=NSEW)

		header.score.label = Label(header.score, text=f"Score: {score}", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		header.score.label.pack(side=LEFT)

		# Content section
		content = Frame(self, bg=self.COLOURSCHEME[1])
		content.grid(column=0, row=2, sticky=NSEW)

		content.user_label = Label(content, text="Name: ", font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])
		content.user_label.grid(column=0, row=0, sticky=NSEW)
		content.columnconfigure(0, weight=0)

		content.user_input = Entry(content, font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])
		content.user_input.grid(column=1, row=0, sticky=NSEW)
		content.columnconfigure(1, weight=1)

		content.button = Frame(content)
		content.button.grid(column=0, row=1, sticky=NSEW, columnspan=2)

		content.button.save = HoverButton(content.button, text="Save", font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], command=lambda: self.save(level, operator, content.user_input.get(), score))
		content.button.save.grid(column=0, row=0)
		content.button.columnconfigure(0, weight=1)

		content.button.exit = HoverButton(content.button, text="Exit without saving", font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], command=self.page_back_to_menu)
		content.button.exit.grid(column=1, row=0)
		content.button.columnconfigure(1, weight=1)

	def save(self, level: str, operator: str, user: str, score: str) -> None:
		leaderboard.append_data(level, operator, user, score)
		self.page_back_to_menu()