# from itertools import *
#
# def f(w,x,y,z):
#     return (not(x<=y)) or (z<=w) or (not z)
#
# for val in product([0,1],repeat=7):
#     table=[
#         (val[0],0,val[1],0),
#         (1,val[2],val[3],val[4]),
#         (0,1,val[5],val[6])
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(p)

# for n in range(1,100):
#     r=bin(n)[2::]
#     if r.count('1')%2==0:
#         r='10'+r[2:]+'0'
#     else:
#         r='11'+r[2:]+'1'
#     r=int(r,2)
#     if r>19:
#         print(n)
#         break

# from turtle import *
# size=50
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
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
#
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# print((1_310_720*300)/(1024*768*12))

# from itertools import product
#
# r=0
# def check(x):
#     if x[-1]=='0' and x[-2] in '1357':
#         return False
#     for i in range(1, len(x)-1):
#         if x[i]=='0' and (x[i-1] in '1357' or x[i+1] in '1357'):
#             return False
#     return True
#
# for a in product('012345678', repeat=5):
#     if a[0]!='0':
#         if a.count('0')==1:
#             if check(a):
#                 print(a)
#                 r+=1
# print(r)

# s='1'*81
# while '11111' in s or '888' in s:
#     if '11111' in s:
#         s=s.replace('11111','88',1)
#     else:
#         s=s.replace('888','8',1)
# print(s)

# r=0
# from ipaddress import *
# for host in ip_network('172.16.168.0/255.255.248.0',0):
#     if sum([bin(int(x))[2:].count('1') for x in str(host).split('.')])%5!=0:
#         r+=1
# print(r)

# def to25(x):
#     alph='0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
#     alph=sorted(alph)
#     res=''
#     while x>0:
#         res=str(alph[x%25])+res
#         x=x//25
#     return res
#
# for i in range(1,2031):
#     n= 25**100+25**20-i
#     n=to25(n)
#     if n.count('0')==81:
#         print(i)
#         break

# from itertools import combinations
# def f(x):
#     p = 15 <= x <= 40
#     q = 21 <= x <= 63
#     a = a1 <= x <= a2
#     return (p)<=(((q) and (not a))<= (not p))
#
# ox=[i/4 for i in range(15*4,64*4)]
# res=[]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         res.append(a2-a1)
# print(min(res))

# from sys import setrecursionlimit
# setrecursionlimit(9999999)
#
# def f(n):
#     if n<6:
#         return 1
#     else:
#         return (n+5)*f(n-5)
# print((f(20240)+2*f(20235))/f(20230))

# f=open('17.txt')
# s=[int(x) for x in f]
# f.close()
#
# kr27=0
# for i in s:
#     if abs(i)%27==0:
#         kr27+=1
# r1,r2=0,0
# for i in range(len(s)-1):
#     if (s[i]+s[i+1])<kr27:
#         r1+=1
#         r2= max(r2, abs(s[i])+abs(s[i+1]))
# print(r1,r2)

# def f(s,p):
#     if s<=19: return p%2==0
#     if p==0: return False
#     act=[f(s-2,p-1), f(s-5,p-1), f(s//3, p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19:', [s for s in range(20,100) if f(s,2)])
# print('20:', [s for s in range(20,100) if f(s,3) and not f(s,1)])
# print('21:', [s for s in range(20,100) if f(s,4) and not f(s,2)])

# def f(s,e):
#     if s==e: return True
#     if s<e: return False
#     return f(s-2,e)+f(s//2,e)
# print(f(38,16)*f(16,2))

# f=open('24.txt')
# s=f.readline().strip()
# f.close()
# import re
# a=re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*',s)
# print(len(max(a, key = len)))

# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
#
# def dell(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             if prime(i):
#                 res.append(i)
#             if i!=x//i and prime(x//i):
#                 res.append(x//i)
#     if len(res)>0:
#         return max(res)+min(res)
#     else:
#         return 0
#
# br=0
# for i in range(1_000_000+1, 10**10):
#     if br==5:
#         break
#     m=dell(i)
#     if m>1000 and m%10==5:
#         print(i,m)
#         br+=1

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def cent(cl):
    maxclie=-1
    for p in cl:
        clie=sum([x[2] for x in cl if dist(p[0], p[1],x[0],x[1])<=1])
        if clie>maxclie:
            maxclie=clie
            res=p
    return res

f=open('27A.txt')
a1,a2=[],[]
for s in f:
    s=s.replace(',', '.')
    s=s.split()
    s[0] = float(s[0])
    s[1]= float(s[1])
    s[2]= int(s[2])
    if s[1]>-2:
        a1.append(s)
    else:
        a2.append(s)
r1=cent(a1)
r2=cent(a2)
print((r1[0]+r2[0])/2*10_000)
print((r1[1]+r2[1])/2*10_000)

f=open('27B.txt')
a1,a2,a3=[],[],[]
for s in f:
    s=s.replace(',', '.')
    s=s.split()
    s[0] = float(s[0])
    s[1]= float(s[1])
    s[2]= int(s[2])
    if s[1]>4:
        a1.append(s)
    else:
        if s[1]<0:
            a2.append(s)
        else:
            a3.append(s)
r1=cent(a1)
r2=cent(a2)
r3=cent(a3)
print((r1[0]+r2[0]+r3[0])/3*10_000)
print((r1[1]+r2[1]+r3[1])/3*10_000)
