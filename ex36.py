from sys import argv
from sys import exit
import matplotlib.pyplot as plt


script, story_name = argv

def door_1():
	print("hi")

def start(instance = 1):

	if instance == 2:
		print("\n")

	else:
		print("\tLong Wina and the ", story_name)
		print("You are Long Wina, an adventurer looking for treasure in the catacombs of Paris.")
		print("You enter the network, where there are 5 doors.")
		print("Which door do you choose?")

	door = int(input("> "))

	if door == 1:
		print("You chose door 1.")
		door_1()
	elif door == 2:
		print("You chose door 2.")
	elif door == 3:
		print("You chose door 3.")
	elif door == 4:
		print("You chose door 4.")
	elif door == 5:
		print("You chose door 5.")
	else:
		print("That's not an option ya doofus.")
		print("Please enter a number from 1 to 5.")
		start(2)


start()