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

def print_menu():

	for i in range(len(menu)):

		for key, value in menu[i].items():
			print(i, key)

#print menu
print_menu()

#checks for order input
while True:
	try:
		order = int(input("what are you interested in"))
		orderitem = (menu[order].items)
		def itemname():
			for key , value in menu[order].items():
				print(key)

#prints price
		for key, value in orderitem():
			print("$", value)
			amount = int(input("how much do you want?"))
			price = amount * value 
			print("the price is $", price ,)
			#creates a cart with customer items
			menu.append( {"cart" : [menu[order].keys() , amount , price]})
			for key , value in menu[-1].items():
				print (value)

			print_menu()

#validates user input	
	except ValueError:
		print("use numbers only")

	except IndexError:
		print(f"item not avaliable, insert items from 0 to", len(menu))
