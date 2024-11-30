from itertools import *
from math import floor

def change_sys(n,base):
    res=''
    while n>0:
        res=str(n%base)+res
        n=n//base
    return res

#1
# for i in range(2,10):
#     print(change_sys(636,i), i)

#2
# num=(5**2004)-(5**1016)-(5**400)+(25**250)
# print(change_sys(num,5).count("4"))

#3
# a=2*(3**30)+2*(3**25)+3**6+7*(3**4)+2*(9**2)+1
# print(change_sys(a,9).count("0"))

#4
# for x in range(6):
#     n1=f"12{x}35"
#     n2=f"1{x}243"
#     if (int(n1, 6)+int(n2,6))%5==0:
#         print((int(n1, 6)+int(n2,6))//5)
#         break

#5
# def sumnum(num):
#     res=0
#     for i in num:
#         res+=int(i)
#     return res
#
# for n in range(10000):
#     n_bin=bin(n)[2::]
#     n_bin=n_bin+str(sumnum(n_bin)%2)
#     n_bin = n_bin +str(sumnum(n_bin)%2)
#     if int(n_bin,2)>335:
#         print(n)
#         break

#6
# a=product("ЕНОТ", repeat=4)
# a=list(a)
# print(a[-225])

#7
# a=product("СЛОН", repeat=5)
# res=0
# for i in a:
#     if i.count("С")<=2:
#         res+=1
# print(res)

#8
#paint

#9
#обратное 100 - 011

#10
# print(bin(255)[2:])
# print(bin(103)[2:])
# print(bin(96)[2:])
# print(int("11111000"))
# print(int("11111000",2))

#11
# print(147&252, 2**4-2)

#16
# def f(x):
#     p=20<=x<=32
#     q=17<=x<=27
#     a=a1<=x<=a2
#     return (p<=a) and ((not q) or a)
# ox=[i/4 for i in range(17*4, 33*4)]
# z=[]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in range(10000)):
#         z.append(a2-a1)
# print(min(z))

#17
# def f(x):
#     return ((x%a==0)<=((x%15==0) or (x%23!=0))) and ((x+a)>=150)
# for a in range(1,10000):
#     if all(f(x) for x in range(1,10000)):
#         print(a)
#         break

#19
# def f(x,y,z,w):
#     return ((not x) or y) and (not(w<=z))
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0], val[1], 0, val[2]),
#         (0, val[3], 1, val[4]),
#         (1, val[5], val[6],0)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#                 print(p)

#20
# def f(x,y,z,w):
#     return (w<=y) and ((x<=z) == (y<=x))
#
# for val in product([0,1], repeat=4):
#     table=[
#         (val[0], 1, val[1], 0),
#         (0, val[2], 1, val[3]),
#         (0,1,0,1)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#                 print(p)