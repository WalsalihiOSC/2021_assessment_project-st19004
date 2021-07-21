from tkinter import Frame, Label, NSEW, LEFT

COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]
TITLE_FONT = ("Arial", 100)
HEADER_FONT = ("Arial", 32)
CONTENT_FONT = ("Arial", 32)
class Page(Frame):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		self.columnconfigure(0, weight=1) # Ensure the frame size stretches to fit horizontally


		# Title section
		title_section = Frame(self, bg=COLOURSCHEME[3])
		title_section.grid(column=0, row=0, sticky=NSEW)

		title = Label(title_section, text="Level {level} {difficulty}", font=TITLE_FONT, bg=COLOURSCHEME[3], fg="#FFFFFF")
		title.grid(column=0, row=0)


		# Header section
		header_section = Frame(self, bg=COLOURSCHEME[2])
		header_section.grid(column=0, row=1, sticky=NSEW)
		header_section.columnconfigure(0, weight=4)
		header_section.columnconfigure(1, weight=1)

		user_header = Frame(header_section, bg=COLOURSCHEME[2])
		user_header.grid(column=0, row=0, sticky=NSEW)

		user_header_label = Label(user_header, text="User", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		user_header_label.pack(side=LEFT)

		score_header = Frame(header_section, bg=COLOURSCHEME[2])
		score_header.grid(column=1, row=0, sticky=NSEW)

		score_header_label = Label(score_header, text="Score", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		score_header_label.pack(side=LEFT)


		# Content section
		content_section = Frame(self, bg=COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=4)
		content_section.columnconfigure(1, weight=1)

		user_content = Frame(content_section, bg=COLOURSCHEME[1])
		user_content.grid(column=0, row=0, sticky=NSEW)

		score_content = Frame(content_section, bg=COLOURSCHEME[1])
		score_content.grid(column=1, row=0, sticky=NSEW)

		if __debug__:
			for row, (user, score) in enumerate(zip(["Alex", "Alex"], ["34", "14"])):
				user_frame = Frame(user_content, bg=COLOURSCHEME[1])
				user_frame.grid(column=0, row=row, sticky=NSEW)
				user_label = Label(user_frame, text=user, font=CONTENT_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
				user_label.pack(side=LEFT)
				
				score_frame = Frame(score_content, bg=COLOURSCHEME[1])
				score_frame.grid(column=1, row=row, sticky=NSEW)
				score_label = Label(score_frame, text=score, font=CONTENT_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
				score_label.pack(side=LEFT)
