

def transpose(m):
	matrix = m 

	row = 0
	column = 0
	n = len(matrix)

	while column < n:
		if row >= column:
			row = 0
			column += 1

			if column == n:
				break

		temp = matrix[column][row]
		matrix[column][row] = matrix[row][column]
		matrix[row][column] = temp

		row += 1

	return matrix


trans = transpose([[1,2,3],[4,5,6],[7,8,9]])

for t in trans:
	print(t)