


def fine(d,c,p):

	# 0 = even
	# 1 = odd
	c = c.split(' ')
	p = p.split(' ')
	odd_even = d % 2
	total_fine = 0

	for i in range(0, len(c)):
		car_num = int(c[i])

		if car_num % 2 != odd_even:
			total_fine += int(p[i])

	return total_fine

t = fine(11, '2375 7682 2325 2352', '250 500 350 200')
t2 = fine(8, '2222 2223 2224', '200 300 400')

print(t, t2)
