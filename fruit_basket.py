


fruit_basket = ["orange", "apple", "watermelon", "grape", "cherry"]


def guess_fruit(i):
		
	if i < 5:	
		guess = raw_input("Guess what fruit is in the basket.\n")
	

		if guess in fruit_basket:
			print ("correct")			
			return

		else:
   			i += 1
			guess_fruit(i)
	
	else:
		print ("wrong")
		return

guess_fruit(0)
