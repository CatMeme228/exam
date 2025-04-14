from itertools import *

# def f(x,y,z,w):
#     return y and (x or z) or (not(y or z)) or w
#
# for val in product([0,1], repeat=4):
#     table=[
#         (1, val[0], 0,1),
#         (val[1], 1,0,val[2]),
#         (0,0,val[3],1)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**(dict(zip(p,row)))) for row in table]==[0,0,0]:
#                 print(p)

# for n in range(2,10**9):
#     r= bin(n)[2:]
#     if n%2==0:
#         r=r+r[-2]+r[-1]
#     else:
#         r='1'+r+'0'
#
#     if int(r, 2)==202:
#         print(n)

# from turtle import *
# tracer(10)
# setworldcoordinates(-25,-25,25,25)
# left(90)
# for i in range(2):
#     forward(5)
#     left(90)
#     back(13)
#     left(90)
# penup()
# back(10)
# right(90)
# forward(9)
# left(90)
# pendown()
# for i in range(2):
#     forward(11)
#     right(90)
#     forward(7)
#     right(90)
# penup()
# for x in range(-25,25):
#     for y in range(-25,25):
#         setpos(x,y)
#         dot(4, 'red')
# exitonclick()

# c=0
# for i in product('0123456',repeat=6):
#     if i[0]!='0':
#         if i.count('3')==1:
#             if not(int(i[0])%2==int(i[1])%2==1 or int(i[1])%2==int(i[2])%2==1 or int(i[2])%2==int(i[3])%2==1 or int(i[3])%2==int(i[4])%2==1 or int(i[4])%2==int(i[5])%2==1):
#                 c=c+1
# print(c)


# r=0
# for n in range(4,1_000):
#     s='7'+'1'*n
#     while '1111' in s or '7777' in s:
#         if '1111' in s:
#             s=s.replace('1111','77',1)
#         else:
#             s=s.replace('7777','1',1)
#     z=7*s.count('7')+1*s.count('1')
#     r=max(r, z)
# print(r)

# c=0
# from ipaddress import *
# rawip=IPv4Address('192.168.32.96')
# mask=IPv4Address('255.255.255.224')
# net=ip_network(f'{rawip}/{mask}',0)
# for host in net.hosts():
#     if sum([bin(int(el))[2:].count('1') for el in str(host).split('.')])%2==0:
#         c+=1
# host='192.168.32.96'
#
# if sum([bin(int(el))[2:].count('1') for el in str(host).split('.')])%2==0:
#     c+=1
# print(c)

# def ch_sys(x):
#     res=''
#     while x>0:
#         res=str(x%9)+res
#         x=x//9
#     return res
#
# z=2*729**2019+2*243**2020-81**2021+2*27**2022-2*9*2023-2024
# a=ch_sys(z)
# print(len(a)-a.count('0'), a)

# def f(x):
#     q= 47<=x<=115
#     p= 24<=x<=90
#     a = a1<=x<=a2
#     return q<=((p and (not a))<=(not q))
# z=[]
# ox=[i/4 for i in range(24*4,116*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print(min(z))
#
# from sys import setrecursionlimit
# setrecursionlimit(9999999)
# def f(n):
#     if n>=2031:
#         return 1
#     else:
#         return n+31+f(n+31)
# print(f(31)-f(23))

# f=open('2803files/17.txt')
# a=[int(x) for x in f.readlines()]
# mpos=0
# r1,r2=0,0
# for i in a:
#     if 100<=i<=999 and i%10==5:
#         mpos=max(i, mpos)
#
# for i in range(len(a)-2):
#     c1,c2,c3=0,0,0
#     if a[i]%10==5:
#         c1=1
#     if a[i+1]%10==5:
#         c2=1
#     if a[i+2]%10==5:
#         c3=1
#     if c1+c2+c3==1 and a[i]+a[i+1]+a[i+2]<=mpos:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# def f(s,p):
#     if s>=135: return p%2==0
#     if p==0: return False
#     act= [f(s+5,p-1), f(s*3, p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print([s for s in range(1,135) if f(s,2)])
# print([s for s in range(1,135) if f(s,3) and not(f(s,1))])
# print([s for s in range(1,135) if f(s,4) and not(f(s,2))])

# def f(s,e):
#     if s==e:
#         return True
#     if s>e:
#         return False
#     if s==21:
#         return False
#     return f(s+1,e)+f(s*2,e)+f(s*3,e)
# print(f(2,9)* f(9,37))

# f=open('2803files/24.txt')
# a=f.readline()
# r=1
# z=0
# for i in range(len(a)-1):
#     if a[i]=='F' and a[i+1]=='S':
#         r+=1
#     elif a[i]=='S' and a[i+1]=='W':
#         r+=1
#     elif a[i]=='W' and a[i+1]=='Y':
#         r+=1
#     elif a[i]=='Y' and a[i+1]=='F':
#         r+=1
#     else:
#         z=max(r,z)
#         r=1
# print(z)

# from fnmatch import *
# for i in range(98591,10**11, 98591):
#     if fnmatch(str(i), '123*45??1?'):
#         print(i, i//98591)


def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def cent(a):
    minr=10**10
    for i in range(len(a)):
        s = 0
        for j in range(len(a)):
            s+=dist(a[i][0], a[i][1], a[j][0], a[j][1])
        if minr>s:
            r=a[i]
            minr=s
    return r

# f=open('2803files/27A.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>0:
#         a1.append(s)
#     else:
#         a2.append(s)
# r1=cent(a1)
# r2=cent(a2)
# print((r1[0]+r2[0])/2*10_000)
# print((r1[1]+r2[1])/2*10_000)
#
# f=open('2803files/27B.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]<0:
#         a1.append(s)
#     else:
#         if s[1]>4:
#             a2.append(s)
#         else:
#             a3.append(s)
# r1=cent(a1)
# r2=cent(a2)
# r3=cent(a3)
# print((r1[0]+r2[0]+r3[0])/3*10_000)
# print((r1[1]+r2[1]+r3[1])/3*10_000)