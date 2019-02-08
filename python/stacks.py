
# Get the smallest number in a stack in constant time.

nums = [3,8,5,2,-1,6]

stack = []
minStack = []

def push(n):
	if len(stack) == 0:
		stack.append(n)
		minStack.append(n)
	else:
		if stack[-1] >= n:
			stack.append(n)
			minStack.append(n)
		else:
			stack.append(n)

def pop():
	if len(stack) != 0:
		if stack[-1] == minStack[-1]:
			del stack[-1]
			del minStack[-1]
		else:
			del stack[-1]


def getMin():
	return minStack[-1]


push(8)
push(5)
push(6)
push(2)
push(4)
push(-1)
push(8)
push(-2)

pop()
pop()
pop()
print(getMin())
