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

#2.22
res=[]
for N in range(1,1000):
    bin_n=bin(N)[2:]
    if N%3==0:
        bin_n+="000"
    else:
        bin_n+=bin(N%3*3)[2::]
    res.append(int(bin_n, 2))
print(*res)
res.sort()
max_amount=-1
for left in range(len(res)-1):
    for right in range(left+1, len(res)):
        if res[right]-res[left]<=60:
            max_amount=max(max_amount, right-left)
print(max_amount)
