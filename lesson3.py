from itertools import *
alph=sorted("УРОК")
# a=list(product(alph, repeat=4))
# print(a.index(('И', 'Т', 'М', 'О'))+1)
ind=1
res=[''.join(el) for el in product(alph, repeat=4)]
for el in res:
    if "К" not in el and "ОО" not in el:
        print(ind)
        break
    ind+=1

#3.21
print(len([el for el in product('01', repeat=4) if el.count("1")==2]))
