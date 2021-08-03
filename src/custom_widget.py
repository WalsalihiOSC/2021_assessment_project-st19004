from tkinter import Button, PhotoImage

class HoverButton(Button):
	"""
	Creates a button that when hovered over,
	changes the background and foreground to match colourscheme
	"""
	COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, event):
		"""Method for when <Enter> is triggered"""
		self.config(bg=self.COLOURSCHEME[2], fg=self.COLOURSCHEME[1])

	def on_leave(self, event):
		"""Method for when <Leave> is triggered"""
		self.config(bg=self.COLOURSCHEME[1], fg=self.COLOURSCHEME[0])

class BackButton(Button):
	"""
	Creates a back button
	"""
	COLOURSCHEME = ["#707070", "#FFFFFF", "#1FB500", "#28C538"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.image=PhotoImage(file="asset/back.png")
		self.image_hover=PhotoImage(file="asset/back-hover.png")
		self.config(image=self.image)

		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, event):
		"""Method for when <Enter> is triggered"""
		self.config(image=self.image_hover)

	def on_leave(self, event):
		"""Method for when <Leave> is triggered"""
		self.config(image=self.image)