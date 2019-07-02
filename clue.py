import random
import Tkinter
people = ["Ruby","Robert","Jessica","Heather","Mitchell","Daniel","Dr.Orchard"]
rooms = ["Living room", "Guest Bedroom","Balcony","Office","Courtyard","Kitchen","Cellar"]
weapons = ["Dagger","Revolver","Candlestick","Wrench","Poison","Lead Pipe"]
random.shuffle(people)
killer = random.choice(people)
people.remove(killer)
random.shuffle(rooms)
room = random.choice(rooms)
rooms.remove(room)
random.shuffle(weapons)
weapon = random.choice(weapons)
weapons.remove(weapon)
print("Welcome to the game of clue!")
print("\n\n\n")
print("Last night, Mr. White, the owner of the Catshiere Hotel was killed. He was last seen in his house, Marriot Gardens, \n along with his friends, Ruby, Robert, Jessica, Heather, Mitchell, Daniel and Dr. Orchad, who are all suspected of killing him.\n")
print("You are the best detective in town and it is your job to solve this mystery, but don't delay, your enemies are also \n trying to solve this crime, and if they succeed, you will be framed for this crime and your status will be invoked.")
print("In order to solve this crime, you must find the place were Mr. White was killed, what weapon was used to kill him and who killed him. Good luck! And hurry!")
print("\n\n\n\n")
userSuppects = [ ]
userRooms = [ ]
userWeapons = [ ]
for i in range (3):
	userSuppects.append(people[i])
	userRooms.append(rooms[i])
	userWeapons.append(weapons[i])
print("Remember, cards you have don't have a link to Mr.White's death, because there is no evidence to support them. The suspects include, Ruby, Robert, Jessica, Mitchell, Daniel and Dr.Orchard.\n\n")
print("The possible weapons used to kill him are the dagger, the revolver, the candlestick, wrench, poison and the lead pipe. The rooms he could have been killed in are the living room, the bedroom, balcony, office, courtyard, kitchen and the cellar.")
print("You have to make a possible accusation every turn and a confirmed accusation when you know for certain what is happening. If your confirmed accusation is wrong, you will loose and your ememies will win. If you confirmed accusation is correct, you win!\n\n\n")
print("Here are your cards: ")
print(userSuppects)
print(userRooms)
print(userWeapons)
while True:
	Type = int(input("Type in a 1 for a possible accusation and a 2 for a confirmed accusation: "))
	if Type == 1:
		personName = raw_input("Please enter your suspect: ")
		if personName == killer:
			print("You have the right suspect!")
		else:
			print("You have the wrong suspect.")
		location = raw_input("Please enter the location where you think Mr.White was killed: ")
		if location == room:
			print("You have the right location!")
		else:
			print("You have the wrong location.")
		mode = raw_input("Please type in the weapon you think was used to kill Mr. White: ")
		if mode == weapon:
			print("You have the right weapon!")
		else:
			print("You have the wrong weapon.")
	elif Type == 2:
		person = raw_input("Please enter your final suspect:")
		location = raw_input("Please enter you final location: ")
		mode = raw_input("Please enter the final weapon used: ")
		if person == killer and location == room and mode == weapon:
			print("You have solved the mystery!")
			break;
		else:
			print("We are sorry to inform you that you have lost and that your enemies have beat you.")
			break;

