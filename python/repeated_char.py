# Programmer: Cyril Garcia
# Date: November 15, 2018
# Problem description: https://practice.geeksforgeeks.org/problems/repeated-character/0

def repeated_char(s):
	i = 0

	for c in s:
		if c in s[i:]:
			return c
		else:
			i += 1

	return -1


res = repeated_char('yhkoryenollwpjwqquwigwnebvypnigmpsdjtjylu')
print(res)