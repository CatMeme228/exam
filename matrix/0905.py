# from itertools import *
#
# def f(w,x,y,z):
#     return (not(y<=(not(z<=w)))) and ((not z)<=((not w)==x))
#
# for val in product([0,1],repeat=5):
#     table=[
#         (1,val[0],1,1),
#         (val[1],val[2],0,0),
#         (val[3],0,0,val[4])
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('wxyz'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,1,1]:
#                 print(p)

# for n in range(1,10**10):
#     bin_n=bin(n)[2::]
#     r=''
#     for i in bin_n:
#         r+=i*2
#     if int(r,2)>32:
#         print(int(r,2))
#         break

# from turtle import *
# size=20
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
# right(90)
# for i in range(3):
#     right(45)
#     forward(10)
#     right(45)
# right(315)
# forward(10)
# for i in range(2):
#     right(90)
#     forward(10)
#
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(2,'red')
# done()

# def neib(x):
#     for i in range(len(x)-1):
#         if x[i]==x[i+1]=='С':
#             return False
#     return True
#
# from itertools import *
# res=0
# for i in product(sorted('СОЙКА'), repeat=5):
#     res+=1
#
#     if i.count('О')<=1 and neib(i):
#         print(i, res)

# for n in range(4,10**10):
#     s='3'+'5'*n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s=s.replace('25','5',1)
#         if '355' in s:
#             s=s.replace('355', '52',1)
#         if '555' in s:
#             s=s.replace('555','3',1)
#     if len(s)==s.count('5'):
#         print(n,s)
#         break

# from ipaddress import *
# r=0
# for ip in ip_network('192.168.134.64/255.255.255.192',0):
#     if sum([bin(int(x))[2::].count('1') for x in str(ip).split('.')])%5==0:
#         r+=1
# print(r)

# for x in range(0, 111):
#     n1 = x * (111 ** 3) + 3 * (111 ** 2) + 2 * (111 ** 1) + 1 * (111 ** 0)
#     n2 = 1 * (211 ** 3) + 7 * (211 ** 2) + x * (211 ** 1) + 4 * (211 ** 0)
#     if (n1+n2)%111==0:
#         print((n1+n2)/111)


# from itertools import *
# def f(x):
#     p = 24 <= x <= 77
#     q = 47 <= x <= 92
#     r = 82 <= x <= 116
#     a = a1 <= x <= a2
#     return (not((q)<=((p) or (r)))) <= ((not a) <= (not q))
#
# res=[]
# ox=[i/4 for i in range(24*4, 117*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         res.append(a2-a1)
# print(min(res))

# import sys
# sys.setrecursionlimit(9999999)
# def f(n):
#     if n==1 or n==2:
#         return n
#     a=[None]*(n+1)
#     a[0]=0
#     a[1]=1
#     a[2]=2
#     for i in range(3,n+1):
#         a[i]=i*(i-1)+a[i-1]-a[i-2]
#     return a[n]
#
# print(f(2024)+f(2020)-f(2019))

# f = open('0905files/17.txt')
# s = [int(x) for x in f]
# mpos = 0
# for x in s:
#     if x % 100 == 17:
#         mpos = max(mpos, x)
#
# r1, r2 = 0, 0
#
# for i in range(len(s) - 2):
#     f1 = (1000 <= s[i] <= 9999) + (1000 <= s[i + 1] <= 9999) + (1000 <= s[i + 2] <= 9999)
#     f2 = (s[i] % 5 == 0) + (s[i + 1] % 5 == 0) + (s[i + 2] % 5 == 0)
#     f3 = (s[i] + s[i + 1] + s[i + 2]) > mpos
#     if f1==2 and f2>0 and f3:
#         r1+=1
#         r2=max(r2, (s[i] + s[i + 1] + s[i + 2]))
# print(r1,r2)

# from math import ceil
# def f(s1,s2,p):
#     if (s1+s2)<=32: return p%2==0
#     if p==0: return False
#     act=[f(s1-1,s2,p-1), f(ceil(s1/2),s2,p-1), f(s1, s2-1,p-1), f(s1,ceil(s2/2),p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print([s for s in range(23,100) if f(10,s,2)])
# print([s for s in range(23,100) if f(10,s,3) and (not f(10,s,1))])
# print([s for s in range(23,100) if f(10,s,4) and (not f(10,s,2))])

# def f(s,e):
#     if s==e: return True
#     if e>s: return False
#     return f(s-1,e)+f(s//2,e)
# print(f(30,8)*f(8,1))

# f=open('0905files/24.txt')
# s=f.readline().strip()
# f.close()
# s=s.split('V')
# k=120
# tk=k
#
# for i in range(1,k):
#     tk+=len(s[i])
# mink=tk
#
# for i in range(2, len(s)-k+1):
#     tk=tk-len(s[i-1])+len(s[i+k-2])
#     mink=min(mink, tk)
# print(mink)

# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
#
# def dell(x):
#     res=[0]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             res.append(i)
#             if i!=x//i:
#                 res.append(x//i)
#     return max(res)
#
# br=0
# for i in range(550_000+1,10**100):
#     md=dell(i)
#     if not(prime(md)):
#         print(i, md)
#         br+=1
#     if br==6:
#         break

f=open('0905files/26.txt')
k=int(f.readline())
m=int(f.readline())
caves=[-1]*k
bags=[]
r1,r2=0,0
for s in f:
    s=s.split()
    tmp=[int(x) for x in s]
    bags.append(tmp)
bags.sort()
for x in bags:
    st=x[0]
    fin=x[1]
    for i in range(len(caves)):
        if st>caves[i]:
            caves[i]=fin
            r1+=1
            r2=i+1
            break
print(r1,r2)
# from math import dist
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p,p0) for p0 in cl])
#         if minr>s:
#             res=p
#             minr=s
#     return res
#
# f=open('0905files/27_A.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>1 and s[1]<3:
#         a1.append(s)
#     elif s[1]>3 and s[0]>-2:
#         a2.append(s)
# res1=cent(a1)
# res2=cent(a2)
# print((res1[0]+res2[0])/2*10_000)
# print((res1[1]+res2[1])/2*10_000)
#
# f=open('0905files/27_B.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[1]>2:
#         a1.append(s)
#     elif s[0]>2 and s[1]>-2:
#         a2.append(s)
#     elif -3<=s[0]<=0 and -3<=s[1]<=1:
#         a3.append(s)
# res1=cent(a1)
# res2=cent(a2)
# res3=cent(a3)
# print(res1,res2,res3)
# print((res1[0]+res2[0]+res3[0])/3*10_000)
# print((res1[1]+res2[1]+res3[1])/3*10_000)