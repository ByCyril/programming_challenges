# Programmer: Cyril Garcia
# Date: November 15, 2018

def binary(i):

	n = i
	results = ''

	while n >= 1:
		r = int(n) % 2
		results = str(int(r)) + results
		n = n / 2

	return results

i = ' '

while i != '':
	i = input('i = ')
	res = binary(int(i))
	print(res)