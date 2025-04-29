# from itertools import *
#
# def f(w,x,y,z):
#     return (not(x<=y)) or (z<=w) or (not z)
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0],0,val[1],0),
#         (1,val[2],val[3],val[4]),
#         (0,1,val[5],val[6])
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(p)



# for n in range(1,10**10):
#     r=bin(n)[2:]
#     if r.count('1')%2==0:
#         r='10'+r[2:]+'0'
#     else:
#         r='11'+r[2:]+'1'
#     if int(r,2)>19:
#         print(n)
#         break

# from turtle import *
# tracer(0)
# setworldcoordinates(-60,-60,60,60)
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
#     for y in range(-60,60):
#         setpos(x,y)
#         dot(4,'red')
# exitonclick()

# from itertools import *
#
# def check(x):
#     if x[-1]=='0' and x[-2] in '1357':
#         return False
#     else:
#         for i in range(1,len(x)-1):
#             if (x[i-1] in '1357' or x[i+1] in '1357') and x[i]=='0':
#                 return False
#     return True
#
# res=0
# for n in product('012345678', repeat=5):
#     if n[0]!='0' and n.count('0')==1 and check(n):
#         print(n)
#         res+=1
# print(res)

# def uni(x):
#     kol,pov=0,0
#     for i in range(1, len(x)-1):
#         if x[i-1]==x[i]==x[i+1]:
#             kol+=1
#             pov=x[i]
#     if kol==1:
#         return pov
#     else:
#         return 0
#
# f=open('2604files/9.csv')
# res=0
#
# for s in f:
#     nums=[int(x) for x in s.split(';')]
#     nums.sort()
#     tmp=uni(nums)
#     if tmp!=0:
#         if 3*(tmp**2)>(sum(nums)-3*tmp):
#             print(nums)
#             res+=1
# print(res)

# s='1'*81
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s=s.replace('11111','88',1)
#     else:
#         s=s.replace('888','8',1)
# print(s)

# from ipaddress import *
# raw=IPv4Address('172.16.168.0')
# mask=IPv4Address('255.255.248.0')
# net= ip_network(f'{raw}/{mask}',0)
# # допроверь 172.16.168.0 и 172.16.175.255
# res=0
# for host in net.hosts():
#     print(host)
#     if sum([bin(int(x))[2:].count('1') for x in str(host).split('.')])%5!=0:
#         res +=1
# if sum([bin(int(x))[2:].count('1') for x in '172.16.168.0'.split('.')])%5!=0:
#     res +=1
# if sum([bin(int(x))[2:].count('1') for x in '172.16.175.255'.split('.')])%5!=0:
#     res +=1
# print(res)

# def changesys(x):
#     alph='0123456789ABCDEFGHIJKLMNO'
#     res=''
#     while x>0:
#         res=alph[x%25]+res
#         x=x//25
#     return res
#
# for i in range(1,2031):
#     num=(25**100)+(25**20)-i
#     t=changesys(num)
#     if t.count('0')==81:
#         print(i)
#         break

# from itertools import *
# def f(x):
#     p = 15 <= x <= 40
#     q = 21 <= x <= 63
#     a = a1 <= x <=a2
#     return p<=(((q) and (not a)) <= (not p))
#
# res=[]
# ox=[i/4 for i in range(15*4, 64*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         res.append(a2-a1)
# print(min(res))

# from sys import setrecursionlimit
#
# setrecursionlimit(999999999)
# def f(n):
#     if n<6:
#         return 1
#     elif n>=6:
#         return (n+5)*f(n-5)
# print((f(20240)+2*f(20235))/f(20230))

# f=open('2604files/17.txt')
# nums=[int(x) for x in f.readlines()]
# res,kr27=0,0
# for x in nums:
#     if abs(x)%27==0:
#         kr27+=1
# r1,r2=0,0
# for i in range(len(nums)-1):
#     if nums[i]+nums[i+1]<kr27:
#         r1+=1
#         r2=max(r2, abs(nums[i])+abs(nums[i+1]))
# print(r1,r2)

# def f(s,p):
#     if s<=19: return p%2==0
#     if p==0: return False
#     act=[f(s-2,p-1), f(s-5,p-1), f(s//3,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print('19', [s for s in range(20,100) if f(s,2)])
# print('20', [s for s in range(20,100) if f(s,3) and not f(s,1)])
# print('21', [s for s in range(20,100) if f(s,4) and not f(s,2)])

# def f(s,e):
#     if s==e: return True
#     if s<e: return False
#     return f(s-2,e)+f(s//2,e)
# print(f(38,16)*f(16,2))

import re
f=open('2604files/24.txt')
s=f.readline()
res=re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]))',s)
print(res)

# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
#
# def dell(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0 and prime(i):
#             res.append(i)
#             if i!=x//i and prime(x//i):
#                 res.append(x//i)
#     if len(res)>0:
#         return max(res)+min(res)
#     else:
#         return 0
#
# c=0
# for i in range(1_000_000+1, 10**100):
#     m=dell(i)
#     if m>1000 and m%10==5:
#         print(i,m)
#         c+=1
#     if c==5:
#         break

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def cent(cl):
    maxcl=0
    for i in cl:
        clie=0
        for j in cl:
            if dist(i[0],i[1], j[0],j[1])<=1:
                clie+=j[2]
        if clie>maxcl:
            maxcl=clie
            res=i
    return res

f=open('2604files/27A.txt')
a1,a2=[],[]
for s in f:
    s=s.split()
    s[0]=float(s[0].replace(',', '.'))
    s[1]=float(s[1].replace(',', '.'))
    s[2]=int(s[2])
    if s[1]>-2:
        a1.append(s)
    else:
        a2.append(s)
r1=cent(a1)
r2=cent(a2)
print((r1[0]+r2[0])/2*10_000)
print((r1[1]+r2[1])/2*10_000)

f=open('2604files/27B.txt')
a1,a2,a3=[],[],[]
for s in f:
    s=s.split()
    s[0]=float(s[0].replace(',', '.'))
    s[1]=float(s[1].replace(',', '.'))
    s[2]=int(s[2])
    if s[1]>4:
        a1.append(s)
    else:
        if s[0]>6:
            a2.append(s)
        else:
            a3.append(s)
r1=cent(a1)
r2=cent(a2)
r3=cent(a3)
print((r1[0]+r2[0]+r3[0])/3*10_000)
print((r1[1]+r2[1]+r3[1])/3*10_000)