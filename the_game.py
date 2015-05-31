#TheAbraxas RPG Version 0.1

import character
import game

from random import randint

pos = ["Yes", "yes", "Yep", "yep", "Y", "y"]
neg = ["No", "no", "Nope", "nope", "N", "n"]

def start ():
	print "You are starting a new job"
	player = character.Character(raw_input("Enter your name: "))

	print "Wlecome to your new job at SUPERMEGACORP, %s" % player.name
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

def level_1(player):
	s = "Your stats for this level are: \n Level: {0} \n Health: {1} \n Strength: {2}"
	print s.format(player.level, player.health, player.strength)



game.Game().start(player)















#CREDITS

#Lead Developer - Stewart Olson
#Secondary Lead Developer - Felixk24 
#Lead Editor - Felixk24