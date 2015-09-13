import sys

if len(sys.argv) > 1:
	
	for arg in sys.argv[1:]:
	
		try:
			if type(int(arg)) is int:
				n = int(arg)
		except ValueError:
			print "Please use integers."
			quit()
			
		if type(int(arg)) is int:
				n = int(arg)
		
		x = 1

		print "Fizz buzz counting up to " + str(n)
		
		while x <= n:
			if x % 3 == 0:
				print "Fizz"
			if x % 5 == 0:
				print "Buzz"
			if x % 3 == 0 and x % 5 == 0:
				print "FizzBuzz"
			print str(x)
			x += 1

if len(sys.argv) == 1:
	
	user_input = raw_input("Please enter number for FizzBuzz to count up to: ")

	try:	
		if type(int(user_input)) is int:
			n = int(user_input)
	except ValueError:
		print "Please enter a number."
		user_input = raw_input("Please enter number for FizzBuzz to count up to: ")
	
	if type(int(user_input)) is int:
			n = int(user_input)
	x = 1

	print "Fizz buzz counting up to " + str(n)
			
	while x <= n:
		if x % 3 == 0:
			print "Fizz"
		if x % 5 == 0:
			print "Buzz"
		if x % 3 == 0 and x % 5 == 0:
			print "FizzBuzz"
		print str(x)
		x += 1