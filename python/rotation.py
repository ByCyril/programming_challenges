
A = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
B = [[1]]
C = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(A):
	matrix_size = len(A)
	number_of_levels = int(matrix_size / 1)
	last = matrix_size - 1

	for level in range(0, number_of_levels):
		for i in range(level, last):
			
			swap(level, i,i, last, A)
			swap(level, i,last, ((last - i) + level), A)
			swap(level, i,((last - i) + level), level, A)

		last -= 1

	return A

def swap(x1, y1, x2, y2, A):
	temp = A[x2][y2]
	A[x2][y2] = A[x1][y1]
	A[x1][y1] = temp  




for r in rotate(C):
	print(r)