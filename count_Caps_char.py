with open('/home/prachi/Python-Program/read_file.txt') as fh:
	caps_count = 0
	caps_list = []
	lower_count = 0
	lower_list = []
	text = fh.readline()
	for character in text:
		if character.isupper():
			print(character)
			caps_list.append(caps_count)
			count=+1
	
		if character.islower():
			print(character)
			lower_list.append(lower_count)
			lower_count=+1
	print("small Count:",lower_list)
	print("Caps Count:",caps_list)
