from os import sep, write
from sys import prefix
from typing import List

def append_data(level: str, operator: str, user: str, score: str) -> None:
	"""Appends data to a file"""
	with open("leaderboard.txt", "a+") as f:
		f.write(f"{level},{operator},{user},{score}\n")

def filter_data(level: str, operator: str) -> List[List]:
	"""Takes in level and operator and returns tuple of name and score"""
	with open("leaderboard.txt", "r+") as f:
		# Returns a list within a list containing a user and score sorted by score
		return sorted((line.strip().split(sep=",")[2:] for line in f.readlines() if line.startswith(f"{level},{operator}")), key=lambda a: a[1])
