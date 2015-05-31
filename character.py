#Character File

from random import randint

class Character:
	def __init__(self, name):
		#Initializing character
		self.name = name
		self.level = 1
		self.health_m = randint(15,25)
		self.health = self.health_m
		self.strength = randint(5,10)