#this python project manages and calculates prices for a shop on discord
#my plans are to connect this to a mail apiand have it calculate shipping
#keep in mind im fairly new and this is all part of my learning path



print ("hello and welcome to my shop! \n")

name= input ("what is your name?\n") 

#scammer check
if name == "scammer":
	scamcheck = input ("are you a scammer?")
	if scamcheck == "yes":
		exit()
	else:
	 print ("great")	

print( "hello " + name + " what would you like today?\n")

order = input ("we have:\n mushrooms\n kratom\n mimosa\n amanita\n")

if order == "mushrooms":
	mushrooms = input ("the price is 10$ a G, how much do you want?\n")
	print ( int(mushrooms) * 10)
elif order == "kratom":
	kratom = input ("the price is 5$ a G, how much do you want\n")
	print (int(kratom) * 5)  
	stealth = input ("do you want stealth shipping?")
	if stealth == "yes":
		print (int(kratom) * 5 + 5)
elif order == "mimosa":
	mimosa = input("the price is 50$ for 100g, how much do you want?\n")
	print (int(mimosa) * 50 )

elif order == "amanita":
	order = input("not in stock at thw moment, want something else?")


