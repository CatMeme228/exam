# def f(x,y,a):
#     return ((x+3*y+4)<(2*a)) or ((3*x)>=(2*y-4)) or (y>=89)
#
# for a in range(1000):
#     if all(f(x,y,a) for x in range(100) for y in range(100)):
#         print(a)
#         break

# print(17*4/8)
# #8,5 -> 9 байт
# print((9+22)*15)

# alph='0123456789ABCDE'
# for x in alph:
#     for y in alph:
#         p1=f'1{x}59{y}3'
#         p2=f'223{y}{x}9'
#         if (int(p1,23)+int(p2,15))%99==0:
#             print(int(x,15), int(y,15), (int(p1,23)+int(p2,15))/99)

# def f(s,e):
#     if s==e: return True
#     if s>e: return False
#     if s==22: return False
#     return f(s+1, e)+f(s*2, e)
# print(f(5,8)*f(8,60))

# f=open('3cw/17.txt')
# a=[int(x) for x in f]
# mpos=10**10
# for i in a:
#     if abs(i)%10==0:
#         mpos=min(mpos, i)
# mpos=mpos**2
# r1,r2=0,0
# for i in range(len(a)-1):
#     fl=0
#     if abs(a[i])%10==1:
#         fl+=1
#     if abs(a[i+1])%10==1:
#         fl+=1
#     if fl==1 and (a[i]**2+a[i+1]**2)>=mpos:
#         r1+=1
#         r2=max(r2, a[i]**2+a[i+1]**2)
#         # print(a[i],a[i+1], mpos)
# print(r1,r2)

# f=open('3cw/24.txt')
# a=[x.rstrip() for x in f]
# mstr=''
# mQ=0
# llet, lc='',10**10
# for x in a:
#     if x.count('Q')>=mQ:
#         mQ=x.count('Q')
#         mstr=x
# print(mstr, mQ)
# for x in mstr:
#     if mstr.count(x)<=lc:
#         lc=mstr.count(x)
#         llet+=x+str(mstr.count(x))
# print(llet)

# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# for i in range(10_000_000-30, 10_000_000+120):
#     if prime(i):
#         print(i, abs(i-10_000_000))

# from turtle import *
# setworldcoordinates(-20,-20,20,20)
# tracer(11)
# left(90)
# for i in range(2):
#     forward(10)
#     right(90)
#     forward(15)
#     right(90)
# penup()
# forward(10)
# right(90)
# pendown()
# for i in range(2):
#     forward(10)
#     right(90)
#     forward(15)
#     right(90)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         setpos(x,y)
#         dot(4,'red')
# exitonclick()

# def dist(x1,y1,x2,y2):
#     return max(abs(x2-x1), abs(y2-y1))
#
# def cent(a):
#     minr = 10 ** 10
#     for i in range(len(a)):
#         s=0
#         for j in range(len(a)):
#             s+=dist(a[i][0], a[i][1], a[j][0],a[j][1])
#         if minr>s:
#             minr=s
#             res=a[i]
#     return res
#
# f=open('3cw/27a.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[1]>5:
#         a1.append(s)
#     else:
#         a2.append(s)
# res1=cent(a1)
# res2=cent(a2)
# print((res1[0]+res2[0])/2*10_000)
# print((res1[1]+res2[1])/2*10_000)
# f.close()
#
# f=open('3cw/27b.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>3:
#         a1.append(s)
#     else:
#         if s[1]>=-2.5:
#             a2.append(s)
#         else:
#             a3.append(s)
# res1=cent(a1)
# res2=cent(a2)
# res3=cent(a3)
# print((res1[0]+res2[0]+res3[0])/3*10_000)
# print((res1[1]+res2[1]+res3[1])/3*10_000)
# f.close()
# 7 = 30, 34