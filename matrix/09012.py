from itertools import *
from sys import setrecursionlimit, set_int_max_str_digits
# from turtle import *
from ipaddress import *
from fnmatch import *

# def f (x,y,z,w):
#     return (x and (not y)) or (x==z) or w
#
# for i in product([0,1], repeat=4):
#     table=[
#         (1, i[0], 0,0),
#         (1,1,i[1],0),
#         (i[2],1,1,i[3])
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p, row))) for row in table]==[0,0,0]:
#                 print(p)

# for n in range(10**10):
#     r=bin(n)[2::]
#     if n%3==0:
#         r=r[-3:]+r
#     else:
#         r=bin(3*(n%3))[2::]+r
#     if int(r,2)>92:
#         print(n)
#         break

# tracer(0)
# setworldcoordinates(-35,-35,35,35)
# left(90)
# for i in range(3):
#     forward(33)
#     right(90)
#     forward(30)
#     right(90)
# penup()
# forward(9)
# right(90)
# forward(6)
# left(90)
# pendown()
# for i in range(2):
#     forward(40)
#     right(90)
#     forward(40)
#     right(90)
# penup()
# for x in range(-35,35):
#     for y in range(-35,35):
#         setpos(x,y)
#         dot(4, 'red')
# exitonclick()

# print((2*8000*34*(39*60+35)+(16*130*1024*8))/314572800)

# c=0
# fl=0
# for i in product("012345678", repeat=5):
#     if i[0]!="0":
#         if i.count('3')==2:
#             for j in range(1,(len(i)-1)):
#                 if i[0]=='3' and int(i[1])%2!=0:
#                     break
#                 if i[4]=='3' and int(i[3])%2!=0:
#                     break
#                 if  i[j]=='3' and (int(i[j-1])%2!=0 or int(i[j+1])%2!=0):
#                     break
#             else:
#                 print(i)
#                 c+=1
#             fl=0
# print(c)

# for n in range(3, 10_000):
#     a='4'+'8'*n
#     while '48' in a or '288' in a or '8888' in a:
#         if '48' in a:
#             a=a.replace('48', '8', 1)
#         if '288' in a:
#             a=a.replace('288', '84', 1)
#         if '8888' in a:
#             a=a.replace('8888', '2', 1)
#     res= [int(x) for x in a]
#     if sum(res)==64:
#         print(n)
#         break

# r=0
# raw=IPv4Address('142.178.32.160')
# mask=IPv4Address('255.255.255.240')
# net=ip_network(f'{raw}/{mask}',0)
# for host in net.hosts():
#     tmp=[int(x) for x in str(host).split('.')]
#     tmp_bin=bin(tmp[0])[2::]+bin(tmp[1])[2::]+bin(tmp[2])[2::]+bin(tmp[3])[2::]
#     if tmp_bin.count("1")%2==0:
#         r+=1
# s='142.178.32.255'
# tmp=[int(x) for x in s.split('.')]
# tmp_bin=bin(tmp[0])[2::]+bin(tmp[1])[2::]+bin(tmp[2])[2::]+bin(tmp[3])[2::]
# if tmp_bin.count("1")%2==0:
#     r+=1
#
# print(r)

# alph='0123456789abcdefghijklm'
# for x in alph:
#     z=int(f'7{x}38596', 23)+int(f'14{x}36', 23)+int(f'61{x}7', 23)
#     if z%22==0:
#         print(x, z/22)

# def f(x):
#     q= 32<=x<=84
#     p= 19<=x<=56
#     a= a1<=x<=a2
#     return ((not a) and q)<=p
# t=[]
# ox= [i/4 for i in range(19*4,85*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         t.append(a2-a1)
# print(min(t))

# setrecursionlimit(9999999)
# def f(n):
#     if n==1:
#         return 3
#     elif n>1:
#         return 2*n+5+f(n-1)
# print(f(3026)-f(3024))

# with open('text.txt') as f:
#     tmp=0
#     a=[int(x) for x in f.readlines()]
#     for i in a:
#         if len(str(i))==2:
#             tmp=max(tmp,i)
#     r1,r2=0,0
#     for i in range(len(a)-1):
#         if ((len(str(a[i]))==2 and len(str(a[i+1]))!=2) or (len(str(a[i]))!=2 and len(str(a[i+1]))==2))  and (a[i]+a[i+1])%tmp==0:
#             r1+=1
#             r2= max(r2, a[i]+a[i+1])
#     print(r1,r2)

# def f(s,p):
#     if s>=91: return p%2==0
#     if p==0: return False
#     act=[f(s+1, p-1), f(s+4,p-1), f(s*3, p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19', [s for s in range(1,91) if f(s, 2)])
# print('20', [s for s in range(1,91) if f(s, 3) and not f(s,1)])
# print('21', [s for s in range(1,91) if f(s, 4) and not f(s,2)])

# def f(s,d):
#     if s==d: return True
#     if s>d or s==15: return False
#     return f(s+2,d)+f(s+3,d)+f(s*2,d)
# print(f(3,9)*f(9,25))

# with open('text.txt') as f:
#     a=f.readline()
#     c=0
#     m=0
#     for i in range(1,len(a)):
#         if a[i]=='A' and (a[i-1]=='A' or a[i-1]=='B' or a[i-1]=='C'):
#             m=max(m,c)
#             c=1
#         elif a[i]=='B' and (a[i-1]=='A' or a[i-1]=='B' or a[i-1]=='C'):
#             m = max(m, c)
#             c = 1
#         elif a[i]=='C' and (a[i-1]=='A' or a[i-1]=='B' or a[i-1]=='C'):
#             m = max(m, c)
#             c = 1
#         else:
#             c+=1
#     print(m)

# for i in range(1921, 10**8, 1921):
#     if fnmatch(str(i), '2*1?5?1'):
#         print(i, i//1921)

# def f(u,w,x,y,z):
#     return ((x<=y) and (z==(not w)))<=(u==(x or z))
#
# for i in product([0,1], repeat=8):
#     table=[
#         (0, i[0], 0,0,0),
#         (0,i[1], i[2],0,0),
#         (i[3],0,0,0,i[4]),
#         (i[5],0,i[6],i[7],0)
#     ]
#     if len(table)==len(set(table)):
#         for j in permutations("uwxyz"):
#             if [f(**(dict(zip(j,row)))) for row in table]==[0,0,0,0]:
#                 print(j)


# a=[]
# b=0
# for n in range(10**5):
#     r=bin(n)[2:]
#     r=r+bin(n%4)[2:]
#     a.append(int(r,2))
# a.sort()
# for i in range(0,400):
#     c = 0
#     for j in a:
#         if 1+i<=j<=49+i:
#             c+=1
#     b=max(b,c)
# print(b)

# tracer(10)
# setworldcoordinates(-10,-10,15,15)
# left(90)
# for i in range(4):
#     forward(14)
#     right(90)
# for i in range(5):
#     forward(5)
#     right(45)
# penup()
# for x in range(-10,15):
#     for y in range(-10,15):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# print((1024*768*12*0.8)/(200*1024*8))


# for x in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@$%':
#     for y in '0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@$%':
#         z=f'57{x}692{y}19'
#         if int(change_sys(z, 40))%39==0:
#             x1=int(change_sys(x,40))
#             y1=int(change_sys(y,40))
#             if (x1*y1)**0.5==int(x1*y1)**0.5:
#                 print(x1*y1)

# def f(x):
#     return ((x&57>0) or (x&99>0))<=(x&a>0)
# for a in range(10000):
#     if all(f(x) for x in range(10000)):
#         print(a)

# setrecursionlimit(9999999)
# set_int_max_str_digits(9999999)
# def f(n):
#     if n<5:
#         return n
#     else:
#         return 2*n*f(n-4)
# print((f(13766)-9*f(13762))/f(13758))

# with open('text.txt') as f:
#     a=[int(x) for x in f.readlines()]
#
# mp=66123
# r1,r2=0,0
# for i in range(len(a)-2):
#     t1= (9999<a[i]<100_000 and 9999<a[i+1]<100_000) or  (9999<a[i]<100_000 and 9999<a[i+2]<100_000) or  (9999<a[i+2]<100_000 and 9999<a[i+1]<100_000)
#     t2= (a[i]%3== 0 and a[i+1]%3!=0 and a[i+2]%3!=0) or (a[i+1]%3== 0 and a[i]%3!=0 and a[i+2]%3!=0) or (a[i+2]%3== 0 and a[i+1]%3!=0 and a[i]%3!=0)
#     t3= a[i]+a[i+1]+a[i+2]>mp
#     if t1 and t2 and t3:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# def f (s,p):
#     if s>=96: return p%2==0
#     if p==0: return False
#     if s%2==0:
#         act=[f(s+1,p-1), f(s*1.5,p-1)]
#     if s%3==0:
#         act=[f(s+1,p-1), f((s/3)*4,p-1)]
#     if s%2!=0 and s%3!=0:
#         act=[f(s+1,p-1), f(s*2,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print([s for s in range(1,96) if f(s,2)])
# print([s for s in range(1,96) if f(s,3) and not f(s,1)])
# print([s for s in range(1,96) if f(s,4) and not f(s,2)])

# def f(s,d, fl):
#     if s==d: return True
#     if s>d: return False
#     if fl <2:
#         return f(s-1,d,fl+1)+f(s*2,d, fl)+f(s*3,d, fl)
#     else:
#         return  f(s * 2, d, fl) + f(s * 3, d, fl)
# print(f(3,20,0))

# for i in range(3147, 10**10, 3147):
#     if fnmatch(str(i), '1*4302?1'):
#         print(i)

with open('text.txt') as f:
    a=f.readline()
i=0
ap,bp=0,0
ac=0
bc=0
c,r=0,0
while i!=len(a):
    if a[i]=='a':
        ac+=1
        if ac==0:
            ap=i
    if a[i]=='b':
        bc+=1
        if bc==0:
            bp=i
    
    i+=1