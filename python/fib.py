# Programmer: Cyril Garcia
# Date: November 10, 2018

# Print the nth fib number

def fib(n):
	if n < 0:
		return 0
	elif n ==  1:
		return 1
	else:
		a = 0
		b = 1
		t = 0
		for i in range(1,n):
			t = a + b
			a = b
			b = t
		return t


a = fib(6)
print(a)