


def isBalanced(s):
    dict = {'[': 1, '(': 2, '{': 3, ']': -1, ')': -2, '}': -3}
    stack = []

    for i in range(0, len(s)):
        char = s[i]
        if char in dict:
            bracketCode = dict[char]
            
            if bracketCode > 0:
                stack.append(bracketCode)
            else:
            	if len(stack) > 0:
            		if (bracketCode * -1) == stack[-1]:
            			del stack[-1]
            		else:
            			return "NO"
            	else:
            		return "NO"



                    
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


r = isBalanced(testCase)

print(r)