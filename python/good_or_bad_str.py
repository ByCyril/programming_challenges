

def good_or_bad(i):
	vowels = 'aeiuo'

	v = 0
	c = 0

	for s in i:
		if s in vowels:
			v += 1
			c = 0

		elif s not in vowels and s != '?':
			v = 0
			c += 1

		elif s == '?':
			v += 1
			c += 1

		if c > 3 or v > 5:
			return 0

	return 1





# print(good_or_bad('a???ycgy?ips?ubxdkr?a?psiqrrs?ysysnrstiozvcvkbooj?jizy?chlrxgik?zxomjwzemz'))
# print(good_or_bad('aeioup??'))
# print(good_or_bad('bcdaeiou??'))
# print(good_or_bad('a?????baaaa?'))
# print(good_or_bad('bbbbabbbb'))
# print(good_or_bad('t'))
print(good_or_bad('d?ea?glo?l?s'))
print(good_or_bad('dvgup?'))

 