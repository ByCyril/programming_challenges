


def maximize(A):
	stack = [0]
	results = [0]
	i = 1
	
	while i < len(A):
	
		a = A[i]
		if stack[-1] < a:
			results.append(stack[-1])
			stack.append(a)
			i += 1
		else:
			del stack[-1]

	print(A)	
	print(results)
		

maximize([0,6,8,2,4,9,7,3,5,1,92])
