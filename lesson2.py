def change_sys(num, base):
    res=""
    alph = "qwertyuiopasdfghjklzxcvbnm"
    list(alph).sort
    alph= "0123456789"+alph
    while num>0:
        res = alph[int(num%base)] + res
        num=num//base
    return res
print(change_sys(5,25))

from itertools import *

alph="abcd"
alph2="efgh"
res=product(alph, repeat=3)#размещение
res=permutations(alph)#перестановка
res= combinations(alph, 2)#сочитания
res= combinations_with_replacement(alph, 2)#сочитания с повтором
for i in res:
    print(''.join(i))

