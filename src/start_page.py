from tkinter import Frame, Label, NSEW

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

		title = Label(title_section, text="Untitled Math Program", font=TITLE_FONT, bg=title_section["bg"], fg="#FFFFFF")
		title.grid(column=0, row=0)


		# Header section
		header_section = Frame(self, bg=COLOURSCHEME[2])
		header_section.grid(column=0, row=1, sticky=NSEW)

		level_frame = Frame(header_section, bg=COLOURSCHEME[2])
		level_frame.grid(column=0, row=0, sticky=NSEW)
		header_section.columnconfigure(0, weight=4)

		level_label = Label(level_frame, text="Level", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		level_label.pack(side="left")

		for level in ["Easy", "Normal", "Hard"]:
			label = Label(level_frame, text=level, font=HEADER_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
			label.pack(side="left")

		recent_match_frame = Frame(header_section, bg=COLOURSCHEME[2])
		recent_match_frame.grid(column=3, row=0, columnspan=1, sticky=NSEW)
		header_section.columnconfigure(3, weight=1)

		recent_match_label = Label(recent_match_frame, text="Recently played", font=HEADER_FONT, bg=COLOURSCHEME[2], fg=COLOURSCHEME[1])
		recent_match_label.pack(side="left")


		# Content section
		content_section = Frame(self, bg=COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=1)

		for i, level in enumerate(["Addition", "Subtraction", "Multiplication", "Division"]):
			frame = Label(content_section, bg=COLOURSCHEME[1])
			frame.grid(column=0, row=i, sticky=NSEW)
			label = Label(frame, text=level, font=CONTENT_FONT, bg=COLOURSCHEME[1], fg=COLOURSCHEME[0])
			label.pack(side="left")
