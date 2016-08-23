control_main=1
control_1=0
control_2=0
control_3=0
control_4=0
control_5=0
while control_main:
	print """Welcome to the Python Pokedex!
		1: Name Search
		2: Type Search
		3: Number Search (By Regional Dex)
		4: Game Search
		5: Image Search (Red through Generation V sprites only)
		"""
	user_input = input("How would you like to look up your Pokemon? ")
	print "%s? That's badass!" % user_input
	if user_input:
		control_main=0
		print "Detected user input, closing program."
