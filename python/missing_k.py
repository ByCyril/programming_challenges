


def findMissing(N, k):
	nKeys = {}
	min = N[0]
	max = N[0]
	
	for n in N:
		nKeys[n] = 1
		
		if n < min:
			min = n
		elif n > max:
			max = n
			
	count = 0
	for i in range(min, max + 1):
		if i not in nKeys.keys():
			count += 1
		if count == k:
			return i 
			
	return -1	


print(findMissing([2,4,10,7],1))			
print(findMissing([2,4,10,7],2))			
print(findMissing([2,4,10,7],3))			
print(findMissing([2,4,10,7],4))					
print(findMissing([2,4,10,7],5))
print(findMissing([2,4,10,7],6))