

def sum67(nums):

	s = 0
	stop = False

	for num in nums:
		if stop == False:
			if num != 6:
				s += num
			else:
				stop = True
		else:
			if num == 7:
				stop = False

	return s

print(sum67([1,2,2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))