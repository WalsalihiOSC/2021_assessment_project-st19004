from tkinter import Frame, Label, NSEW, LEFT
from src import base_page

class Page(base_page.BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally


		# Title section
		title_section = Frame(self, bg=self.COLOURSCHEME[3])
		title_section.grid(column=0, row=0, sticky=NSEW)

		title = Label(title_section, text="Level {level} {difficulty}", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		title.grid(column=0, row=0)


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

		if __debug__:
			for row, (user, score) in enumerate(zip(["Alex", "Alex"], ["34", "14"])):
				user_frame = Frame(user_content, bg=self.COLOURSCHEME[1])
				user_frame.grid(column=0, row=row, sticky=NSEW)
				user_label = Label(user_frame, text=user, font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])
				user_label.pack(side=LEFT)
				
				score_frame = Frame(score_content, bg=self.COLOURSCHEME[1])
				score_frame.grid(column=1, row=row, sticky=NSEW)
				score_label = Label(score_frame, text=score, font=self.CONTENT_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])
				score_label.pack(side=LEFT)
