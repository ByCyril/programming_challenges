


def two_sums(nums, sum):

	head = 0
	tail = len(nums) - 1

	while head < tail:
		x = nums[head]
		y = nums[tail]
		sum_of_xy = x + y

		if sum_of_xy > sum:
			tail -= 1
		elif sum_of_xy < sum:
			head += 1
		else:
			return True

	return False

a = two_sums([2,3,4,4], 8)

print(a)