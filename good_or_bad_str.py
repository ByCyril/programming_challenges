

def good_or_bad(i):
	vowels = 'aeiuo'

	v = 0
	c = 0
	q = 0

	for s in i:
		if s in vowels:
			v += 1
			c = 0
			q = 0
		elif s not in vowels and s != '?':
			v = 0
			c += 1
			q = 0
		elif s == '?':
			q += 1
		print(v,c,q)
		if c + q >= 3 or v + q >= 5:
			return 0
	print(v,c,q)
	return 1





# print(good_or_bad('a???ycgy?ips?ubxdkr?a?psiqrrs?ysysnrstiozvcvkbooj?jizy?chlrxgik?zxomjwzemz'))
# print(good_or_bad('aeioup??'))
# print(good_or_bad('bcdaeiou??'))
# print(good_or_bad('a?????baaaa?'))
# print(good_or_bad('bbbbabbbb'))
# print(good_or_bad('t'))
print(good_or_bad('d?ea?glo?l?s'))

 