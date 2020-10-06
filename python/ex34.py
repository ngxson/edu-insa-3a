print(set('totto'))
# erreur car set([iterable])
# on doit écrire set(('totto'))

print({'totto'})
# affiche {'totto'}

print({{'toto'}, {'tata'}})
# TypeError: unhashable type: 'set'

print('abcde'[-1])
# affiche 'e'

print({'abcde'}[0][1])
# erreur car 'set' n'a pas de ordre

print('abcdefg'[2:5])
# affiche 'cde'

print((list('abcdefg')*3)[2:5])
# list('abcdefg') = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# list('abcdefg')*3 = ['a', ..., 'g', 'a', ..., 'g', 'a', ..., 'g']
# affiche ['c', 'd', 'e']

print((list('abcdefg')*3)[19:22])
# on prends l'indice 19, 20, 21
# mais l'indice 21 n'existe pas
# il affiche ['f', 'g']

print('abcdefg'[-5:-2])
# affiche 'cde'

print( list(range(12))[13:5:-2] )
# on va de 13 à 6 par pas de -2
# donc on prend 11, 9, 7
# affiche [11, 9, 7]

print({0:1, None:2, False:5})
# parce que: False.__hash__() = 0
# et int(0).__hash__() = 0
# donc la valeur de 0:1 est remplacé par False:5

s = { print(i) for i in range(1,3) }
# s = {None}
# et il affiche
# 1
# 2

ss = { (i,print(i)) for i in range(1,3) }
# ss = { (1, None), (2, None) }
# et il affiche
# 1
# 2

sss = { (i,i,print(i)) for i in range(1,3) }
# sss = { (1, 1, None), (2, 2, None) }
# et il affiche
# 1
# 2

print(s,ss,sss,sep='\n')
# {None}
# { (1, None), (2, None) }
# { (1, 1, None), (2, 2, None) }
