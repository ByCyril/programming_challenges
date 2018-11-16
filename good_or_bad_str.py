

def good_or_bad(i):
	vowels = 'aeiuo'

	v = 0
	c = 0
	q = 0

	for s in i:
		if s in vowels:
			vowel_count += 1
			cont_count = 0
			q_marks = 0
		elif s not in vowels and s != '?':
			vowel_count = 0
			cont_count += 1
			q_marks = 0
		elif s == '?':
			q_marks += 1

		if cont_count + q_marks > 3 or vowel_count + q_marks > 5:
			return 0

	return 1





print(good_or_bad('a???ycgy?ips?ubxdkr?a?psiqrrs?ysysnrstiozvcvkbooj?jizy?chlrxgik?zxomjwzemz'))


print(good_or_bad('a?????baaaa?'))

 