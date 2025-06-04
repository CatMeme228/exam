# from itertools import *
#
# def f(x,y,z,w):
#     return ((w<=x)<=y) or (not(z))
#
# for val in product([0,1], repeat=7):
#     table=[
#         (val[0],0,val[1],val[2]),
#         (val[3],1,0,val[4]),
#         (val[5],val[6],1,0)
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(*p, sep='')

res=10**10
for n in range(1,1000):
    r=bin(n)[2:]
    if r[:2] == '00':
        r = '11' + r[2:]
    elif r[:2] == '01':
        r = '10' + r[2:]
    elif r[:2] == '10':
        r = '01' + r[2:]
    elif r[:2] == '11':
        r = '00' + r[2:]

    if r.count('1')%2==0:
        r=r+'10'
    else:
        r=r+'11'
    r=int(r,2)
    if r>43:
        res=min(r,res)
print(res)

# from turtle import *
# size=20
# setworldcoordinates(-size,-size,size,size)
# tracer(0)
# left(90)
#
# for i in range(2):
#     forward(8)
#     right(90)
#     forward(18)
#     right(90)
# penup()
# forward(4)
# right(90)
# forward(10)
# left(90)
# pendown()
# for i in range(2):
#     forward(17)
#     right(90)
#     forward(7)
#     right(90)
#
# penup()
# for x in range(-size,size):
#     for y in range(-size,size):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# r=0
# from itertools import *
# for a in product('012345678', repeat=5):
#     if a[0]!='0':
#         if a[0]!='1' and a[0]!='3' and a[0]!='5' and a[0]!='7':
#             if a[-1]!='1' and a[-1]!='2':
#                 if a.count('8')>=2:
#                     print(a)
#                     r+=1
# print(r)

# s='1'*70
# while '1111' in s or '2222' in s:
#     if '1111' in s:
#         s=s.replace('1111','22',1)
#     else:
#         s=s.replace('2222','11',1)
# print(s)

# from ipaddress import *
# r=0
# for ip in ip_network('192.168.32.48/255.255.255.240'):
#     if sum([bin(int(x))[2:].count('1') for x in str(ip).split('.')])%2!=0:
#         r+=1
# print(r)

# def tr(x):
#     res=''
#     while x>0:
#         res= str(x%3)+res
#         x=x//3
#     return res
#
# for i in range(1,2031):
#     num=3**100-i
#     num=tr(num)
#     if num.count('0')==5:
#         print(i)
#         break

# from itertools import combinations
# def f(x):
#     b = 24<=x<=90
#     c = 47<=x<=115
#     a= a1<=x<=a2
#     return c<=(( (not a) and b)<=(not c))
#
# r=[]
# ox =[i/4 for i in range(24*4, (115+1)*4)]
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         r.append(a2-a1)
# print(min(r))

# from sys import setrecursionlimit
# setrecursionlimit(99999999)
# def f(n):
#     if n>=2025:
#         return n
#     else:
#         return n+3+f(n+3)
# print(f(2018)-f(2022))

# f=open('17.txt')
# s=[int(x) for x in f]
# f.close()
# mpos=min(s)
# r1,r2=0,0
# for i in range(len(s)-1):
#     if s[i]%22==mpos or s[i+1]%22==mpos:
#         r1+=1
#         r2=max(r2, s[i]+s[i+1])
# print(r1,r2)

# def f(s1,s2,p):
#     if (s1+s2)>=77: return p%2==0
#     if p==0: return False
#     act=[f(s1+1,s2,p-1),f(s1*2,s2,p-1),f(s1,s2+1,p-1),f(s1,s2*2,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print('19', [s for s in range(1,69) if f(8,s,2)])
# print('20', [s for s in range(1,69) if f(8,s,3) and not f(8,s,1)])
# print('21.1', [s for s in range(1,69) if f(8,s,2)])
# print('21.2', [s for s in range(1,69) if f(8,s,4) and not f(8,s,2)])

# def f(s,e):
#     if s==e: return True
#     if s<e: return False
#     return f(s-1,e)+f(s//2,e)
# print(f(32,11)*f(11,1))

# f=open('24.txt')
# s=f.readline()
# f.close()
#
# s=s.replace('DE',' ')
# s=s.split()
# k=240
# mk=0
# for i in range(len(s)-k):
#     tk = k * 2
#     for j in range(i, i+k+1):
#         tk+=len(s[j])
#     mk=max(mk,tk)
# print(mk)

# def f(x):
#     res=[0]
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             res.append(i)
#             if i!=x//i:
#                 res.append(x//i)
#     return sum(res)
#
# c=0
# for i in range(600_000+1,10**10):
#     r=f(i)
#     if r%10==6:
#         print(i,r)
#         c+=1
#         if c==5:
#             break

# f=open('26test.txt')
# n=int(f.readline())
# staff=[]
# for s in f:
#     s=s.split()
#     s=[int(x) for x in s]
#     staff.append(s)
# print(n)


# from math import dist
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p,p0) for p0 in cl])
#         if minr>s:
#             minr=s
#             res=p
#     return res
#
# f=open('27a.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',','.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>4:
#         a1.append(s)
#     else:
#         a2.append(s)
# r1=cent(a1)
# r2=cent(a2)
# print((r1[0]+r2[0])/2*10_000)
# print((r1[1]+r2[1])/2*10_000)
#
# f=open('27b.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',','.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[1]>6:
#         a1.append(s)
#     else:
#         if s[1]<2:
#             a2.append(s)
#         else:
#             a3.append(s)
# r1=cent(a1)
# r2=cent(a2)
# r3=cent(a3)
# print(r1,r2,r3)
# print((r1[0]+r2[0]+r3[0])/3*10_000)
# print((r1[1]+r2[1]+r3[1])/3*10_000)
