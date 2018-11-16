

def max_tip(X,Y,A,B):

	total_tip = 0
	remaining = 0

	for a,b in zip(A,B):
	
		if a > b and X > 0:
			total_tip += a
			X -= 1
		elif a > b and Y > 0:
			total_tip += b
			Y -= 1
		elif a < b and Y > 0:
			total_tip += b
			Y -= 1
		elif a < b and X > 0:
			total_tip += a
			X -= 1
		elif a == b:
			remaining += b
			
	return total_tip + remaining


m1 = max_tip(1, 4, [5,5,5,5,5], [1,1,1,1,1])
m2 = max_tip(4,4, [1, 2, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8])


print(m1)


