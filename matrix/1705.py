# from itertools import *
#
# def f(w, x, y, z):
#     return ( (x == y) <= ((not z) or w) ) == (not( (w<=x) or (y<=z) ))
#
# for val in product([0,1], repeat=5):
#     table=[
#         (0,1,val[0],val[1]),
#         (val[2], val[3],1,0),
#         (0,val[4],0,0)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p, row))) for row in table]==[1,1,1]:
#                 print(p)

# def tr(x):
#     res=''
#     while x>0:
#         res = str(x%3)+res
#         x= x//3
#     return res
# res=10**10
# for n in range(1,1000):
#     r=tr(n)
#     if n%3==0:
#         r=r+r[-2:]
#     else:
#         r+=tr(n%3*5)
#     r=int(r,3)
#     if r>111:
#         res=min(r,res)
# print(res)

# from turtle import *
# tracer(0)
# size=20
# left(90)
# setworldcoordinates(-size,-size,size,size)
#
# for i in range(4):
#     for i in range(4):
#         forward(6)
#         right(90)
#     forward(10)
#     right(90)
#     forward(3)
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(4,'red')
# done()

# def ch(x):
#     if x[0]=='3' and x[1] in '13579':
#         return False
#     if x[-1]=='3' and x[-2] in '13579':
#         return False
#     for i in range(1, 4):
#         if x[i]=='3' and (x[i-1] in '13579' or x[i+1] in '13579'):
#             return False
#     return True
# r=0
# from itertools import *
# for a in product('012345678', repeat=5):
#     if a[0]!='0' and a.count('3')==2:
#         if ch(a):
#             print(a)
#             r+=1
# print(r)

# def st_check(n,st, table):
#     count=0
#     for i in range(16_000):
#         if table[i][st]==n:
#             count+=1
#         if count>150:
#             return True
#     return False
#
# f=open('1705files/09.csv')
# t=[]
# res=0
# for s in f:
#     s=s.split(',')
#     s=[int(x) for x in s]
#     t.append(s)
# for i in t:
#     c=0
#     if len(set(i))>=5:
#         for j in range(len(i)):
#             if i.count(i[j])==1:
#                 if st_check(i[j],j,t):
#
#                     c+=1
#         if c>=5:
#             res+=1
# print(res)

# res=0
# for n in range(4,10_000):
#     s='3'+'7'*n
#     while '37' in s or '577' in s or '777' in s:
#         if '37' in s:
#             s=s.replace('37','7',1)
#         if '577' in s:
#             s=s.replace('577', '73',1)
#         if '777' in s:
#             s=s.replace('777','5',1)
#     summ=sum([int(x) for x in s])
#     res=max(res,summ)
# print(res)

# res=10**10
# from ipaddress import *
# for m in range(13,33):
#     if ip_network(f'114.91.57.39/{m}',0)==ip_network(f'114.91.19.61/{m}',0):
#         tres=0
#         for ips in ip_network(f'114.91.57.39/{m}',0):
#             if sum([bin(int(x))[2::].count('1') for x in str(ips).split('.')])%2==0:
#               tres+=1
#         res=min(res,tres)
# print(res)

# a='0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
# a=sorted(a)
# for p in range(9,36):
#     for x in a[:p]:
#         for y in a[:p]:
#             for z in a[:p]:
#                 for w in a[:p]:
#                     n1=int(f'{z}{x}{y}{x}4',p)
#                     n2 = int(f'{x}{y}658', p)
#                     n3 = int(f'{w}{z}{x}73', p)
#                     if n1+n2==n3:
#                         print(int(f'{x}{y}{z}{w}',p))

# def f(x):
#     return (x&20777!=0) <= ((x&12332==0) <= (x&a!=0))
#
# for a in range(0,1000):
#     if all(f(x) for x in range(0,1000)):
#         print(a)
#         break

# from sys import setrecursionlimit
# setrecursionlimit(999999999)
# def f(n):
#     if n<5:
#         return n
#     else:
#         return 2*n*f(n-4)
# print((f(13766)-9*f(13762))/f(13758))

# f=open('1705files/17.txt')
# s=[int(x) for x in f]
# mpos=-1
# for i in s:
#     if i%1000==238:
#         mpos=max(mpos,i)
# r1,r2=0,0
# for i in range(len(s)-2):
#     f1= (10_000<=s[i]<=99_999)+(10_000<=s[i+1]<=99_999)+(10_000<=s[i+2]<=99_999)
#     f3= (s[i]%3==0)+(s[i+1]%3==0)+(s[i+2]%3==0)
#     f5 = (s[i] % 5 == 0) + (s[i + 1] % 5 == 0) + (s[i + 2] % 5 == 0)
#     if 1<=f1<3 and f3>f5 and (s[i]+s[i+1]+s[i+2])>mpos:
#         r1+=1
#         r2=max(r2, s[i]+s[i+1]+s[i+2])
# print(r1,r2)

# def f(s,p):
#     if s<10: return p%2==0
#     if p==0: return 0
#     act=[f(s-1,p-1)]
#     if s%2==0:
#         act.append(f(s/2,p-1))
#     if s%3==0:
#         act.append(f(s/3*2,p-1))
#     return any(act) if (p-1)%2==0 else all(act)
#
# print('19', [s for s in range(10,100) if f(s,2)])
# print('20', [s for s in range(10,100) if f(s,3) and (not(f(s,1)))])
# print('21', [s for s in range(10,100) if f(s,4) and (not(f(s,2)))])

# def f(s,e,pr,a):
#     if pr=='a':
#         a+=1
#     else: a=0
#     if a==2: return False
#     if s==e: return True
#     if s>=14 or s<-10: return False
#     return f(s-1,e,'a',a)+f(s+3,e,'',a)+f(s*2,e,'',a)
# print(f(3,12,'',0))

# import re
# res=0
# f=open('1705files/24.txt')
# s=f.readline().strip()
# a=re.findall(r'(?:[A]{1,})(?:0|[1-6][0-6]*)(?:[-*](?:0|[1-6][0-6]*))*',s)
# for i in a:
#     res=max(res, i.count('A'))
# print(res)

# from fnmatch import *
# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
#
# def dell(x):
#     res=0
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0 and prime(i):
#             if i!=(x//i) and prime(x//i):
#                 if prime(i+x//i):
#                     res=i+x//i
#     return res
#
# for i in range(1,10**7):
#     if fnmatch(str(i), '13?45*8'):
#         m=dell(i)
#         if m!=0:
#             print(i,m)

# from math import dist
#
# def anticent(cl):
#     maxr = 0
#     for p in cl:
#         s = sum([dist(p, p0) for p0 in cl])
#         if s > maxr:
#             maxr = s
#             res = p
#     return res
#
#
# f = open('1705files/27_7_2A.txt')
# a1, a2 = [], []
# for s in f:
#     s = s.replace(',', '.').split()
#     s = [float(x) for x in s]
#     if s[1] > 3:
#         a1.append(s)
#     else:
#         a2.append(s)
# f.close()
# r1 = anticent(a1)
# r2 = anticent(a2)
# print((r1[0] + r2[0]) / 2 * 10_000)
# print((r1[1] + r2[1]) / 2 * 10_000)
#
# f = open('1705files/27_7_2B.txt')
# a1, a2, a3 = [], [], []
# for s in f:
#     s = s.replace(',', '.').split()
#     s = [float(x) for x in s]
#     if s[1] > 7:
#         a1.append(s)
#     else:
#         if s[1] < 4:
#             a2.append(s)
#         else:
#             a3.append(s)
# f.close()
# r1 = anticent(a1)
# r2 = anticent(a2)
# r3 = anticent(a3)
# print((r1[0] + r2[0] + r3[0]) / 3 * 10_000)
# print((r1[1] + r2[1] + r3[1]) / 3 * 10_000)