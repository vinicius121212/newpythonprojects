#project for a store in python!

# prices and aditional info about them
item1 = {"item1" : 10}
item2 = {"item2": 20}
item3 = {"item3" : 100}

#defines the name of the items
menu = [item1 , item2, item3]

#adds quit button to menu
menu.insert(0, {"quit":"quits"})

#iterates the menu

for i in range(len(menu)):
	for key, value in menu[i].items():
		print(i, key)

#checks for order input
while True:
	try:
		order = int(input("what are you interested in"))
		order = (menu[order].items)

		for key, value in order():
			print("$", value)
			amount = int(input("how much do you want?"))
			price = amount * value 
			print(price)
	
	except ValueError:
		print("use numbers only")

