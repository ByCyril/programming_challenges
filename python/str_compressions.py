

def str_compression(str_array):
	if len(str_array) == 0:
		return

	char_holder = str_array[0]
	counter = 0
	temp_array = []

	for i in range(len(str_array)):
		if char_holder == str_array[i]:
			counter += 1
		else:
			temp_array.append(char_holder + str(counter))
			counter = 1
			char_holder = str_array[i]

	return temp_array + [char_holder + str(counter)]


res = str_compression(['a', 'a','a','a','b','b','c','d','e','e','f'])
print(res)

