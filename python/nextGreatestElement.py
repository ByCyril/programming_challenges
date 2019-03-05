

# Find the first greatest element

def nextGreatestElement(N):
	stack = [N[-1]]
	results = [-1]
	i = len(N) - 2
	
	while i >= 0:
		if N[i] > stack[-1]:
			del stack[-1]
		else:
			results = [stack[-1]] + results
			stack.append(N[i])
			i -= 1
			
		if len(stack) == 0:
			results = [-1] + results
			stack.append(N[i])
			i -= 1
		
	print(results)

	
nextGreatestElement([4,5,2,25,10])
nextGreatestElement([1,2,3,4,5,6,7,6,10])

	