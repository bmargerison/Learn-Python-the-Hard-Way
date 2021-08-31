"""
1. Write or draw the problem:
Death - when the player dies, selection of death types
Central chamber - the middle room form which player selects the doors
Door - the choices are player makes to enter certain rooms
	door1 - dead instantly
	door2 - 1 in 10 chance of picing correct door
	door3 - where the player obtains the thing required for the final room
	door4 - fake door
	treasure room - the final room where teh player wins

"""

from sys import argv

script, story_name = argv

def door_1():
	dead("You thought you would be clever and pick each door in turn.\nUnfortunately the door leads to a gaping chasm.\nYou fall down the hole to your death.")

def door_2(instance = 1):

	if instance == 2:
		print("\n")

	else:
		print("There are 10 doors lined up.")
		print("9 of the doors are metal, and one of the doors is paper.")
		print("You must run full pace at one of the doors in order to break it.")
		print("Which door do you choose?")


	door = int(input("> "))

	if door > 11 or door <= 0:
		print("That was not one of the options given, please choose again.")
		door_2(2)
	elif door == 11:
		print("Okay smarty pants, you found a magic number, you can proceed.")
		treasure_room()
	elif door == 3:
		print("Phew, that was a paper door!")
		print("You may proceed.")
		treasure_room()
	elif door <= 2 or door >= 4:
		dead("That was a metal door. You break your neck. Ouch.")
	else:
		print("That was not one of the options given, please choose again.")
		door_2(2)


def treasure_room():

	global story_name_obtained

	print("You have made it! You have found the treasure room!")
	print("But wait, it turns out you need the ", story_name, "to proceed.")

	if story_name_obtained == True:
		print("\nLucky for you traveller, you alredy have it!")
		print("Take all the gold that your heart desires.")
		print("But beware, this level of wealth can corrupt even the most dignified travellers.")
		print("\n")
		print("YOU WIN")

	else:
		print("You will have to return to the original room to find it.")
		start(3)

def door_3(instance=1):

	global story_name
	global story_name_obtained

	if instance == 2:
		print("\n")

	elif story_name_obtained == True:
		print("You have completed your quest here, return to the original room.")
		start(3)

	else:
		print("This is the moment you have been searching for your whole life.")
		print("You see it sitting there behind a contraption:")
		print("The magnificent and glorious, unmistakable ", story_name)
		print("To release it, you must put your hand in one of three holes to pull a lever.")
		print("Which is the correct hole?")

	try:
		hole = int(input("> "))

		if story_name_obtained == False:

			if hole == 1:
				dead("Great, that was full of spiders. They chew your hands off.")
			elif hole == 2:
				dead("That was full of scorpions. You are stung to death.")
			elif hole == 3:
				print("You pull the lever and release the ", story_name, "!")
				print("But your journey is not over, and you must return to the orignal room to find the treasure.")
				story_name_obtained = True
				start(3)


	except ValueError:
		print("That's not an option ya doofus.")
		print("Please enter a number from 1 to 3.")
		door_3(2)



def door_4():
	print("There isn't really a door 4, I was just kidding.")
	print("Please choose again.")
	start(3)


def start(instance=1):

	if instance == 2:
		print("\n")

	elif instance == 3:
		print("Which door do you choose next?")

	else:
		print("\tLong Wina and the ", story_name)
		print("You are Long Wina, an adventurer looking for treasure in the catacombs of Paris.")
		print("You enter the network, where there are 5 doors.")
		print("Which door do you choose?")
	
	try:
		door = int(input("> "))

		if door == 1:
			print("You chose door 1.")
			door_1()
		elif door == 2:
			print("You chose door 2.")
			door_2()
		elif door == 3:
			print("You chose door 3.")
			door_3()
		elif door == 4:
			print("You chose door 4.")
			door_4()
		else: 
			print("That's not an option ya doofus.")
			print("Please enter a number from 1 to 5.")
			start(2)

	except ValueError:
		print("That's not an option ya doofus.")
		print("Please enter a number from 1 to 5.")
		start(2)


def dead(why):
	print(why, "\n \nGAME OVER")
	exit(0)

story_name_obtained = False

start()