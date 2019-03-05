
# Remove all duplicates


def uniqueVals(nums):
	vals = {}
	uVals = []
	
	for i in range(0, len(nums)):
		if nums[i] not in vals:
			vals[nums[i]] = 1
		else:
			vals[nums[i]] = 2
	
	
	for val in vals.keys():
		if vals[val] == 1:
			uVals.append(val)
	
	return uVals
	
			
		
		
	

vals = uniqueVals([7, 7, 1, 8, 8, 9, 4, 2, 2])
print(vals)

