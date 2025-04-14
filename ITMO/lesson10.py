# def prime(z):
#     for i in range(2, int(z**0.5)+1):
#         if z%i==0:
#             return False
#     return True
# def dell(x):
#     r=set()
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0 and prime(i):
#             r.add(i)
#             if prime(x//i):
#                 r.add(x//i)
#     if len(r)>0:
#         return r
#     else:
#         r.add(0)
#         return r

# c=0
# for i in range(50000000+1, 10**10):
#     t1=dell(i)
#     if len(t1)>=6:
#         t=[int(x) for x in t1]
#         t.sort()
#         if t[0]*t[1]*t[2]*t[3]*t[4]*t[5]<i:
#             print(i, t[0]*t[1]*t[2]*t[3]*t[4]*t[5])
#             c+=1
#     if c==10:
#         break

# import re
#
#
# def prime():
#     x = [i for i in range(10 ** 5)]
#     x[1] = 0
#     for i in range(len(x)):
#         if x[i] != 0:
#             for j in range(x[i] * 2, len(x), x[i]):
#                 x[j] = 0
#     return set(x)
#
# def dividers(n):
#     d = set()
#     for div in range(2, int(n ** 0.5) + 1):
#         if n % div == 0:
#             d.add(div)
#             d.add(n // div)
#     return sorted(d, reverse=True)
#
# c=0
# x = prime()
# for n in range(10 ** 8 + 1, 10 ** 10):
#     d = dividers(n)
#     s = ''
#     for el in d:
#         if el in x:
#             s += str(el)
#
#     y = re.fullmatch(r'1\d9\d*3', s)
#     if y:
#         print(n, d[0])
#         c+=1
#     if c==7:
#         break
# with open('text.txt') as f:
#     a=[i.rstrip() for i in f.readlines()]
#     l,c=0,0
#     for i in a:
#         if i.count('A')>=3:
#             l+=len(i)
#             c+=1
#     print(l/c)



# with open('text.txt') as f:
#
#     def freq(let):
#         for el in alph:
#             if el[0]==let:
#                 el[1]+=1
#
#     a=[i.rstrip() for i in f.readlines()]
#     alph='QWERTYUIOPASDFGHJKLZXCVBNM'
#     alph=[[let,0] for let in sorted(alph)]
#     for line in a:
#         for i in range(len(line)-1):
#             if line[i]=='B':
#                 freq(line[i+1])
#     print(sorted(alph, key= lambda x:x[1], reverse=True))

# with open('text.txt') as f:
#     a=f.readline()
# k,m=1,0
# a = a.replace('CA', '*')
# a = a.replace('CO', '*')
# a = a.replace('DA', '*')
# a = a.replace('DO', '*')
# a = a.replace('FA', '*')
# a = a.replace('FO', '*')
# for i in range(len(a)-1):
#     if a[i]==a[i+1]=='*':
#         k+=1
#     else:
#         m=max(m,k)
#         k=1
# print(m)
from sys import setrecursionlimit
setrecursionlimit(99999999)
# def f(n):
#     if n>=1000:
#         return True
#     else:
#         return f(n+1)/(n+1)
# c=0
# for i in range(1, 10_000+1):
#     z=f(i)
#     if z or z%i==0:
#             c+=1
# print(c)


# with open('text.txt') as f:
#     c=[x.rstrip() for x in f.readlines()]
# mina=10**8
# buf=''
# for line in c:
#     if 1<=line.count('A')<mina:
#         mina=line.count('A')
#         buf=line
# count=0
# letter=''
# for l in set(buf):
#     if count<buf.count(l):
#         count=buf.count(l)
#         letter=l
# print(letter)

#поиск числа выражений
# import re
# with open('text.txt') as f:
#     s=f.readline()
# res=re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*',s)
# print(len(max(res, key=len)))
import re

#не работает
with open('text.txt') as f:
    c=f.readline().rstrip()
tmp=1
max_len=0
for i in range(1,len((c))):
    if c[i-1]+c[i] not in ('-0','*0','0-','0*','--','-*','*-','**'):
        tmp+=1
    else:
        if tmp>=max_len:
            max_len=max(max_len, tmp)
            tmp=1

print(max_len)