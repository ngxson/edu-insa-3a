# True if p is empty
# else, check if False is NOT in this dict
# dict has 1 element, can be either True or False
# and it is True when p[j] == p[len(p)-j-1]
# that means p is palindrome
f = lambda p : \
    True if len(p) == 0 \
    else not False in \
    {True if p[j] == p[len(p)-j-1] \
    else False for j in range (len(p)//2)}
# it is correct

# simplified version
def f(p):
    return all( p[j] == p[len(p)-j-1] for j in range (len(p)//2) )

assert f([]) == True
assert f([1]) == True
assert f([1,2]) == False
assert f([1,1]) == True
assert f([1,1,1]) == True
assert f([1,2,1]) == True
assert f([1,2,2,1]) == True
assert f([1,2,3,1]) == False
assert f([1,2,3,2,1]) == True