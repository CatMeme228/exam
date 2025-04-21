from itertools import *
from turtle import *

# def f1(w,x,y,z):
#     return (x==y) and (w<=z)
#
# def f2(w,x,y,z):
#     return (x<=y)<=(w==z)
#
# for val in product([0,1], repeat=4):
#     table=[
#         (1,val[0],1,1),
#         (0,1,0,val[1]),
#         (val[2],0,0,val[3])
#     ]
#     if len(set(table))==len(table):
#         for p in permutations('wxyz'):
#             if [f1(**dict(zip(p,row))) for row in table]==[1,1,0] and ([f2(**dict(zip(p,row))) for row in table]==[0,1,0] or [f2(**dict(zip(p,row))) for row in table]==[0,0,0]):
#                 print(p)

# def tr(x):
#     res=''
#     while x>0:
#         res=str(x%3)+res
#         x=x//3
#     return res
#
# for n in range(100,0,-1):
#     r=tr(n)
#     if n%3==0:
#         r='1'+r+'02'
#     else:
#         r=r+tr((n%3)*4)
#     if int(r,3)<199:
#         print(n)
#         break

# setworldcoordinates(-20,-20,20,20)
# tracer(0)
# left(90)
# for i in range(8):
#     right(45)
#     forward(8)
# penup()
# for x in range(-20,21):
#     for y in range(-20,20):
#         setpos(x,y)
#         dot(4, 'red')
# done()

# c=0
# for a in product('АВЕСТ', repeat=5):
#     c+=1
#     if a[0]=='С' and a[1]=='В' and a[2]=='Е' and a[3]=='Т' and a[4]=='А':
#         print(c)
#         break
# print(int('31240',5)+1)

f=open('2004files/09.csv')
c=0
for s in f:
    n=[int(x) for x in s.split(',')]
    n.sort()
    if 6==len(set(n)):
        if (n[0]+n[5])/2>(n[1]+n[2]+n[3]+n[4])/4:
            c+=1
            print(n)
print(c)

# print((5*1024*1024/32768)-((5*5+90*11)/8))

# for n in range(4,10**10):
#     s='3'+'5'*n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s=s.replace('25','5',1)
#         if '355' in s:
#             s=s.replace('355','52',1)
#         if '555' in s:
#             s=s.replace('555','3',1)
#     if len(s)==s.count('5'):
#         print(n,s)
#         break


# def f37(x,al):
#     tmp=x[::-1]
#     res=0
#     for x in range(len(tmp)):
#         res+=37**x*al.index(tmp[x])
#     return res
#
# alph='0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
# alph=sorted(alph)
# alph.append('$')
# r=0
# for x in alph:
#     for y in alph:
#         n=f'12{x}643{y}7'
#         if f37(n,alph)%36==0:
#             r=max(r, f37(x,alph)*f37(y,alph))
# print(r)

# def f(x,y):
#     return ((x+2*y)>48) or (y>x) or ((x+3*y)<a)
# for a in range(1000):
#     if all(f(x,y) for x in range(100) for y in range(100))!=True:
#         print(a)

# def f(n):
#     if n>=1000:
#         return 1000
#     elif n<1000 and n%2!=0:
#         return n*f(n+1)
#     elif n<1000 and n%2==0:
#         return n*f(n+1)/2
# print(f(998)/f(1001))

# f=open('2004files/17.txt')
# a=[int(x) for x in f.readlines()]
# mpos=0
# for x in a:
#     if x%100==19:
#         mpos=max(mpos,x)
# r1,r2=0,0
# for i in range(len(a)-2):
#     f1 = (len(str(a[i]))==4) + (len(str(a[i+1]))==4) + (len(str(a[i+2]))==4)
#     f2 = (a[i]%3==0) + (a[i+1]%3==0) + (a[i+2]%3==0)
#     if f1==2 and f2>=1 and (a[i]+a[i+1]+a[i+2])>mpos:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# def f(s,p):
#     if s>=108: return p%2==0
#     if p==0: return False
#     if s%2!=0:
#         act=[f(s+1,p-1),f(s*2,p-1)]
#     elif s%2==0:
#         act=[f(s+1,p-1),f(s*1.5,p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
#
# print('19', [s for s in range(1,108) if f(s,2)])
# print('20', [s for s in range(1,108) if f(s,3) and not f(s,1)])
# print('21', [s for s in range(1,108) if f(s,4) and not f(s,2)])

# def f(s,e):
#     if s==e: return True
#     if s>e: return False
#     if s==12: return False
#     return f(s+1,e)+f(s*2,e)+f(s**2,e)
# print(f(3,25))

# f=open('2004files/24.txt')
# a=f.readline()
# b=a
# a=a.split('A')
# b=b.split('B')
#
# k=0
# for i in a:
#     if 'B' in i:
#         i = i.split('B')
#         k=max(k, len(i[0])+2, len(i[-1])+2)
# for i in b:
#     if 'A' in i:
#         i = i.split('A')
#         k=max(k, len(i[0])+2, len(i[-1])+2)
# print(k)

# def prime(n):
#     for x in range(2, int(n**0.5)+1):
#         if n%x==0:
#             return False
#     return True
#
# def dell(n):
#     res=[]
#     for x in range(2, int(n**0.5)+1):
#         if n%x==0:
#             res.append(x)
#             if x!=n//x:
#                 res.append(n//x)
#     if len(res)>0:
#         return max(res)
#     else:
#         return 0
# c=0
# for i in range(550_000+1,10**100):
#     z=dell(i)
#     if z!=0 and not prime(z):
#         print(i,z)
#         c+=1
#     if c==6:
#         break

# from math import dist
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p1,p) for p1 in cl])
#         if minr>s:
#             res=p
#             minr=s
#     return res
# f=open('2004files/27_9_A.txt')
# e=0.8
# r1=[]
# r2=[]
# vsecl=[]
# a=[[float(x) for x in s.replace(',', '.').split()] for s in f]
#
# while len(a)>0:
#     tcl=[a[-1]]
#     a.pop()
#     for p in tcl:
#         bliz_t=[t1 for t1 in a if dist(t1,p)<e]
#         for x in bliz_t:
#             tcl.append(x)
#             a.remove(x)
#     vsecl.append(tcl)
# print(len(vsecl[0])+len(vsecl[1])+len(vsecl[2])+len(vsecl[3])+len(vsecl[4]),len(vsecl))
# for cl in vsecl:
#     if len(cl) > 1:
#         r1.append(cent(cl)[0])
#         r2.append(cent(cl)[1])
# print(sum(r1)/len(r1)*10_000, sum(r2)/len(r2)*10_000)
# f.close()
#
# f=open('2004files/27_9_B.txt')
# e=1
# r1=[]
# r2=[]
# vsecl=[]
# a=[[float(x) for x in s.replace(',', '.').split()] for s in f]
#
# while len(a)>0:
#     tcl=[a[-1]]
#     a.pop()
#     for p in tcl:
#         bliz_t=[t1 for t1 in a if dist(t1,p)<e]
#         for x in bliz_t:
#             tcl.append(x)
#             a.remove(x)
#     vsecl.append(tcl)
# print(len(vsecl[0])+len(vsecl[1])+len(vsecl[2])+len(vsecl[3])+len(vsecl[4])+len(vsecl[5])+len(vsecl[6]),len(vsecl))
# for cl in vsecl:
#     if len(cl) > 1:
#         r1.append(cent(cl)[0])
#         r2.append(cent(cl)[1])
# print(sum(r1)/len(r1)*10_000, sum(r2)/len(r2)*10_000)
# f.close()