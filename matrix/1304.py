from itertools import *
from sys import setrecursionlimit
from turtle import *
#
# def f(x,y,z,w):
#     return (not(x<=y)) or (z<=w) or (not z)
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0], 0,val[1],0),
#         (1,val[2],val[3],val[4]),
#         (0,1,val[5],val[6])
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**(dict(zip(p,row)))) for row in table]==[0,0,0]:
#                 print(p)

# for n in range(1,10**10):
#     r=bin(n)[2::]
#     if r.count('1')%2==0:
#         r='10'+r[2:]+'0'
#     else:
#         r='11'+r[2::]+'1'
#     if int(r,2)>19:
#         print(n)
#         break

# setworldcoordinates(-60,-60,60,50)
# tracer(0)
# left(90)
# for i in range(9):
#     forward(27)
#     right(90)
#     forward(30)
#     right(90)
# penup()
# forward(3)
# right(90)
# forward(6)
# left(90)
# pendown()
# for i in range(9):
#     forward(77)
#     right(90)
#     forward(66)
#     right(90)
# penup()
# for x in range(-60,60):
#     for y in range(-60,50):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# r=0
# for n in product('012345678',repeat=5):
#     if n[0]!='0' and n.count('0')==1:
#         if n[4]=='0' and (int(n[3]))%2==0:
#             r+=1
#         else:
#             for i in range(1,len(n)-1):
#                 if n[i]=='0':
#                     if int(n[i-1])%2==int(n[i+1])%2==0:
#                         r+=1
#                         break
# print(r)

# r=0
# f=open('1304files/09.csv')
# for s in f:
#     n=[int(x) for x in s.split(',')]
#     if len(set(n))==3 and max(n)<(sum(n)-max(n)):
#         r+=1
# print(r)

# s='1'+90*'0'
# while '1' in s:
#     if '10' in s:
#         s=s.replace('10','0001',1)
#     else:
#         s=s.replace('1','000',1)
# print(s.count('0'))

# from ipaddress import *
# r=0
# net=ip_network('172.16.80.0/255.255.248.0',0)
# for host in net.hosts():
#     if sum([bin(int(x))[2:].count('1') for x in str(host).split('.')])%2!=0:
#         r+=1
#
# if sum([bin(int(x))[2:].count('1') for x in '172.16.80.0'.split('.')]) % 2 != 0:
#     r += 1
# if sum([bin(int(x))[2:].count('1') for x in '172.16.87.255'.split('.')]) % 2 != 0:
#     r += 1
# print(r)

# def s3(x):
#     r=''
#     while x>0:
#         r=str(x%3)+r
#         x=x//3
#     return r
#
# m0,r=0,0
#
# for i in range(1,2031):
#     t= 3**100-i
#     t=s3(t)
#     if m0<=t.count('0'):
#         m0=t.count('0')
#         r=i
# print(r)

# def f(x):
#     p = 17<=x<=58
#     q = 29<=x<=80
#     a = a1<=x<=a2
#     return p<=((q and (not a))<=(not p))
# z=[]
# ox=[i/4 for i in range(17*4,(80+1)*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print(min(z))

# setrecursionlimit(999999999)
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return n*f(n-1)
# print((f(2024)/4+f(2023))/f(2022))

# f=open('1304files/17.txt')
# n=[int(x) for x in f.readlines()]
# mpos=min(n)
# r1,r2=0,0
# for i in range(len(n)-1):
#     if n[i]%16==mpos or n[i+1]%16==mpos:
#         r1+=1
#         r2=max(r2, n[i]+n[i+1])
# print(r1,r2)

# def f(s,e):
#     if s==e: return True
#     if e>s: return False
#     return f(s-1,e)+f(s//2,e)
# print(f(30,12)*f(12,1))

#AB 21 раз
# with open('1304files/24.txt') as f:
#     s=f.readline()
# s=s.replace('AB', 'A*B')
# s=s.split('*')
# maxk=0
# k=100
# tk=0
# for i in range(k+1):
#     tk+=len(s[i])
# maxk=tk
# for i in range(1, len(s)-k):
#     tk=tk-len(s[i-1])+len(s[i+k])
#     maxk=max(maxk, tk)
# print(maxk)

# def dell(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             res.append(i)
#             if x//i!=i:
#                 res.append(x//i)
#     if len(res)>0:
#         return min(res)+max(res)
#     else:
#         return 0
# c=0
# for i in range(700_000+1, 10**10):
#     m=dell(i)
#     if m%10==4:
#         print(i,m)
#         c+=1
#     if c==5:
#         break

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def cent(a):
    minr=10**10
    for i in range(len(a)):
        s=0
        for j in range(len(a)):
            s+=dist(a[i][0],a[i][1],a[j][0],a[j][1])
        if s<minr:
            res=a[i]
            minr=s
    return res

f=open('1304files/27_A.txt')
f.readline()
a1,a2=[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if s[1]>0:
        a1.append(s)
    else:
        a2.append(s)
r1=cent(a1)
r2=cent(a2)
print((r1[0]+r2[0])/2*10_000)
print((r1[1]+r2[1])/2*10_000)

f=open('1304files/27_B.txt')
f.readline()
a1,a2,a3=[],[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if s[1]>5:
        a1.append(s)
    else:
        if s[1]<-5:
            a2.append(s)
        else:
            a3.append(s)
r1=cent(a1)
r2=cent(a2)
r3=cent(a3)
print((r1[0]+r2[0]+r3[0])/3*10_000)
print((r1[1]+r2[1]+r3[1])/3*10_000)