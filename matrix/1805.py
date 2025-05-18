# from itertools import *
# def f(x,y,z,w):
#     return (not(x or y)) and (not(w)) or (not(z or w)) and y
#
# for val in product([0,1], repeat=8):
#     table=[
#         (val[0],1,val[1],val[2]),
#         (val[3],val[4],1,val[5]),
#         (val[6], 1, val[7],1)
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p,row))) for row in table]==[1,1,1]:
#                 print(p)

# res=10**10
# for n in range(1,1000):
#     r=bin(n)[2:]
#     if n%3==0:
#         r+=r[-2:]
#     else:
#         r+=bin(n%3*3)[2:]
#     r=int(r,2)
#     if r>=195:
#         res=min(res,r)
# print(res)

# from turtle import *
# size=50
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
# for i in range(2):
#     forward(23)
#     left(90)
#     back(27)
#     left(90)
# penup()
# back(5)
# right(90)
# forward(11)
# left(90)
# pendown()
# for i in range(2):
#     forward(26)
#     right(90)
#     forward(32)
#     right(90)
#
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(4,'red')
# done()

# from itertools import *
# res=0
# for a in product('0123456',repeat=7):
#     if a[0]!='0':
#         if a.count('0')+a.count('2')+a.count('4')+a.count('6')==2:
#             res+=1
# print(res)

# res=-1
# for n in range(4,1000):
#     s='8'+'4'*n
#     while '11' in s or '444' in s or '8888' in s:
#         if '11' in s:
#             s=s.replace('11','4',1)
#         if '444' in s:
#             s=s.replace('444','88',1)
#         if '8888' in s:
#             s=s.replace('8888','1',1)
#     a=sum([int(x) for x in s])
#     res=max(res,a)
# print(res)

# res=0
# from ipaddress import *
# for host in ip_network('112.208.0.0/255.255.128.0'):
#     if sum([bin(int(x))[2:].count('1') for x in str(host).split('.')])%11==0:
#         res+=1
# print(res)


# def chsys(x):
#     res=''
#     alph='0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
#     alph=sorted(alph)
#     while x>0:
#         res=alph[x%25]+res
#         x=x//25
#     return res
#
# res=0
# n=4*3125**2019+3*625**2020-2*125**2021+25**2022-4*5**2023-2024
# n=chsys(n)
# for i in n:
#     if i not in '0123456789':
#         res+=1
#         print(i)
# print(res)

# def f(x):
#     return (not (x % a == 0)) <= ((x % 28 == 0) <= (not(x%49==0)))
#
# for a in range(1,1000):
#     if all(f(x) for x in range(1,10000)):
#         print(a)

# from sys import setrecursionlimit
# setrecursionlimit(9999999)
# def f(n):
#     if n<=3:
#         return 2025
#     else:
#         return 3*(n-1)*f(n-2)
#
# print(f(2027)/f(2023))

# f=open('1805files/17.txt')
# s=[int(x) for x in f]
# mpos=0
# for i in s:
#     tmp=abs(i)
#     if 10_000<=tmp<=99_999 and tmp%100==21:
#         mpos=max(mpos,i)
# r1,r2=0,0
# for i in range(len(s)-1):
#     n1=abs(s[i])
#     n2=abs(s[i+1])
#     f1= (10_000<=n1<=99_999)+ (n1%100==21)
#     f2 = (10_000 <= n2 <= 99_999) + (n2 % 100 == 21)
#     if ( (f1!=2 and f2==2) or (f1==2 and f2!=2)) and (s[i]**2+s[i+1]**2)>=mpos**2:
#         r1+=1
#         r2=max((s[i]+s[i+1]),r2)
#         print(s[i],s[i+1])
# print(r1,r2)

# def f(s,p):
#     if s>=435: return p%2==0
#     if p==0: return False
#     act=[f(s+5,p-1),f(s*3,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19:', [s for s in range(1,435) if f(s,2)])
# print('20:', [s for s in range(1,435) if f(s,3) and not(f(s,1))])
# print('21:', [s for s in range(1,435) if f(s,4) and not(f(s,2))])

# def f(s,e):
#     if s == 16: return False
#     if s==e: return True
#     if s>e: return False
#     return f(s+1,e)+f(s+2,e)+f(s*3,e)
# print(f(2,9)*f(9,18))

# f=open('1805files/24.txt')
# s=f.readline().strip()
# res=-1
# tmp=1
# for i in range(len(s)-1):
#     if (s[i]=='K' and s[i+1]=='L') or (s[i]=='L' and s[i+1]=='M') or (s[i]=='M' and s[i+1]=='N') or (s[i]=='N' and s[i+1]=='K'):
#         tmp+=1
#     else:
#         res=max(res,tmp)
#         tmp=1
# print(res)

# def dell(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             res.append(i)
#             if i!=(x//i):
#                 res.append(x//i)
#     if len(res)>0:
#         return min(res)+max(res)
#     else:
#         return 0
# c=0
# for i in range(700_001,10**100):
#     if c==5:
#         break
#     m=dell(i)
#     if m%10==4:
#         print(i,m)
#         c+=1

from math import dist

def cent(cl):
    minr=10**10
    for p in cl:
        s=sum([dist(p,p0) for p0 in cl])
        if minr>s:
            minr=s
            res=p
    return res

f=open('1805files/27_7_4A.txt')
a1,a2=[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if 2*s[0]-16<=s[1]<=2*s[0]:
        if s[1]>=(5/6)*s[0]-3:
            a1.append(s)
        else:
            a2.append(s)
f.close()
r1=cent(a1)
r2=cent(a2)
print((r1[0]+r2[0])/2*10_000)
print((r1[1]+r2[1])/2*10_000)

f=open('1805files/27_7_4B.txt')
a1,a2,a3,a4=[],[],[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if (s[0]>0 and -s[0]<=s[1]<=s[0]+8) or (s[0]<=0 and s[0]-4<=s[1]<=-s[0]+14):
        if s[0] > 3.8 and s[1] > 5.8:
            a1.append(s)
        elif s[1] < 4 * s[0] - 9.2:
            a2.append(s)
        elif s[1] < 0.2436 * s[0] + 4.9744:
            a3.append(s)
        else:
            a4.append(s)

f.close()
r1=cent(a1)
r2=cent(a2)
r3=cent(a3)
r4=cent(a4)
print((r1[0]+r2[0]+r3[0]+r4[0])/4*10_000)
print((r1[1]+r2[1]+r3[1]+r4[1])/4*10_000)
