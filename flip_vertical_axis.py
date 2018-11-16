# Programmer: Cyril Garcia
# Date: November 10, 2018
# Challenge Description: Create a function that will flip a 
# matrix from its vertical axis and another function that will
# flip a matrix from its horizontal axis

def flip_vertical_axis(matrix):
	# Create a temporary array
	temp_array = []

	# Iterate through each row of the matrix
	for row in matrix:
		head = 0
		tail = len(row) - 1
		# Swap elements from one end of the row to the other
		while head < tail:
			temp = row[head]
			row[head] = row[tail]
			row[tail] = temp
			head += 1
			tail -= 1
		
		# Append the flipped array to the tempArray
		temp_array.append(row)

	# Return the array
	return temp_array

def flip_horizontal_axis(matrix):
	m = matrix
	upperBound = int(len(m) / 2)

	for i in range(0, upperBound):
		temp = m[i]
		m[i] = m[len(m) - i - 1]
		m[len(m) - i - 1] = temp

	return m

matrix = [[1,2,3,4],[5,6,7,8]]
a = flip_vertical_axis(matrix)
b = flip_horizontal_axis(matrix)
print(a)
print(b)