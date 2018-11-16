# Programmer: Cyril Garcia
# Date: November 11, 2018
# Challenge Description: Given a list of sorted numbers increasing by one, find the nth missing number.


def missing_num(nums, n):
	checker = nums[0]
	flag = 0
	i = 0
	
	while i < len(nums):
		num = nums[i]

		if checker == num:
			i += 1
			checker += 1
		else:
			flag += 1

			if flag == n:
				return checker
			else:
				checker += 1

	return -1


print(missing_num([1,2,5,7,8,10], 0))