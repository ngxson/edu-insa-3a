from math import sqrt, floor

def isqrt_builtin(n):
	return floor(sqrt(n))

def test(f):
	for n in range(100):
		assert f(n) == isqrt_builtin(n)

def isqrt_hard(n):
	i = 0
	while (i+1) ** 2 < n + 1:
		i = i+1
	return i

test(isqrt_hard)

def isqrt_sum(n):
	s = 0
	if n <= 1:
		return 0 if n == 0 else 1
	for k in range(1, n + 1):
		s = s + (k + k - 1)
		# Sn is now equals k ** 2
		if s > n:
			return k - 1

test(isqrt_sum)

def isqrt_dicho(n):
	L = 0
	R = n
	while L != R:
		m = (L+R) // 2 + 1
		if m ** 2 <= n:
			L = m
		else:
			R = m - 1
	return L

test(isqrt_dicho)

