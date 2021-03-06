from tkinter import Button, Frame, Label, NSEW, LEFT, Entry, StringVar, IntVar
from tkinter.ttk import Progressbar
from tkinter.constants import CENTER, HORIZONTAL
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
		# Max time
		self.time = 60
		self.score = IntVar()
		self.init_match()
		
	def init_match(self) -> None:
		self.init_title_section()
		self.init_header_section()
		self.init_content_section()
		self.init_answer()
		self.init_calculator()
		self.step() # Updating function
	
	def init_title_section(self) -> None:
		self.title = Frame(self, bg=self.COLOURSCHEME[3])
		self.title.grid(column=0, row=0, sticky=NSEW)

		self.title.label = Label(self.title, font=self.TITLE_FONT, bg=self.COLOURSCHEME[3], fg=self.COLOURSCHEME[1])
		self.title.label.grid(column=0, row=0)

		back_button = BackButton(self.title, command=self.page_back, bg=self.COLOURSCHEME[3], relief="flat")
		back_button.place(relx=1, rely=0, x=-10, y=10, anchor="ne")
	
	def init_header_section(self) -> None:
		self.header = Frame(self, bg=self.COLOURSCHEME[2])
		self.header.grid(column=0, row=1, sticky=NSEW)
		self.header.columnconfigure(0, weight=4)
		self.header.columnconfigure(1, weight=1)

		self.header.time = Frame(self.header, bg=self.COLOURSCHEME[2])
		self.header.time.grid(column=0, row=0, sticky=NSEW)

		self.header.time.label = Label(self.header.time, text="Time left: ", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		self.header.time.label.grid(column=0, row=0)
		self.header.time.columnconfigure(0, weight=0)

		self.header.time.value = Label(self.header.time, text=f"{self.time}", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		self.header.time.value.grid(column=1, row=0)
		self.header.time.columnconfigure(1, weight=0)

		self.header.score = Frame(self.header, bg=self.COLOURSCHEME[2])
		self.header.score.grid(column=1, row=0, sticky=NSEW)
		self.header.score.columnconfigure(0, weight=1)
		self.header.score.columnconfigure(1, weight=1)

		self.header.score.label = Label(self.header.score, text="Score", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		self.header.score.label.grid(column=0, row=0, sticky=NSEW)
		self.header.score.value = Label(self.header.score, text="0", font=self.HEADER_FONT, bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])
		self.header.score.value.grid(column=1, row=0, sticky=NSEW)
		# _a, _b, _c variable are irrelevant to updating the score header
		self.score.trace_add("write", lambda _a, _b, _c: self.header.score.value.config(text=self.score.get()))

	def init_content_section(self) -> None:
		self.content = Frame(self, bg=self.COLOURSCHEME[1])
		self.content.grid(column=0, row=2, sticky=NSEW)
		self.content.columnconfigure(0, weight=1)
		self.content.columnconfigure(1, weight=1)
		self.content.columnconfigure(2, weight=1)
		self.content.rowconfigure(0, weight=1)

	def init_calculator(self) -> None:
		# Calculator
		calculator = Frame(self.content, bg=self.COLOURSCHEME[1])
		calculator.grid(column=1, row=0, sticky=NSEW, pady=30)

		# Padding to keep calculator centred
		padding_frame_left = Frame(self.content, bg=self.COLOURSCHEME[1])
		padding_frame_left.grid(column=0, row=0, sticky=NSEW)
		padding_frame_right = Frame(self.content, bg=self.COLOURSCHEME[1])
		padding_frame_right.grid(column=2, row=0, sticky=NSEW)
		
		def command(x: str) -> None:
			if x.isdigit():
				# Regular digits that is safe for the answer box
				self.answer_var.set(self.answer_var.get() + x)
			elif x == "???":
				# Enter
				# Submits the current answer box for checking and scoring
				self.answer()
			elif x == "???":
				# Backspace
				# Removes 1 character from answer box
				self.answer_var.set(self.answer_var.get()[0:-1])
			else:
				# Just in case I add a new value and forgot a case for it
				raise ValueError("Invalid calculator button")
		
		def create_calculator_button(i: int, v: str) -> None:
			col, row = i % 3, int(i / 3)
			calculator.columnconfigure(col, weight=1)
			calculator.rowconfigure(row, weight=1)
			button = Button(calculator, text=v, bg=self.COLOURSCHEME[1], font=self.CONTENT_FONT, borderwidth=1, relief="solid", command=lambda: command(v))
			button.grid(column=col, row=row, sticky=NSEW, padx=10, pady=10)

		# Initialisation for the calculator's buttons
		for (i, v) in enumerate(["1", "2", "3", "4", "5", "6", "7", "8", "9", "???", "0", "???"]):
			create_calculator_button(i, v)
			
	def init_answer(self) -> None:
		self.answer_var = answer_var = StringVar()
		answer_box = Entry(self.title, width=6, font=self.TITLE_FONT, bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0], justify=CENTER, textvariable=answer_var, validate="key", validatecommand=(self.register(self.validate_input), "%P"))
		answer_box.grid(column=1, row=0)
		answer_box.bind("<Return>", self.answer)
		self.generate_question()

	def answer(self, event=None) -> None:
		input = self.answer_var.get()
		# Just in case the input wasn't validated 
		# when inputted for whatever reason
		if self.validate_input(input):
			# Checks if answer is correct
			# If correct award 1 point
			if self.check_answer():
				self.increment_score()
			self.generate_question()

	def generate_question(self) -> None:
		num1 = randint(1*10**(self.level-1), 1*10**self.level)
		num2 = randint(1*10**(self.level-1), 1*10**self.level)
		# Have the biggest number on the left side to make it easier
		if num1 < num2:
			num1, num2 = num2, num1
		equation = f"{num1}{self.operator}{num2}"
		self.title.label.config(text=f"{equation}=")
		self.answer_var.set("")
		# Evaluate equation and turn the number into a string
		self.correct_answer = correct_answer = str(eval(equation))
	
	def check_answer(self) -> bool:
		answer = self.answer_var.get()
		if answer:
			if float(answer) == float(self.correct_answer):
				return True
			else:
				return False
		else:
			return False

	def validate_input(self, text: str) -> bool:
		"""Return true if text is a digit or is empty"""
		return (text.isdigit() or text == "")

	def increment_score(self) -> None:
		self.score.set(self.score.get()+1)
	
	def step(self):
		if self.time == 0:
			self.finish()
		else:
			self.header.time.value.config(text=f"{self.time}")
			self.time -= 1
			self.after(1000, self.step)
	
	def finish(self):
		self.show_result(self.level, self.operator, self.score.get())
