# f=open('files/24_1p.txt')
# s=f.readline()
import string

# s=s.replace('AA', 'A A')
# s=s.replace('AA', 'A A')
# s=s.split()
# print(len(max(s,key=len)))

# s=s.replace('AD', 'A D')
# s=s.replace('DA', 'D A')
# s=s.split()
# print(len(max(s,key=len)))

#нет accb
# s=s.replace('ACCB', 'ACC CCB')
# s=s.split()
# print(len(max(s,key=len)))

# m=0
# s=s.replace('D','E')
# s=s.split('E')
# print(len(max(s, key = len)))
# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         t=s[l:r+1]
#         if 'D' in t or 'E' in t:
#             break
#         else:
#             m=max(m, len(t))
# print(m)

# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         t=s[l:r+1]
#         if 'A' in t:
#             break
#         else:
#             m=max(m, len(t))
# print(m)

# s=s.replace('AA','A A')
# s=s.replace('AA','A A')
# s=s.replace('BB','B B')
# s=s.replace('BB','B B')
# s=s.replace('CC','C C')
# s=s.replace('CC','C C')
# s=s.replace('DD','D D')
# s=s.replace('DD','D D')
# s=s.replace('EE','E E')
# s=s.replace('EE','E E')
# s=s.split()
# print(len(max(s, key = len)))

# s=s.replace('AA','A A')
# s=s.replace('AA','A A')
# s=s.split()
# print(len(max(s, key = len)))

# f=open('files/24_23osn.txt')
# s=f.readline()
# m,k=0,0
# for i in s:
#     if i in '0123456789ABCDEFGH':
#         k+=1
#     else:
#         m=max(k,m)
#         k=0
# print(m)

#не более 120 A
# f=open('files/24_23osn1.txt')
# s=f.readline()
# l,r,m=0,0,0
# lA, kA=120,0
# for r in range(len(s)):
#     if s[r]=='A':
#         kA+=1
#     while kA>lA:
#         if s[l]=='A':
#             kA-=1
#         l+=1
#     m=max(m,r-l+1)
# print(m)

#не менее 120 A
# f=open('files/24_23osn1.txt')
# s=f.readline()
# l,r,m=0,0,10**10
# lA, kA=120,0
# for r in range(len(s)):
#     if s[r]=='A':
#         kA+=1
#     while kA==lA:
#         m = min(m, r - l + 1)
#         if s[l]=='A':
#             kA-=1
#         l+=1

# #ровно 21 AB
# s=open('files/24var07.txt').readline()
# m=0
# for l in range(len(s)):
#     for r in range(l+m,len(s)):
#         t=s[l:r+1]
#         if t.count('AB')==21:
#             m=max(m,len(t))
#         elif t.count('AB')>21:
#             break
# print(m)

#не более 500 а без е
# s=open('files/24var04.txt').readline()
# m=0
# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         t=s[l:r+1] #перебор всех подсток
#         if t.count('A')<=500 and t.count('E')==0:
#             m=max(m, len(t))
#         else:
#             break
# print(m)

#досрок
# s=open('files/24_25dosr.txt').readline()
# m14=''
# m10=0
# t=''
# for i in s:
#     if i in '0123456789ABCD':
#         t+=i
#         if int(t,14)>m10 and i in '02468AC':
#             m10=int(t,14)
#             m14=t
#     else:
#         t=''
#
#
# zeros=0
# for i in m14:
#     if i=='0':
#         zeros+=1
#     else:
#         print()
#     print(len(m14)-zeros)
#     break

# s=open('files/24_25dosr.txt').readline()
# m=0
# alf=string.ascii_uppercase
# for x in alf[4:]:
#     s=s.replace(x, ' ')
# s1=s.split()
# for ts in s1:
#     for l in range(len((ts))):
#         if ts[l]!='0':
#             for r in range(l, len(ts)):
#                 t=ts[l:r+1]
#                 if int(t,14)%13==0:
#                     m=max(m,len(t))
# print(m)

# f= open('files/26_2_ЕГЭ_2024_День2.txt')
# stud=[]
# n,st=map(int, f.readline().split())
# for s in f:
#     a = [int(z) for z in s.split()]
#     a.append(sum(a))
#     stud.append(a)
# stud.sort(key=lambda x: (x[3], x[1], x[2]),reverse=True)
# print(stud[st-1][3], stud[st-1][1])

# f= open('files/26real2021_den1.txt')
# mt=[]
# res=[]
# n=map(int, f.readline().split())
# for s in f:
#     a = [int(z) for z in s.split()]
#     mt.append(a)
# mt.sort()
# for i in range(len(mt)-1):
#     if mt[i+1][0]==mt[i][0]:
#         if mt[i+1][1]-mt[i][1]==3:
#             res.append([mt[i][0], mt[i][1]+1])
# print(res)

# f=open('files/26_3_03.txt')
#
# n=int(f.readline())
# a=[int(x) for x in f]
# a.sort(reverse=True)
# res=[]
# while len(a)>0:
#     blok = [a[0]]
#     a.pop(0)
#     for x in a[:]:
#         if blok[-1]-x >=7:
#             blok.append(x)
#             a.remove(x)
#     res.append(len(blok))
# print(len(res), max(res))

# f=open('files/26real2022_den1.txt')
# n=int(f.readline())
# a=[int(x) for x in f]
# a.sort(reverse=True)
# k=n//4
# print(sum(a[:k])/2+sum(a[k:]))
# a.sort()
# print(sum(a[:k])/2+sum(a[k:]))

# f=open('files/26_3_04.txt')
# k=int(f.readline())
# n=int(f.readline())
#
# a=[[int(x) for x in s.split()] for s in f]
# a.sort()
# cam=[0]*k
# r1,r2=0,0
# for i in range(len(a)):
#     for j in range(k):
#         if a[i][0]>cam[j]:
#             cam[j]=a[i][1]
#             r1+=1
#             r2=j+1
#             break
# print(r1,r2)

# f=open('files/26real2023_den1.txt')
# n=int(f.readline())
# a=[[int(x) for x in s.split()] for s in f]
# a.sort(key=lambda x:[x[1],x[0]])
# res=[a[0]]
# for x in a:
#     if x[0]>=res[-1][1]:
#         res.append(x)
# print(len(res))
# print(max(a)[0]-res[-2][1])


# from math import *
# from turtle import *
# from random import *
# def visual(vsecl):
#     tracer(0)
#     screensize(1000,1000)
#     c=60
#     penup()
#     for cl in vsecl:
#         color= (random(), random(),random())
#         for p in cl:
#             goto(p[0]*c, p[1]*c)
#             dot(10, color)
#     exitonclick()
#
# def cent(cl):
#     minr=10**10
#     for p in cl:
#         s=sum([dist(p,p0) for p0 in cl])
#         if minr>s:
#             minr =s
#             res=p
#     return res
#
# f=open('files/27b.txt')
# a1=[[float(x) for x in s.replace(',', '.').split()] for s in f]
# for e in range(1,100):
#     vsecl = []
#     a=a1[:]
#     while len(a)>0:
#         tcl=[a[-1]]
#         a.pop()
#         for p in tcl:
#             for p1 in a[:]:
#                 if dist(p,p1)<=e/10:
#                     tcl.append(p1)
#                     a.remove(p1)
#         if len(tcl) > 10:
#             vsecl.append(tcl)
#     if len(vsecl)==3:
#         visual(vsecl)
#         res1,res2,k=0,0,0
#         for cl in vsecl:
#                 s=cent(cl)
#                 res1+=s[0]
#                 res2+=s[1]
#                 k+=1
#         print(res1/k*10_000, res2/k*10_000)
#         break

# from math import *
# from turtle import *
# from random import *
# def visual(vsecl):
#     tracer(0)
#     screensize(1000,1000)
#     c=50
#     penup()
#     for cl in vsecl:
#         color= (random(), random(),random())
#         for p in cl:
#             goto(p[0]*c, p[1]*c)
#             dot(10, color)
#     exitonclick()
#
# def sklad(cl):
#     m=0
#     for p in cl:
#         st=[]
#         for p1 in cl:
#             if dist(p,p1)<=1:
#                 st.append(p1)
#         k2=0
#         for p2 in cl:
#             st1=[]
#             if p2!=p1:
#                 for p1 in cl:
#                     if p1 not in st:
#                         if dist(p2,p1)<=1:
#                             st.append(p1)
#                 k2=max(k2,len(st1))
#         m=max(m+k2,len(st))
#     return m
#
# f=open('files/27_105A.txt')
# a1=[[float(x) for x in s.replace(',', '.').split()] for s in f]
# e=1
# vsecl = []
# a=a1[:]
# while len(a)>0:
#         tcl=[a[-1]]
#         a.pop()
#         for p in tcl:
#             for p1 in a[:]:
#                 if dist(p,p1)<=e:
#                     tcl.append(p1)
#                     a.remove(p1)
#         vsecl.append(tcl)
#
# visual(vsecl)
# res1,res2,k=0,0,0
# for cl in vsecl:
#         s=sklad(cl)
#         print(s)
#         res1+=s[0]
#         res2+=s[1]
#         k+=1
# print(res1/k*10_000, res2/k*10_000)

from re import *
# f=open('files/24var02.txt')
# s=f.readline().strip()
# a=findall(r'(?:0|[5-8][05-8]*)(?:[+-](?:0|[5-8][05-8]*))*',s)
# print(len(max(a, key=len)))

#равно 0
# f=open('files/24_24rezerv0.txt')
# s=f.readline().strip()
# num=r'([1-9][0-9]*|0)'
# pr= rf'({num}\*)*0(\*{num})*'
# reg= rf'{pr}(\+{pr})*'
# n=len(max([x.group() for x in finditer(reg,s)], key=len))
# print(n)
#
# f=open('files/24_24rezerv0.txt')
# s=f.readline().strip()
# for x in '23456789':
#     s=s.replace(x,'1')
# m=0
# for l in range(len(s)-1):
#     if s[l]!='+' and s[l]!='*' and s[l]+s[l+1]!='01' and s[l]+s[l+1]!='00':
#         for r in range(l+m, len(s)):
#             st=s[l:r+1]
#             if '++' not in st and '**' not in st and '+*' not in st and '*+' not in st and '+01' not in st and '+00' not in st and '*01' not in st and '*00' not in st:
#                 if st[-1]!='+' and st[-1]!='*':
#                     if eval(st)==0:
#                         m=max(len(st),m)
#             else:
#                 break
# print(m)

#максимальная
# f=open('files/24-280.txt')
# s=f.readline()
# m=0
# for l in range(len(s)):
#     for r in range(l+m, len(s)):
#         st=s[l:r+1]
#         if st.count('X')==5 and st.count('Y')==5 and st.count('Z')==5:
#             m=max(m, len(st))
#         elif st.count('X')>5 or st.count('Y')>5 or st.count('Z')>5:
#             break
# print(m)

#минимальная
f=open('files/24-280.txt')
s=f.readline()
m=290
for l in range(len(s)):
    for r in range(l+m,l,-1):
        st=s[l:r+1]
        if st.count('X')==5 and st.count('Y')==5 and st.count('Z')==5:
            m=min(m, len(st))
        elif st.count('X')<5 or st.count('Y')<5 or st.count('Z')<5:
            break
print(m)