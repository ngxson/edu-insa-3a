def fahrenheit_to_celsius(F):
	return (F - 32) * 5 / 9

def celsius_to_fahrenheit(C):
	return C * 9 / 5 + 32

def isalmost(n, m, d=1):
	return abs(n - m) <= d

assert(celsius_to_fahrenheit(20) == 68)
assert(isalmost(fahrenheit_to_celsius(-459.67), -273.15, 1e-13))
