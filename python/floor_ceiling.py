

def findFloorAndCieling(A,n):
	floor = -1
	cieling = -1
	
	x = 100
	y = 100
	
	for a in A:
		if a < n:
			if n - a < x:
				x = n - a 
				floor = a 
		elif a > n:
			if a - n < y:
				y = n - a 
				cieling = a 
		else:
			floor = a 
			cieling = a
			
	print(floor, cieling)


findFloorAndCieling([5, 6, 8, 9, 6, 5, 5, 6], 7)
findFloorAndCieling([5, 6, 8, 9, 6, 5, 5, 6], 6)
findFloorAndCieling([5, 6, 8, 9, 6, 5, 5, 6], 10)