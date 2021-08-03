from tkinter import Button, Frame, Label, NSEW, LEFT
from .custom_widget import BackButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)
		# Ensure the frame size stretches to fit horizontally
		self.columnconfigure(0, weight=1)
		# Makes the last row(contentt section) take up the rest of the unused space
		self.rowconfigure(2, weight=1)

		# Title section
		title_section = Frame(self, bg=self.COLOURSCHEME[3])
		title_section.grid(column=0, row=0, sticky=NSEW)

		title = Label(title_section, text="XXX+XXX=", font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
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

		user_header_label = Label(user_header, text="Time left", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		user_header_label.pack(side=LEFT)

		score_header = Frame(header_section, bg=self.COLOURSCHEME[2])
		score_header.grid(column=1, row=0, sticky=NSEW)

		score_header_label = Label(score_header, text="Score", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		score_header_label.pack(side=LEFT)

		# Content section
		content_section = Frame(self, bg=self.COLOURSCHEME[1])
		content_section.grid(column=0, row=2, sticky=NSEW)
		content_section.columnconfigure(0, weight=1)
		content_section.columnconfigure(1, weight=1)
		content_section.columnconfigure(2, weight=1)
		content_section.rowconfigure(0, weight=1)

		# Calculator
		calculator_frame = Frame(content_section, bg=self.COLOURSCHEME[1])
		calculator_frame.grid(column=1, row=0, sticky=NSEW, pady=30)

		# Padding to keep calculator centred
		padding_frame_left = Frame(content_section, bg=self.COLOURSCHEME[1])
		padding_frame_left.grid(column=0, row=0, sticky=NSEW)
		padding_frame_right = Frame(content_section, bg=self.COLOURSCHEME[1])
		padding_frame_right.grid(column=2, row=0, sticky=NSEW)

		# Initialisation for the calculator's buttons
		for row in range(3):
			for col in range(3):
				calculator_frame.columnconfigure(col, weight=1)
				calculator_frame.rowconfigure(row, weight=1)
				label = Label(calculator_frame, text=str(row*3+col+1), bg=self.COLOURSCHEME[1], font=self.CONTENT_FONT, borderwidth=1, relief="solid")
				label.grid(column=col, row=row, sticky=NSEW, padx=10, pady=10)
		# Initialisation for the last 2 buttons
		# Should be changed to reduce duplication
		calculator_frame.rowconfigure(3, weight=1)
		label = Label(calculator_frame, text="0", bg=self.COLOURSCHEME[1], font=self.CONTENT_FONT, borderwidth=1, relief="solid")
		label.grid(column=0, row=3, sticky=NSEW, padx=10, pady=10)
		label = Label(calculator_frame, text="Enter", bg=self.COLOURSCHEME[1], font=self.CONTENT_FONT, borderwidth=1, relief="solid")
		label.grid(column=1, row=3, sticky=NSEW, columnspan=2, padx=10, pady=10)