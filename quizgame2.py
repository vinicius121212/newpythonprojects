#quizgame2.py

#defines an ammount of points
points = 0

#creates a function that enumerates the alternatives, grabs the answer and adds points, the whole game is in this very simple function
def alternatives_func(list , correct):
	for count, element in enumerate(list, start=1):
		print(count , element)
	answer = int(input("whats your answer?"))
	if answer == correct:
		print("ayyy ya got it")
		global points	 
		points = points + 1

	else:
		print("wrong")


#starts the game

start = input("this is my python quiz Game, press anything to start")

#questions

print("1. which of the following are integers?")

alternatives_func(["'1'" , "1" , "0.1"] , 2)


print("1. which of the following are strings?")

alternatives_func(["'strings'" , "strings" , "True"], 1)

print(points)