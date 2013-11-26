#a solution to the monty hall paradox. Shows that you should always switch
#runs each 10,0000 times to get a fairly stable 33/66 split
#increase xrange for an even better approximation

from __future__ import division
import random



#returns percentage of wins without switching
def monty_stay():
	win = 0
	tries = 0
	for x in xrange(1,10000):
		doors = ["goat", "goat", "goat"]
		prize_door = random.randint(0,2)
		doors[prize_door] = "prize"
		if doors[0] == "prize":
			win += 1
		tries += 1
	
	return "same door win rate: " + str(((win/tries) * 100))

#returns percentage of wins always switching
def monty_switch():
	win = 0
	tries = 0
	for x in xrange(1,10000):
		doors = ["goat", "goat", "goat"]
		prize_door = random.randint(0,2)
		doors[prize_door] = "prize"
		user_door = random.randint(0,2)
		if doors[0] == "prize" and user_door == 0:
			user_door = 1
		elif doors[1] == "prize" and user_door == 1:
			user_door = 0
		elif doors[2] == "prize" and user_door == 2:
			user_door = 0
		elif doors[0] == "goat" and user_door == 0:
			user_door = prize_door
		elif doors[1] == "goat" and user_door == 1:
			user_door = prize_door
		elif doors[2] == "goat" and user_door == 2:
			user_door = prize_door

		if doors[user_door] == "prize":
			win += 1
		tries += 1
	return "switch door win rate: " + str(((win/tries) * 100))


print monty_stay()
print monty_switch()