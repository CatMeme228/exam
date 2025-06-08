# from itertools import *
# def f(x,y,z,w):
#     return (not(z<=w)) or (z or x) and y or (not(x))
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0],0,0,val[1]),
#         (1,val[2],val[3],val[4]),
#         (0,1,val[5],val[6])
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(p)

# def tr(x):
#     res=''
#     while x>0:
#         res = str(x%3)+res
#         x=x//3
#     return res
# result=10**10
# for n in range(1,10000):
#     r=tr(n)
#     if n%3==0:
#         r=r+r[-2]+r[-1]
#     else:
#         r=r+tr(sum([int(i) for i in r]))
#     r=int(r,3)
#     if r>220 and r%2==0:
#         result=min(r, result)
# print(result)

# from turtle import *
# size=50
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
# for i in range(4):
#     forward(16)
#     right(90)
#     forward(22)
#     right(90)
# penup()
# forward(5)
# right(90)
# forward(5)
# left(90)
# pendown()
# for i in range(4):
#     forward(57)
#     right(90)
#     forward(75)
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
# c=0
# for a in product(sorted('ПАМЯТЬ'),repeat=5):
#     c+=1
#     if c%2==0:
#         if 'Ь' not in a and a.count('Я')==2:
#             res=c
#             print(a)
# print(res)

# for n in range(4,10_000):
#     s='1'+'2'*n
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s:
#             s=s.replace('12','2',1)
#         if '322' in s:
#             s=s.replace('322','21',1)
#         if '222' in s:
#             s=s.replace('222','3',1)
#     tmp=sum([int(x) for x in s])
#     if tmp==15:
#         print(n)
#         break

# from ipaddress import *
# for host in ip_network('142.29.122.138/255.255.192.0',0).hosts():
#     print(host)

# def to5(x):
#     res=''
#     while x>0:
#         res = str(x%5)+res
#         x=x//5
#     return res
#
# rs=0
# zeros=0
# for i in range(1,2501):
#     n=5**100-i
#     n=to5(n)
#     tmp=n.count('0')
#     if tmp>zeros:
#         rs=i
#         zeros=tmp
# print(rs)

# from itertools import *
# def f(x):
#     p = 16<=x<=53
#     q = 38 <=x<=75
#     a=a1<=x<=a2
#     return (p) <= (( (q) and (not a)) <=(not p))
# r=[]
# ox=[i/4 for i in range(16*4,76*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         r.append(a2-a1)
# print(min(r))

# from sys import setrecursionlimit
# setrecursionlimit(9999999)
# def f(n):
#     if n<10:
#         return n*n
#     else:
#         return (n-1)*f(n-2)
# print((f(34652)-250*f(34650))/f(34648))

f = open('17.txt')
s = [int(x) for x in f]
f.close()
mpos = -999999999
for i in s:
    tmp = abs(i)
    if 10_000 <= tmp <= 99_999 and tmp % 100 == 43:
        mpos = max(tmp, mpos)

r1, r2 = 0, 10**10
for i in range(len(s) - 2):
    f1 = 10_000 <= abs(s[i - 1]) <= 99_999 and abs(s[i - 1]) % 100 == 43
    f2 = 10_000 <= abs(s[i]) <= 99_999 and abs(s[i]) % 100 == 43
    f3 = 10_000 <= abs(s[i + 1]) <= 99_999 and abs(s[i + 1]) % 100 == 43
    if (f1 or f2 or f3) and (s[i - 1] ** 2 + s[i] ** 2 + s[i + 1] ** 2) <= mpos ** 2:
        r1 += 1
        r2 = min(r2, s[i - 1] ** 2 + s[i] ** 2 + s[i + 1] ** 2)
        print(s[i-1], s[i],s[i+1])
print(r1,r2)

# def f(s,p):
#     if s>=97: return p%2==0
#     if p==0: return False
#     act=[f(s+3,p-1),f(s+5,p-1),f(s*3,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19', [s for s in range(1,97) if f(s,2)])
# print('20', [s for s in range(1,97) if f(s,3) and not f(s,1)])
# print('20', [s for s in range(1,97) if f(s,4) and not f(s,2)])

# def f(s,e):
#     if s==e: return True
#     if s<e: return False
#     if s==24: return False
#     return f(s-1,e)+f(s-6,e)+f(s//2,e)
# print(f(34,20)*f(20,19)*f(19,6))

# f=open('24.txt')
# s=f.readline()
# m=0
# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         t=s[l:r+1]
#         if t.count('FSRQ')==80:
#             m=max(m,len(t))
#         elif  t.count('FSRQ')>80:
#             break
# print(m)

# from fnmatch import *
# for i in range(18579,10**10,18579):
#     if fnmatch(str(i), '54?1?3*7'):
#         print(i, i/18579)


# from math import dist
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s= sum([dist(p,p0) for p0 in cl])
#         if minr>s:
#             minr=s
#             res=p
#     return res
#
# f=open('27a.txt')
# f.readline()
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',','.').split()
#     s=[float(x) for x in s]
#     if s[1]>6:
#         a1.append(s)
#     else:
#         a2.append(s)
# r1=cent(a1)
# r2=cent(a2)
# print(r1,r2)
# print((r1[0]+r2[0])/2*10_000)
# print((r1[1]+r2[1])/2*10_000)
#
#
# f=open('27b.txt')
# f.readline()
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',','.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]<0:
#         a1.append(s)
#     else:
#         if s[1]>8:
#             a2.append(s)
#         else:
#             a3.append(s)
# r1=cent(a1)
# r2=cent(a2)
# r3=cent(a3)
# print(r1,r2,r3)
# print((r1[0]+r2[0]+r3[0])/3*10_000)
# print((r1[1]+r2[1]+r3[1])/3*10_000)
