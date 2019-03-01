

def towers(h1, h2, h3):
	t1 = sum(h1)
	t2 = sum(h2)
	t3 = sum(h3)
	print(t1, h1)
	print(t2, h2)
	print(t3, h3)
	print("")
	while t1 != t2 or t1 != t3:
		
		if t1 >= t2 and t1 >= t3:
			t1 -= h1[0]
			del h1[0]
		elif t2 >= t1 and t2 >= t3:
			t2 -= h2[0]
			del h2[0]
		elif t3 >= t1 and t3 >= t2:
			t3 -= h3[0]
			del h3[0]
		print(t1, h1)
		print(t2, h2)
		print(t3, h3)
		print("")
			
	print(t1, h1)
	print(t2, h2)
	print(t3, h3)
			
			

	
tower1 = [1,4] #21
tower2 = [4, 10,1,1,2]	#15
tower3 = [2,4] #15

towers(tower1, tower2, tower3)


