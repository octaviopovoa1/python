# MS-DOS COMMAND AND FILEPATH
# python c:\Users\op300624\Documents\Python\opie.py

# IMPORTS
# OP-20170818: Importing platform to define system type, os to be able to clear screen according to system type and random to only add one master to the corresponding variable.
import platform
import os
import random

# FUNCTIONS
# OP-20170818: Creating 4 functions to separate the selection logic from the outcome. These functions define what happens after the user makes a choice.

def clear_screen():
# OP-20170818: Function to clear the screen separately from setting the system variable.
	if(system == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

def hello_world(): 
# OP-20170818: Function to say hello worls and get another choice input.
	print("\t\tResult: Hello World !")
	input()
	clear_screen()
	user_selection()

def your_name(): 
# OP-20170818: Function to say the user name and get another choice input.
	print("\t\tResult: Hi there",name,"!")
	input()
	clear_screen()
	user_selection()

def random_master():
# OP-20170822: Adding 1 random Jedi Master name to the corresponding variable. Moved into function so we can run this multiple times.
# OP-20170901: Expanded function to get another choice input after saying a Jedi Master name.
	master = random.choice(["Peet-Er Drucker","Tai-Chii Ohno","Stee-Vh Covey","Sai-Mon Sinek","Obi-Wan Kenobi","Sy-Fo Dyas","Luke Skywalker"])
	print("\t\tResult: Word To The Jedi Master Of The Day,",master,"!")
	repeat_master = input("\nChoose an option, please...\n\t0 = Another One\n\tAny Other Key = Go Back\nWhat is thy bidding, my mastah? ")
	if(repeat_master == "0"):
		random_master()
	else:
		clear_screen()
		user_selection()

def fortune_cookie():
# OP-20170901: Adding one more function to share eternal wisdom and get another choice input.
	fortune = random.choice(["don’t panic ...","Hot & Sour Soup is the best !","it could be better, but it’s good enough ...","you will find a thing - it may be important ...","two days from now, tomorrow will be yesterday ...","stop eating now - food poisoning no fun ...","RUN !!!","the fortune you seek is in another cookie ...","you will be hungry again in one hour ...","not every fox that has a wet tail has crossed the creek ...","Futo Buta !!!"])
	print("\t\tResult: Confucious says",fortune)
	repeat_fortune = input("\nChoose an option, please ...\n\t0 = Another One\n\tAny Other Key = Go Back\nWhat is thy bidding, my mastah? ")
	if(repeat_fortune == "0"):
		fortune_cookie()
	else:
		clear_screen()
		user_selection()

def flavor_of_the_day():
# OP-20170822: Adding 1 random mood to the corresponding variable. Moved into function so we can run this multiple times.
# OP-20170901: Expanded function to get another choice input after saying a memorable DE/NH quote.
	mood = random.choice(["Everything is wrong","This solution is full of holes, Wayne","You cannot change anything","Ask Uncle Bob","Evil-A-Dub will unblock it","I decided last week and forgot to tell you","They realized that they never needed/wanted it","That is great, but I am out this week","I don't think we need to change that"])
	print("\t\tResult: Out of nowhere the boss turns around and says -",mood,"!")
	repeat_flavor = input("\nChoose an option, please...\n\t0 = Another One\n\tAny Other Key = Go Back\nWhat is thy bidding, my mastah? ")
	if(repeat_flavor == "0"):
		flavor_of_the_day()
	else:
		clear_screen()
		user_selection()

def good_bye():
# OP-20170901: Adding one more function to share eternal wisdom and get another choice input.
	print("\t\tResult: The Force Is Strong With This One ! Goodbye !")

def user_selection():
# OP-20170818: Asking the user to select an option and running the corresponding option function.
	selection = input("Choose an operation, please...\n\t1 = Say Hello\n\t2 = Say My Name\n\t3 = Random Jedi Master Shoutout\n\t4 = Fortune Cookie Fortune\n\tAny Other Key = Go Away\nWhat is thy bidding, my mastah? ")
	print("\tYou selected",selection)
	if(selection == "1"):
		hello_world()
	elif(selection == "2"):
		your_name()
	elif(selection == "3"):
		random_master()
	elif(selection == "4"):
		fortune_cookie()
# OP-20170822: Adding 1 easter egg option, just for fun
	elif(selection == "8"):
		flavor_of_the_day()
	else:
		good_bye()

# VARIABLES & CORE LOGIC
# OP-20170918: Adjusting comments in this section.

system = platform.system()
# OP-20170818: Identifying the system platform and calling the clear screen function.
clear_screen()

name = input("What is your name? ")
# OP-20170818: Asking the user for his/her name, to be used in one of the options. Firing the main routine.
user_selection()