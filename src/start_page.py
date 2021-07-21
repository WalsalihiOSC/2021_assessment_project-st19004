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

		title = Label(title_section, text="Untitled Math Program", font=TITLE_FONT, bg=COLOURSCHEME[3], fg="#FFFFFF")
		title.grid(column=0, row=0)


		# Header section
		header_section = Frame(self, bg=COLOURSCHEME[2])
		header_section.grid(column=0, row=1, sticky=NSEW)
		header_section.columnconfigure(0, weight=4)
		header_section.columnconfigure(1, weight=1)

		level_header = Frame(header_section, bg=COLOURSCHEME[2])
		level_header.grid(column=0, row=0, sticky=NSEW)

		level_header_label = Label(level_header, text="Level", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		level_header_label.pack(side=LEFT)

		for level in ["Easy", "Normal", "Hard"]:
			label = Label(level_header, text=level, font=HEADER_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
			label.pack(side=LEFT)

		recent_match_header = Frame(header_section, bg=COLOURSCHEME[2])
		recent_match_header.grid(column=1, row=0, sticky=NSEW)

		recent_match_header_label = Label(recent_match_header, text="Recently played", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		recent_match_header_label.pack(side=LEFT)


		# Content section
		content_section = Frame(self, bg=COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=4)
		content_section.columnconfigure(1, weight=1)

		level_content = Frame(content_section, bg=COLOURSCHEME[1])
		level_content.grid(column=0, row=0, sticky=NSEW)
		for i, level in enumerate(["Addition", "Subtraction", "Multiplication", "Division"]):
			level_content.rowconfigure(i, weight=1)
			frame = Frame(level_content, bg=COLOURSCHEME[1])
			frame.grid(column=0, row=i, sticky=NSEW)
			label = Label(frame, text=level, font=CONTENT_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
			label.pack(side=LEFT)
		
		recent_match_content = Frame(content_section, bg=COLOURSCHEME[1])
		recent_match_content.grid(column=1, row=0, sticky=NSEW)
