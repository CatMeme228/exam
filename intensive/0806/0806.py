# from itertools import *
#
# def f(x,y,z,w):
#     return ((x<=y) or (z<=w)) and ((z==y)<=(w==x))
#
# for val in product([0,1], repeat=4):
#     table=[
#         (val[0],1,0,val[1]),
#         (0,1,0,1),
#         (val[2],1,0,val[3])
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(p)
import string


# def tr(num):
#     res=''
#     while num>0:
#         res=str(num%3)+res
#         num= num //3
#     return res
# rs=-1
# for  n in range(1,100000):
#     r=tr(n)
#     if n%3==0:
#         r= r+r[-2]+r[-1]
#     else:
#         r = r+ tr((n%3)*5)
#     r=int(r,3)
#     if r <=242:
#         rs=max(rs,r)
# print(rs)

# from turtle import *
# size=15
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
# for i in range(3):
#     forward(7)
#     right(90)
# forward(10)
# for i in range(3):
#     left(90)
#     forward(6)
#
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# from itertools import *
#
# k=0
# for i in product('01', repeat=11):
#     a=''.join(i)
#     if a[0]=='1' and a.count('1')==3 and '11' not in a:
#         k+=1
# s1= 4**11*k
#
# k=0
# for i in product('01', repeat=11):
#     a=''.join(i)
#     if a[0]=='0' and a.count('1')==3 and '11' not in a:
#         k+=1
# s0= 3*4**10*k
# print(s0+s1)

# res=-1
# for n in range(4,1000):
#     s='3'+'5'*n
#     while '333' in s or '555'in s:
#         if '555' in s:
#             s=s.replace('555', '3',1)
#         else:
#             s=s.replace('333','5',1)
#     tmp=sum([int(x) for x in s])
#     res=max(res,tmp)
# print(res)

# from ipaddress import *
# r=0
# for host in ip_network('192.168.32.48/255.255.255.240'):
#     if sum([bin(int(x))[2:].count('1') for x in str(host).split('.')])%2!=0:
#         r+=1
# print(r)

# alf='0123456789'+string.ascii_uppercase
# for p in range(10,37):
#     for x in alf[:p]:
#         for y in alf[:p]:
#             n1=int(f'32{x}8',p)
#             n2=int(f'{x}{x}{x}9',p)
#             n3=int(f'{y}{y}02',p)
#             if (n1+n2)==n3:
#                 print(int(f'{y}{y}{x}',p))

# def f(x):
#     return ((x&35!=0) or (x&22!=0))<=( (x&15==0) <= (x&a!=0))
#
# for a in range(0,1000):
#     if all(f(x) for x in range(0,1000000)):
#         print(a)
#         break

# from sys import setrecursionlimit
# setrecursionlimit(99999999)
# def f(n):
#     if n<=3:
#         return 1
#     else:
#         return (n+3)*f(n-2)
# print(f(2028)/f(2024))

# f=open('17.txt')
# s= [int(x) for x in f]
# mpos=10**10
# for i in s:
#     if abs(i)%10==3:
#         mpos=min(mpos,i)
# r1,r2=0,0
# for i in range(len(s)-1):
#     f1= abs(s[i])%10 == abs(s[i+1])%10
#     f2= (abs(s[i])%3==0) + (abs(s[i+1])%3==0)
#     f3= (s[i]**2+ s[i+1]**2)<= (mpos**2)
#     if f1 and f2==1 and f3:
#         r1+=1
#         r2=max(r2,s[i]**2+ s[i+1]**2)
#         print(s[i], s[i+1])
# print(r1,r2)

# def f(s1, s2, p):
#     if (s1 + s2) > 45: return p % 2 == 0
#     if p == 0: return False
#     act = []
#     if s1 > s2:
#         for i in range(1, s2 + 1):
#             act.append(f(s1, s2 + i, p - 1))
#     else:
#         for i in range(1, s1 + 1):
#             act.append(f(s1 + i, s2, p - 1))
#     return any(act) if (p - 1) % 2 == 0 else all(act)
#
#
# print('19', min([k1 + k2 for k1 in range(1, 46) for k2 in range(1, 46) if f(k1, k2, 1)]))
# print('20.1', min([s for s in range(1, 41) if f(5, s, 3) and not f(5, s, 1)]))
# print('20.2', max([s for s in range(1, 41) if f(5, s, 3) and not f(5, s, 1)]))
# print('21', min([s for s in range(1, 41) if f(5, s, 4) and not f(5, s, 2)]))


# def f(s,e, umn):
#     if s==e and umn==1: return True
#     if s>e: return False
#     return f(s+1,e,umn)+f(s+2,e,umn)+f(s*2,e,umn+1)+f(s*3,e,umn+1)
# print(f(1,11,0))

# f=open('24.txt')
# s=[x.strip() for x in f]
# chain=1
# st_let=1
# for i in s:
#     cur_chain=1
#     cur_let=1
#     for j in range(len(i)-1):
#         if i[j]==i[j+1]:
#             cur_chain+=1
#             cur_let=i.count(i[j])
#         else:
#             if cur_chain>chain:
#                 chain = cur_chain
#                 st_let = cur_let
#             elif cur_chain==chain:
#                 chain=cur_chain
#                 st_let=max(cur_let,st_let)
#             cur_chain = 1
#             cur_let = 1
# print(st_let)

# from fnmatch import *
# for i in range(4173,10**10, 4173):
#     if fnmatch(str(i), '1?7246*1'):
#         print(i)

# from math import dist
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p,p0) for p0 in cl])
#         if minr>s:
#             minr =s
#             res=p
#     return res
#
# f=open('27_7_A.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',','.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[1]>4:
#         a1.append(s)
#     elif s[0]>2:
#         a2.append(s)
# r1=cent(a1)
# r2=cent(a2)
# print(r1,r2)
# print((r1[0]+r2[0])/2*10_000)
# print((r1[1]+r2[1])/2*10_000)
#
# f=open('27_7_B.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',','.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if -2<s[0]<2 and s[1]>1:
#         a1.append(s)
#     elif s[0]>2 and s[1]>0:
#         a2.append(s)
#     elif -2<s[0]<2 and s[1]<-1:
#         a3.append(s)
# r1=cent(a1)
# r2=cent(a2)
# r3=cent(a3)
# print(r1,r2,r3)
# print((r1[0]+r2[0]+r3[0])/3*10_000)
# print((r1[1]+r2[1]+r3[1])/3*10_000)
