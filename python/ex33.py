2+2
# on obtiens 4, mais il n'affiche rien

print(2+2)
# la fonction print retourne None, et il affiche 4 sur stdout

print(print(2+2), print(2+2))
# comme la commande précedente, elle affiche 2 fois le numéro 4
# et puis, elle affiche les résultats de "print", qui sont None

l= [ 1+i for i in range(3) ]
# l est une liste de 3 int: 1, 2, 3
# la commande affiche rien

pl = [ print(1+i) for i in range(3) ]
# print(1+i) affiche 1, 2, 3, et elle renvoie None
# l est une list de 3 Nones

print(l,pl)
# la commande affiche [1, 2, 3], qui est l
# et [None, None, None], qui est pl
