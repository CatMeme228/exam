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

from math import dist

def cent(cl):
    minr=10**10
    for p in cl:
        s=sum([dist(p,p0) for p0 in cl])
        if minr>s:
            minr=s
            res=p
    return res

f=open('files/27a.txt')
a1,a2=[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if s[1]>15:
        a1.append(s)
    else:
        a2.append(s)
r1=cent(a1)
r2=cent(a2)
print((r1[0]+r2[0])/2*10_000)
print((r1[1]+r2[1])/2*10_000)

f=open('files/27b.txt')
a1,a2,a3=[],[],[]
for s in f:
    s=s.replace(',','.')
    s=s.split()
    s=[float(x) for x in s]
    if s[1]>15:
        a1.append(s)
    else:
        a2.append(s)
r1=cent(a1)
r2=cent(a2)
r3=cent(a3)
print((r1[0]+r2[0]+r3[0])/3*10_000)
print((r1[1]+r2[1]+r3[0])/3*10_000)
