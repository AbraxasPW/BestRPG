#Game
import character

class Game:
	def __init__(self): # the game start with a player
	  self.player = player
 
	def start(self):
		#Pick your name!
		print "You are starting a new job"
		player = character.Character(raw_input("Enter your name: ")) # modify your code here player now it's player = self.player
 
		print "Welcome to your new job at SUPERMEGACORP, %s" % player.name
		print "What is your specialization again?"
 
		#Define job class/specialization field
 
		answer = raw_input("Choose from: Dev, Sysadmin, or Helpdesk")
		jobs = ["Dev", "dev", "Sysadmin", "sysadmin", "Helpdesk", "helpdesk"]
 
		if answer not in jobs:
			print "That job is not in the options. \nTry again, %s" % player.name
		elif answer in pos:
			print "Get ready to start your new job as a %s" % answer
			level_1(player)
		else:
			print "WTF ARE YOU TALKING ABOUT?"