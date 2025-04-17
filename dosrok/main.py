# from itertools import *
# def f(x,y,z,w):
#     return (x or (not y)) and not(y==z) and w
#
# for val in product([0,1],repeat=4):
#     table=[
#         (1, val[0],val[1],1),
#         (1,1,val[2],1),
#         (val[3], 1, 1, 1)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,row))) for row in table]==[1,1,1]:
#                 print(p)

# def f(x,y):
#     return (x>8) or (2*x<y) or (x*y<a)
#
# for a in range(1000):
#     if all(f(x,y) for x in range(10) for y in range(21)):
#         print(a)
#         break

# from ipaddress import *
# net=ip_network('218.194.82.148/255.255.255.192',0)
# for host in net.hosts():
#     print(host)

# def f(s,e):
#     if s==e: return True
#     if s>e: return False
#     if s==16: return False
#     return f(s+1,e)+f(s+2,e)+f(s*3,e)
#
# print(f(2,9)*f(9,18))

# def f(s,e):
#     if s>=61: return e%2==0
#     if e==0: return False
#     act=[f(s+1,e-1),f(s+4,e-1),f(s*3,e-1)]
#     return any(act) if (e-1)%2==0 else all(act)
#
# print('19:', [s for s in range(1,61) if f(s,2)])
# print('20:', [s for s in range(1,61) if f(s,3) and not f(s,1)])
# print('21:', [s for s in range(1,61) if f(s,4) and not f(s,2)])

# from math import dist
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p,p1) for p1 in cl])
#         if s<minr:
#             res=p
#             minr=s
#     return res
#
# f=open('txts/27_1_A.txt')
# a=[[float(x) for x in s.replace(',','.').split()] for s in f]
# vlecl=[]
# e=1
#
# while len(a)>0:
#     tcl=[a[-1]]
#     a.pop()
#     for p in tcl:
#         bliz_t=[t1 for t1 in a if dist(p,t1)<e]
#         for x in bliz_t:
#             tcl.append(x)
#             a.remove(x)
#     vlecl.append(tcl)
# print(len(vlecl), len(vlecl[0])+len(vlecl[1]))
# res1=cent(vlecl[0])
# res2=cent(vlecl[1])
# print((res1[0]+res2[0])/2*10_000)
# print((res1[1]+res2[1])/2*10_000)
#
#
# f=open('txts/27_1_B.txt')
# a=[[float(x) for x in s.replace(',','.').split()] for s in f]
# vlecl=[]
# e=1
#
# while len(a)>0:
#     tcl=[a[-1]]
#     a.pop()
#     for p in tcl:
#         bliz_t=[t1 for t1 in a if dist(p,t1)<e]
#         for x in bliz_t:
#             tcl.append(x)
#             a.remove(x)
#     vlecl.append(tcl)
# print(len(vlecl), len(vlecl[0])+len(vlecl[1])+len(vlecl[2]))
# res1=cent(vlecl[0])
# res2=cent(vlecl[1])
# res3=cent(vlecl[2])
# print((res1[0]+res2[0]+res3[0])/3*10_000)
# print((res1[1]+res2[1]+res3[1])/3*10_000)

# from sys import setrecursionlimit
# setrecursionlimit(9999999)
# def f(n):
#     if n>2025:
#         return 1
#     else:
#         return 2*n+f(n+2)
# print(f(23)-f(20))

# f=open('txts/17.txt')
# a=[int(x) for x in f.readlines()]
# mpos=max(a)**2
# r1,r2=0,0
# for i in range(len(a)-1):
#     flag=0
#     if 10_000<=abs(a[i])<=99_999 and abs(a[i])%100==21:
#         flag+=1
#     if 10_000<=abs(a[i+1])<=99_999 and abs(a[i+1])%100==21:
#         flag+=1
#     if flag==1 and a[i]**2+a[i+1]**2>=mpos:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1])
# print(r1,r2)

# for x in '0123456789ABCDEFGHIJK':
#     n1=f'943697{x}21'
#     n2=f'2{x}9253'
#     r= int(n1,21)-int(n2,21)
#     if r%20==0:
#         print(x, r//20)

# def ts(x):
#     res=''
#     while x>0:
#         res=str(x%3)+res
#         x=x//3
#     return res
#
#
# for n in range(1,10*10):
#     r=ts(n)
#     if (r.count('0')*0+r.count('1')*1+r.count('2')*2)%2==0:
#         r='10'+r[2:]+'0'
#     else:
#         r='2'+r+str(n%3)
#     if int(r,3)>259:
#         print(n)
#         break

# from turtle import*
# tracer(0)
# setworldcoordinates(-20,-20,20,20)
# left(90)
# right(90)
# for i in range(7):
#     forward(11)
#     right(45)
#     forward(8)
#     right(135)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         setpos(x,y)
#         dot(4,'red')
# done()

# r=0
# from itertools import *
# for a in product('МАСЛО',repeat=6):
#     if a.count('С')==1:
#         if a[0]!='А' and a[0]!='О':
#             if a[-1]=='А' or a[-1]=='О':
#                 print(a)
#                 r+=1
# print(r)

