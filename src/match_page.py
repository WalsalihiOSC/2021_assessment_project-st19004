from tkinter import Button, Frame, Label, NSEW, LEFT, Entry, StringVar, IntVar
from tkinter.constants import CENTER
from random import randint
from typing import Tuple
from .custom_widget import BackButton
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, match_settings: Tuple[int, str], *args, **kwargs) -> None:
		super().__init__()
		# Ensure the frame size stretches to fit horizontally
		self.columnconfigure(0, weight=1)
		# Makes the last row(contentt section) take up the rest of the unused space
		self.rowconfigure(2, weight=1)

		# Unpacks the tuple into 2 variable
		self.level, self.operator = match_settings
		self.score = IntVar()
		self.init_match()
		
	def init_match(self) -> None:
		self.init_title_section()
		self.init_header_section()
		self.init_content_section()
		self.init_answer()
	
	def init_title_section(self) -> None:
		self.title_section = Frame(self, bg=self.COLOURSCHEME[3])
		self.title_section.grid(column=0, row=0, sticky=NSEW)

		self.title = Label(self.title_section, font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		self.title.grid(column=0, row=0)

		back_button = BackButton(self.title_section, command=self.page_back, bg=self.COLOURSCHEME[3], relief="flat")
		back_button.place(relx=1, rely=0, x=-10, y=10, anchor="ne")
	
	def init_header_section(self) -> None:
		self.header_section = Frame(self, bg=self.COLOURSCHEME[2])
		self.header_section.grid(column=0, row=1, sticky=NSEW)
		self.header_section.columnconfigure(0, weight=4)
		self.header_section.columnconfigure(1, weight=1)

		user_header = Frame(self.header_section, bg=self.COLOURSCHEME[2])
		user_header.grid(column=0, row=0, sticky=NSEW)

		user_header_label = Label(user_header, text="Time left", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		user_header_label.pack(side=LEFT)

		score_header = Frame(self.header_section, bg=self.COLOURSCHEME[2])
		score_header.grid(column=1, row=0, sticky=NSEW)
		score_header.columnconfigure(0, weight=1)
		score_header.columnconfigure(1, weight=1)

		score_header_label = Label(score_header, text="Score", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		score_header_label.grid(column=0, row=0, sticky=NSEW)
		score_header_value = Label(score_header, text="0", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		score_header_value.grid(column=1, row=0, sticky=NSEW)
		# _a, _b, _c variable are irrelevant to updating the score header
		self.score.trace_add("write", lambda _a, _b, _c: score_header_value.config(text=self.score.get()))

	def init_content_section(self) -> None:
		self.content_section = Frame(self, bg=self.COLOURSCHEME[1])
		self.content_section.grid(column=0, row=2, sticky=NSEW)
		self.content_section.columnconfigure(0, weight=1)
		self.content_section.columnconfigure(1, weight=1)
		self.content_section.columnconfigure(2, weight=1)
		self.content_section.rowconfigure(0, weight=1)

		self.init_calculator()

	def init_calculator(self) -> None:
		# Calculator
		calculator_frame = Frame(self.content_section, bg=self.COLOURSCHEME[1])
		calculator_frame.grid(column=1, row=0, sticky=NSEW, pady=30)

		# Padding to keep calculator centred
		padding_frame_left = Frame(self.content_section, bg=self.COLOURSCHEME[1])
		padding_frame_left.grid(column=0, row=0, sticky=NSEW)
		padding_frame_right = Frame(self.content_section, bg=self.COLOURSCHEME[1])
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

	def init_answer(self) -> None:
		self.answer_var = answer_var = StringVar()
		answer_box = Entry(self.title_section, width=6, font=self.TITLE_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], justify=CENTER, textvariable=answer_var, validate="key", validatecommand=(self.register(self.validate_input), "%P"))
		answer_box.grid(column=1, row=0)
		answer_box.bind("<Return>", self.answer)
		self.generate_question()

	def answer(self, event) -> None:
		input = self.answer_var.get()
		# Just in case the input wasn't validated 
		# when inputted for whatever reason
		if self.validate_input(input):
			# Checks if answer is correct
			# If correct award 1 point
			# Else remove 1 point
			if self.check_answer():
				self.score.set(self.score.get()+1)
			else:
				self.score.set(self.score.get()-1)
			self.generate_question()
		else:
			# If for unexplained reason the input was invalid
			# Quietly fail the answer and remove 1 point
			self.score.set(self.score.get()-1)

	def generate_question(self) -> None:
		num1 = randint(1*10**(self.level-1), 1*10**self.level)
		num2 = randint(1*10**(self.level-1), 1*10**self.level)
		equation = f"{num1}{self.operator}{num2}"
		self.title.config(text=f"{equation}=")
		self.answer_var.set("")
		# Evaluate equation and turn the number into a string
		self.correct_answer = correct_answer = str(eval(equation))
	
	def check_answer(self) -> bool:
		if self.answer_var.get() == self.correct_answer:
			return True
		else:
			return False

	def validate_input(self, text: str) -> bool:
		"""Return true if text is a digit or is empty and check if length of input is 6 or less"""
		return (text.isdigit() or text == "") and len(text) <= 6
