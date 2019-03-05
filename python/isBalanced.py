


def isBalanced(S):

	bracket_key = {'[': 1, '(': 2, '{': 3, ']': -1, ')': -2, '}': -3}
	stack = []

	for b in S:
		key = bracket_key[b]

		if key > 0:
			stack.append(key)
		elif abs(key) == stack[-1]:
			del stack[-1]
		else:
			return False

	return len(stack) == 0



print(isBalanced(testCase))
