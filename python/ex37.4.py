from math import log10 as lg
from functools import reduce 

def isalpha(c):
    return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z')

assert all ( isalpha(chr(n)) ==chr(n).isalpha() for n in range(128) )
assert all (not isalpha(chr(n)) for n in range(128,256) )

def gramiter(s, n=4):
    return [s[i:i+n] for i in range(0, len(s)-n+1)]

assert tuple(gramiter("ATTACK")) == ('ATTA', 'TTAC', 'TACK')
assert tuple(gramiter("ATTACK",n=1)) == ('A', 'T', 'T', 'A', 'C', 'K')

def process(text="WP.txt", out="quads.txt"):
    d = dict()
    with open(text, 'r', encoding='utf-8') as reader:
        content = reader.read()
        content = content.upper()
        content = ''.join([c for c in content if isalpha(c)])
        quad_gram = gramiter(content)
        for word in quad_gram:
            d[word] = d[word] + 1 if word in d else 1
    with open(out, 'w', encoding='utf-8') as writer:
        words = list(d.items())
        words = sorted(words, key=lambda x: x[1], reverse=True)
        words = [x[0] + ' ' + str(x[1]) for x in words]
        writer.write('\n'.join(words))

#process()

def load_grams(fname="quads.txt"):
    with open(fname, 'r', encoding='utf-8') as reader:
        content = reader.read()
        content = content.split('\n')
        content = [x.split(' ') for x in content]
        content = [(x[0], int(x[1])) for x in content]
        return dict(content)

C = load_grams()

def score(s, C=C):
    st = s.upper()
    st = ''.join([c for c in st if isalpha(c)])
    quad = gramiter(st)
    occurences = [C[word] if word in C else 0 for word in quad]
    N = sum(occurences)
    P = reduce( \
        (lambda x, y: x * y), \
        [o/N if o != 0 else 1/(100*N) for o in occurences] \
    )
    L = sum(lg(o)/N for o in occurences if o != 0)
    return (N, P, L)

print(score('THISISACOHERENTSENTENCE'))