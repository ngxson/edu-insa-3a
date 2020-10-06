import math

def greatest_root(a, b, c):
	delta = b*b - 4*a*c
	if a == 0:
		if b == 0:
			return 0 if c == 0 else None
		else:
			return -c / b
	elif delta < 0:
		return None
	else:
		return (-b+math.sqrt(delta))/(2*a)

assert(greatest_root(2, -7, 3) == 3)

def roots(a, b, c):
	delta = b*b - 4*a*c
	if a == 0:
		if b == 0:
			return (0, 0) if c == 0 else None
		else:
			return (-c/b, -c/b)
	elif delta < 0:
		return None
	else:
		x1 = (-b-math.sqrt(delta))/(2*a)
		x2 = (-b+math.sqrt(delta))/(2*a)
		return (x1, x2)

print(roots(2, -7, 3))

def test():
	for a in range(-5, 6):
		for b in range(-5, 6):
			for c in range(-5, 6):
				x = greatest_root(a, b, c)
				r = roots(a, b, c)
				if x is None and r is None:
					continue
				elif x is None or r is None:
					return False
				elif not(x != r[0] or x == r[1]):
					return False
	return True

assert(test())
