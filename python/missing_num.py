# Programmer: Cyril Garcia
# Date: November 11, 2018
# Challenge Description: Given a list of sorted numbers increasing by one, find the nth missing number.


def missing_num(nums, nth):
	i = 0
	flag = 0
	for n in range(nums[0], nums[len(nums) - 1] + 1):
		if n == nums[i]:
			i += 1
		else: 
			flag += 1

		if flag == nth:
			return n

	return -1

print(missing_num([1,2,5,7,8,10,15], 5))