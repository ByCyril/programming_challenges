# Programmer: Cyril Garcia
# Date: November 11, 2018
# Challenge Description: Given a list of sorted numbers increasing by one, find the nth missing number.


def missing_num(nums, nth):
	if nth >= nums[len(nums) - 1] - 1:
		return -1

	i = 0
	flag = -1
	for n in range(nums[0], nums[len(nums) - 1]):

		if n == nums[i]:
			i += 1
		else: 
			flag += 1

		if flag == nth:
			return n

	return -1

print(missing_num([1,15], 0))