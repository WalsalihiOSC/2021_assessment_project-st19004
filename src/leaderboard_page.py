from tkinter import Button, Frame, Image, Label, NSEW, LEFT, PhotoImage
from .custom_widget import BackButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally

		# Title section
		title_section = Frame(self, bg=self.COLOURSCHEME[3])
		title_section.grid(column=0, row=0, sticky=NSEW)

		title = Label(title_section, text="Level {level} {difficulty}", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.grid(column=0, row=0)

		back_button = BackButton(title_section, command=self.page_back, bg=self.COLOURSCHEME[3], relief="flat")
		back_button.place(relx=1, rely=0, x=-10, y=10, anchor="ne")

		# Header section
		header_section = Frame(self, bg=self.COLOURSCHEME[2])
		header_section.grid(column=0, row=1, sticky=NSEW)
		header_section.columnconfigure(0, weight=4)
		header_section.columnconfigure(1, weight=1)

		user_header = Frame(header_section, bg=self.COLOURSCHEME[2])
		user_header.grid(column=0, row=0, sticky=NSEW)

		user_header_label = Label(user_header, text="User", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		user_header_label.pack(side=LEFT)

		score_header = Frame(header_section, bg=self.COLOURSCHEME[2])
		score_header.grid(column=1, row=0, sticky=NSEW)

		score_header_label = Label(score_header, text="Score", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		score_header_label.pack(side=LEFT)

		# Content section
		content_section = Frame(self, bg=self.COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=4)
		content_section.columnconfigure(1, weight=1)

		user_content = Frame(content_section, bg=self.COLOURSCHEME[1])
		user_content.grid(column=0, row=0, sticky=NSEW)

		score_content = Frame(content_section, bg=self.COLOURSCHEME[1])
		score_content.grid(column=1, row=0, sticky=NSEW)
