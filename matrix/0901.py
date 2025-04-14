from itertools import *

#
# def f(x,y,z,w):
#     return ((x<=y)<=z) or (not w)
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0], 0,val[1], 0),
#         (1, val[2], val[3], val[4]),
#         (0,1,val[5], val[6])
#     ]
#     if len(table)==len(set(table)):
#         for i in permutations("xyzw"):
#             if [f(**(dict(zip(i, row)))) for row in table] == [0,0,0]:
#                 print(i)

# def sumnum(n):
#     res=0
#     for i in n:
#         res+=int(i)
#     return res
# n=1
# for i in range(100):
#     n_bin=bin(n)[2:]
#     if n_bin.count("1")%2==0:
#         n_bin="10"+n_bin[2:]+"0"
#     else:
#         n_bin="11"+n_bin[2:]+"1"
#     if int(n_bin ,2)<20:
#         print(n)
#     n+=1

# from turtle import *
# tracer(0)
# left(90)
# for i in range(8):
#     forward(40*29)
#     right(90)
#     forward(40*17)
#     right(90)
# penup
# forward(5*40)
# right(90)
# forward(1*40)
# left(90)
# pendown
# for i in range(8):
#     forward(40*64)
#     right(90)
#     forward(48*40)
#     right(90)
# penup
# for x in range(-10, 10):
#     for y in range(-10,10):
#         setpos(x*40,y*40)
#         dot(4, "red")

# z=product([0,1,2,3,4,5,6,7,8], repeat=6)
# c=0
# for i in z:
#     if (i[0]==2 or i[0]==4 or i[0]==6 or i[0]==8) and (i[-1]!=2 and i[-1]!=3) and i.count(1)>=2:
#         c+=1
# print(c)
#
# s="7"*108
# while "33333" in s or "777" in s:
#     if "33333" in s:
#         print(1)
#         s=s.replace("33333", "7",1)
#     else:
#         print(2)
#         s=s.replace("777","3",1)
# print(s)

# from ipaddress import *
# c=0
# raw_ip=IPv4Address("106.184.0.0")
# mask=IPv4Address("255.248.0.0")
# network=ip_network(f'{raw_ip}/{mask}', 0)
# for host in network.hosts():
#     if sum([bin(int(el))[2::].count("1") for el in str(host).split('.')])%2!=0:
#         c+=1
# print(c)

#17 маски
