# for x in range(1000000):
#     if (((x-1)<x)<=(40>x**2)) == 1 and x!=0:
#         print(x)
from binascii import a2b_qp
#6.33
# def f(x,y):
#     return (x+3 * y <a) or (y>2*x) or (x>78)
# for  a in range(1000):
#     if all(f(x,y)for x in range(100) for y in range(200)):
#         print(a)
#         break

#6.32
# for x in range(10000):
#     if ((x*x>65)<=((x-1)>(x*(7+x))))==0:
#         print(x)
#         break

#6.38
#
# def f(x,y):
#     return ((x<=9)<=(x*x<+a)) and ((y*y<=a)<=(y<=9))
# for a in range(1000):
#     if all(f(x,y) for x in range(11) for y in range(11)):
#         print(a)

#6.39

# def f(x):
#     return (x&25!=0)<=((x&17==0)<=(x&a!=0))
# for a in range(1000):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break

#6.43

# def f(x):
#     return ((x&45==0)<=(x&24!=0))<=(x&a!=0)
# for a in range(1000):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break

#6.49

# def f(x):
#     return ((x%2==0)<=(x%3!=0)) or ((x+a)>=80)
#
# for a in range(1,1000):
#     if all(f(x) for x in range(1,1000)):
#         print(a)

#6.52
# from itertools import combinations
# def f(x):
#     p=27<=x<=50
#     q=35<=x<=66
#     a= a1<=x<=a2
#     return p <= ((q and not(a)) <= (not p))
#
# z=[]
# ox=[i/4 for i in range(27*4, (66+1)*4)]
# for a1, a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print(min(z))

#6.53
# from itertools import combinations
# def f(x):
#     p=11<=x<25
#     q=15<=x<=40
#     r=32<=x<=57
#     a= a1<=x<=a2
#     return (not r) or (((not p)<=(not q))<=a)
#
# z=[]
# ox=[i/4 for i in range(11*4, (57+1)*4)]
# for a1, a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print(round(min(z)))

# from itertools import combinations
#
# def f(x):
#     p= 15<=x<40
#     q=21<x<=63
#     a= a1<=x<=a2
#     return (p <= ((q and (not a))<= (not p)))
#
# z=[]
# ox =[i/4 for i in range(15*4, (63+1)*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print((min(z)))

# from itertools import combinations
#
# def f(x):
#     p=11<=x<25
#     q=15<=15<=40
#     a=a1<=x<=a2
#     return ((q<=a)<=p)<=p
#
# z=[]
#
# ox=[i/4 for i in range(11*4, 41*4)]
#
# for a1,a2 in combinations(ox,2):
#     if all(f(x) for x in ox):
#         z.append(a2-a1)
# print(min(z))
# 6.40
# def f(x):
#     return ((x&18)==0)<=(((x&51)!=0)<=((x&a)!=0))
# for a in range(1000):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break

# 6.34
# def f(x,y):
#     return ((x+2*y)<a) or (3*y>2*x) or (x>40)
#
# for a in range(1000):
#     if all(f(x,y) for x in range(41) for y in range(28)):
#         print(a)
#         break

# 6.35
# def f(x,y):
#     return ((x+y)<a) or (3*y>x) or (x>100)
#
# for a in range(1000):
#     if all(f(x,y) for x in range(101) for y in range(35)):
#         print(a)
#         break

#6.36
# def f(a,b):
#     return (2*a+4*b)>17 or (a<=x and b<x)
#
# for x in range(1000):
#     if all(f(a,b) for a in range(9) for b in range(5)):
#         print(x)
#         break

# 6.41
# def f(x):
#     return ((x&19==0)<=(x&56!=0))<=(x&a!=0)
#
# for a in range(1000):
#     if all(f(x) for x in range(1000)):
#         print(a)
#         break
