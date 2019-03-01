

deque = []

def prepend(e):
	global deque
	deque = [e] + deque

def append(e):
	deque.append(e)

def pop():
	if len(deque) > 0:
		e = deque[0]
		del deque[0]
		return e
	else:
		return None

def get(i):
	s = ""

	while i > 0:
		p = pop()

		if p != None:

			if len(p) > i:
				s += p[:i]
				p = p.replace(p[:i],"")
				prepend(p)
				break
			else:
				s += p
				i -= len(p)
		else:
			return s

	return s





append("123")
append("45")
append("6789")

print(get(1))
print(deque)

print(get(2))
print(deque)

print(get(3))
print(deque)

print(get(4))
print(deque)
