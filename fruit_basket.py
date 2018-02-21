


fruit_basket = ["orange", "apple", "watermelon", "grape", "cherry"]
guess = raw_input("Guess what fruit is in the basket.\n")
i = 0
for i in range(0,6,1):

	if guess in fruit_basket:
		print "correct"

	elif i <= 5:
		print "guess again\n"


	else :
    		print "wrong"
	



