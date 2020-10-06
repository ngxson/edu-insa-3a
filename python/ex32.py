import math

# prod_cartesien

def prod_cartesien(A, B):
    return { (x, y) for x in A for y in B }

assert prod_cartesien('ABC', {0, 1, 2}) == {('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('B', 2),
('C', 0), ('C', 1), ('C', 2)}

# squares

def squares(n):
    return [ i**2 for i in range(1, n) if i**2 <= n ]

assert squares(100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# palindrome
def palindrome(l):
    return all( l[i] == l[-i-1] for i in range(len(l)) )

assert palindrome('abba')
assert palindrome('abcba')
assert palindrome('')
assert palindrome('a')
assert not palindrome('ab')

# inverse

def inverse(s):
    return [s[-i-1] for i in range(len(s))]

assert inverse('abc') == ['c', 'b', 'a']
assert inverse('') == []

# palinv

def palinv(s):
    return list(s) == inverse(s)

assert palinv('abba')
assert palinv('abcba')
assert palinv('')
assert palinv('a')
assert not palinv('ab')

# rmfrom

def rmfrom(s, bad):
    return [c for c in list(s) if c not in bad]

assert rmfrom('esope reste ici et se repose', 'aeiouy ') == ['s', 'p', 'r', 's', 't', 'c', 't', 's', 'r', 'p', 's']

# rmspaces

def rmspaces(s):
    return rmfrom(s, ' ')

assert rmspaces('esope reste ici et se repose') == [ 'e', 's', 'o', 'p', 'e', 'r', 'e', 's', 't',
'e', 'i', 'c', 'i', 'e', 't', 's', 'e', 'r',
'e', 'p', 'o', 's', 'e']

# palindrome_sentence

def palindrome_sentence(s):
    return palindrome(rmspaces(s))

assert palindrome_sentence('esope reste ici et se repose')
assert not palindrome_sentence('esope reste ici et se reposes')

# fsum

def fsum(f, i, j):
    return sum(f(k) for k in range(i, j+1))

assert fsum(lambda i:i, 0, 10) == 55
assert fsum(lambda i:i**2, 0, 10) == 385

######################

# isprime

def isprime(n):
    #return [i for i in range(2, n) if n % i == 0] == []
    return all( n % i != 0 for i in range(2, n) )

assert isprime(10007)
assert not isprime(10001)

comp = lambda n : { i for i in range(2, n + 1) if not isprime(i) and i <= n }

comp2 = lambda n : { k*i for k in range(2, n) for i in range(k, n) if k*i <= n }

comp3 = lambda n : { i*j for i in range(2, n) for j in range(2, n) if i*j <= n }

n = 100
assert comp(n) == comp2(n) == comp3(n), (comp(n)^comp2(n), comp(n)^comp3(n))

# primes

primes = lambda n : tuple( k for k in range(1, n+1) if k not in comp(n) )

assert primes(100) == tuple( k for k in range(1, n+1) if isprime(k) )

# crange

crange = lambda a, b : list(chr(i) for i in range(ord(a), ord(b) + 1))

assert "".join(crange('A','Z')) == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def charrange(*args):
    for i in range(len(args) // 2):
        a, b = args[i*2], args[i*2+1]
        yield from crange(a, b)

assert "".join(charrange('A','Z','a','z','0','9')) == \
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
assert "".join(charrange()) == ''

