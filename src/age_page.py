from tkinter import Button, Entry, Frame, Label
from tkinter import messagebox
from .base_page import BasePage

class Page(BasePage):
	def __init__(self, *args, **kwargs) -> None:
		super().__init__(*args, **kwargs)

		self.frame = Frame(self)
		self.frame.pack(fill="none", expand=True)
		self.question = Label(self.frame, text="How old are you? ")
		self.question.grid()
		self.entry = Entry(self.frame, justify="center")
		self.entry.grid()
		self.button = Button(self.frame, text="Submit", command=self.on_button_press)
		self.button.grid()
	
	def on_button_press(self) -> None:
		"""Function for when the button is pressed"""
		value = self.entry.get()
		if not self.valid_input(value):
			messagebox.showerror("Input error", "Input is not a valid integer,\nplease input a number between 7 and 12")
		if not self.valid_age(value):
			messagebox.showerror("Range error", "Input is not a number between 7 and 12,\nplease input a number between 7 and 12")
		else:
			self.page_back()
			self.show_main()
	
	def valid_input(self, x: str) -> None:
		"""Returns true if the input are valid numbers"""
		return x.isdigit()

	def valid_age(self, x: str) -> None:
		"""Returns true if the age is between 7 and 12 else false if otherwise"""
		return 7 <= int(x) <= 12
