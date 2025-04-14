#6
# la=(3**2+1**2)**0.5
# lb=((-2)**2+6**2)**0.5
# lc=((-1)**2+(-7)**2)**0.5
# p=0.5*(la+lb+lc)
# print((p*(p-la)*(p-lb)*(p-lc))**0.5*100)
#ответ 999
from ast import iter_child_nodes
# rm=0
# for i in range(1,30):
#     n=2**i
#     if n<10**9:
#         nb=bin(n)[2::]
#         if nb.count('0')>0.5*len(nb):
#             nb=nb.replace('0','1',1)
#         else:
#             nb=nb[::-1]
#             nb = nb.replace('1', '0', 1)
#             nb = nb[::-1]
#         r=abs(n-int(nb,2))
#         if r>rm:
#             print(n, r) # заметим, что макс r при n=2**i
#             rm=r
# n: 536870912

from itertools import*
# c=0
# for l in range(2, 12):
#     for i in combinations('123456789AB',l): #считаем комбитации, тк нужны наборы с уникальными символами
#         c+=1
#         print(i)
# print(c)

# alph='0123456789ABCDEF'
# for p in range(11,17):
#     for x in alph[:p]:
#         for y in alph[:p]:
#             for z in alph[:p]:
#                 if x!='0' and z!='0':
#                     if int(z+x,p)+int(x+y,p)==int(z+y+'A',p):
#                         print(int(x+y+z,p))
#1211


#оптимизация
# def f(x):
#     p= 264952<=x<= 356809
#     q= 306963<=x<= 942523
#     r= 792550<=x<= 970061
#     a= a1<=x<=a2
#     return q<=((p or r)<=a)
#
# ox=[i/4 for i in range(264952*4, 970062*4)]
# print('ox')
# r=[]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         r.append(a2-a1)
# print(min(r))

# from fnmatch import*
# for i in range(9111, 10**9, 9111):
#     if fnmatch(str(i), '4?28*8*3'):
#         print(i)

# f=open('C:/Users/tolab/PycharmProjects/EGE/statgrad/files/09.csv')
# res=0
# for i in f:
#     nums=[int(x) for x in i.split(';')]
#     sr_znach=sum(nums)/8
#     chet=[x for x in nums if x%2==0]
#     nechet=[x for x in nums if x%2!=0]
#     iteres_chet=sum(x>sr_znach for x in chet)
#     iteres_nechet = sum(x > sr_znach for x in nechet)
#     res+= iteres_chet>iteres_nechet and sum(chet)<sum(nechet)
# print(res)


#20 21
def moves(x):
    res=[1,x]
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            res.append(i)
            if i!=x//i:
                res.append(x//i)
    return res

from sys import *
setrecursionlimit(99999999)
def f(s,e):
    if s>=92: return True
    if e==0: return False
    act=[]
    z=moves(s)
    for i in z:
        act.append(f(s+i, e-1))
    return any(act) if (e-1)%2==0 else all(act)

print([s for s in range(1,92) if f(s,2)])
print([s for s in range(1,92) if f(s,3) and not(f(s,1))])
print([s for s in range(1,92) if f(s,4) and not(f(s,2))])