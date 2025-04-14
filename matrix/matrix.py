#17
# from fnmatch import *
# for i in range(1991,10**8+1, 1991):
#     s=str(i)
#     if fnmatch(s, "2*1?71") and i%1991==0:
#         print(i, i//1991)
from array import array
from itertools import filterfalse, product
from math import trunc
from pdb import runctx
from pickle import FALSE
from turtledemo.sorting_animate import enable_keys


# from fnmatch import *
# for i in range(3123, 10**8+1, 3123):
#     s=str(i)
#     if fnmatch(s, '3?1*57') and i%3123==0:
#         print(i, i//3123)

# from fnmatch import *
# for i in range(2024, 10**10+1, 2024):
#     s=str(i)
#     if fnmatch(s,"3?2758*4"):
#         print(i)

# def sumnum(x):
#     tmp=str(x)
#     res=0
#     for i in tmp:
#         res+=int(i)
#     return res
# from fnmatch import *
# for i in range(2024, 10**8+1, 2024):
#     s=str(i)
#     if fnmatch(s,"1?4*78*"):
#         if sumnum(i)<35:
#             print(i)

# from fnmatch import *
# for i in range(3123, 10**8+1, 3123):
#     if fnmatch(str(i), '3?1*57'):
#         if bin(i)[2::].count("1")<11:
#             print(i)

# for b in range(2,52):
#     for n in range(3,19):
#         a=b**n
#         if 105000<=a<=135200:
#             print(a, b,n)

# res=[]
# for m in range(1,30,2):
#     for n in range(0,21,2):
#         z=2**m*3**n
#         if 250_000_000<=z<=450_000_000:
#             res.append([z])
# res.sort()
# print(*res)

# res=[]
# for i in range(2,150):
#     tmp=i*(i+1)*(i+2)
#     for j in range(3, 8):
#         tmp=tmp*(i+j)
#         if 100_000<=tmp<=250_000:
#             res.append([tmp,i,i+j])
#
# print(res)

#поиск делитей
# res = 0
# i=36
# for j in range(1, int(i**0.5)+1):
#     if i==j**2:
#         res+=0.5
#     elif i % j == 0:
#         res += 1
# print(int(res*2))



# for i in range(10271400, 10272501):
#     res = 0
#     for j in range(1, int(i**0.5)+1):
#         if i%j==0:
#             res+=1
#         elif i==j**2:
#             res+=0.5
#     if res*2==4:
#         print(i)
# print(res)

# def delc(i):
#     res = []
#     for j in range(2, int(i ** 0.5) + 1):
#         if j ** 2 == i:
#             res.append(j)
#         elif i % j == 0:
#             res.append(j)
#             res.append(i // j)
#     res.sort()
#     return res
# for i in range(310_235, 310_300+1):
#     if len(delc(i))==4:
#         print(*delc(i))

# def delc(x):
#     res=[]
#     for i in range(1, int(x**0.5)+1):
#         if i**2==x:
#             res.append(i)
#         elif x%i==0:
#             res.append(i)
#             res.append(x//i)
#     return len(res)
#
# maxkd=0
# for i in range(124052, 124131):
#     kd=delc(i)
#     if kd>maxkd:
#         maxkd=kd
#         res=i
# print(maxkd, res)

# def delc(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if i**2==x:
#             res.append(i)
#         elif x%i==0:
#             res.append(i)
#             res.append(x//i)
#     if len(res)==0:
#         return 0
#     else:
#         return max(res)-min(res)
# c=0
# for i in range(700_000,0, -1):
#     m=delc(i)
#     if m%17==0 and m!=0:
#         print(i, m)
#         c+=1
#     if c==5:
#         break

# def delc(x):
#     res=[]
#     for i in range(2, int(x**0.5)+1):
#         if i**2==x:
#             res.append(i)
#         elif x%i==0:
#             res.append(i)
#             res.append(x//i)
#     if len(res)==0:
#         return 0
#     else:
#         return max(res)+min(res)
#
# c=0
# for i in range(900_001,10**10):
#     m=delc(i)
#     if m%10==4:
#         print(i,m)
#         c+=1
#     if c==5:
#         break

# def f(x):
#     r=[]
#     for i in range(1, int(x**0.5)+1):
#         if x%i==0:
#             if i!=9 and i%10==9:
#                 r.append(i)
#             if i!=x//i and (x//i)!=9 and (x//i)%10==9:
#                 r.append(x//i)
#     if len(r)>0:
#         return min(r)
#     else:
#         return 0
#
# c=0
# for i in range(567001, 10**10):
#     z=f(i)
#     if z!=0:
#         print(i, z)
#         c+=1
#     if c==5:
#         break


# def pn(n):
#     res=[]
#     for i in range(1,int(n**0.5)+1):
#         if n%i==0:
#             res.append(i)
#             if n//i!=i:
#                 res.append(n//i)
#     return res
#
# for i in range(4_000_000, 12_000_000+1):
#     if i**0.5==int(i**0.5):
#         z=pn(i)
#         if len(z)==5:
#             z.sort()
#             print(i, z[-2])

# from fnmatch import *
# for i in range(2321,10**8, 2321):
#     if fnmatch(str(i), '1*2??76'):
#         print(i, i//2321)

# def prime_n(x):
#     for i in range(2,int(x**0.5)):
#         if x%i==0:
#             return False
#     return True

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def del_pr(n):
#     d=[]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 d.append(i)
#             if i!=n//i and prime(n//i):
#                 d.append(n//i)
#     return d
#
# md=0
# for i in range(2, 20_000+1):
#     sp=del_pr(i)
#     if md< len(sp):
#         md=len(sp)
#         res=i
# print(res, md)

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return  False
#     return True
# def maxdel_isprime(n):
#     d=[]
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             d.append(i)
#             if i!=n//i:
#                 d.append(n//i)
#     if len(d)!=0:
#         if prime(max(d)):
#             return 0
#         else:
#             return max(d)
#     else:
#         return 0
# c=0
# for i in range(450_001, 10**8):
#     tmp=maxdel_isprime(i)
#     if tmp!=0:
#         print(i, tmp)
#         c+=1
#     if c==6:
#         break

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def s(n):
#     d=[]
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 d.append(i)
#             if i!=n//i and prime(n//i):
#                 d.append(n//i)
#     if len(d)>0:
#         return sum(d)
#     else:
#         return 0
#
# c=0
# for i in range(550_000+1, 10**8):
#     tmp=s(i)
#     if tmp%10==7:
#         print(i,tmp)
#         c+=1
#     if c==5:
#         break

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def m(n):
#     d=[]
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 d.append(i)
#             if i!=n//i and prime(n//i):
#                 d.append(n//i)
#     if len(d)>0:
#         return max(d)+min(d)
#     else:
#         return 0
#
# c=0
# for i in range(1_000_000+1, 10**100):
#     tmp=m(i)
#     if tmp>1000 and tmp%10==5:
#         print(i,tmp)
#         c+=1
#     if c==5:
#         break

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def sum_dig(n):
#     res=0
#     for i in str(n):
#         res+=int(i)
#     return res
#
# for i in range(120_120, 230_230+1):
#     if prime(i):
#         tmp=sum_dig(i)
#         if tmp>=44:
#             print(i, tmp)


# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def m(n):
#     d_chet=[]
#     d_nechet=[]
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if i%2==0:
#                 d_chet.append(i)
#             elif i%2!=0:
#                 d_nechet.append(i)
#             if i!=n//i and (n//i)%2==0:
#                 d_chet.append(n//i)
#             elif i!=n//i and (n//i)%2!=0:
#                 d_nechet.append(n//i)
#     if len(d_nechet)>0 and len(d_chet)>0:
#         return abs(max(d_chet)-max(d_nechet))
#     else:
#         return 0
#
# c=0
# for i in range(100_001, 10**100):
#     tmp=m(i)
#     if prime(tmp) and tmp%10==7:
#         print(i,tmp)
#         c+=1
#     if c==4:
#         break


# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def m(n):
#     d=[]
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 d.append(i)
#             if i!=n//i and prime(n//i):
#                 d.append(n//i)
#     if len(d)>0:
#         return max(d)+min(d)
#     else:
#         return 0
# c=0
# for i in range(1200000+1, 10**100):
#     tmp=m(i)
#     if tmp>2000 and tmp%10==8:
#         print(i, tmp)
#         c+=1
#     if c==5:
#         break
# from fnmatch import *
# def delc(n):
#     d=[]
#     for i in range(1, int(n**0.5)+1):
#         if n%i==0:
#             if i%2!=0:
#                 d.append(i)
#             if i!=n//i and (n//i)%2!=0:
#                 d.append(n//i)
#     if len(d)>0:
#         return d
#     else:
#         return 0
#
# c=0
# for i in range(100_001,10**100):
#     if fnmatch(str(i), '1*1?2'):
#         tmp = delc(i)
#         if len(tmp)==3:
#             print(i, sum(tmp))
#             c+=1
#     if c==5:
#         break

# from fnmatch import *
# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def mult_num(n):
#     res=1
#     for i in str(n):
#         res*=int(i)
#     return res
#
# for i in range(1234, 10**9+1, 1234):
#     if fnmatch(str(i), '24?127*0'):
#         tmp=prime(mult_num(i))
#         if tmp:
#             print(i, i//1234)

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def delc(n):
#     d=[]
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 if i!=n//i and prime(n//i):
#                     return True
#     return False
# c=0
# m=100000000000000000000000
# for i in range(268312, 336492+1):
#     tmp=delc(i)
#     if tmp:
#         c+=1
#         m= min(m, i)
# print(c,m)

# from fnmatch import *
# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def delc(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 if i!=n//i and prime(n//i):
#                     if prime(i+n//i):
#                         return i+n//i
#     return False
#
# for i in range(1, 10**7):
#     if fnmatch(str(i), '13?45*8'):
#         tmp=delc(i)
#         if tmp!=False:
#             print(i, tmp)

# def prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# def xyi(n):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             if prime(i):
#                 if xyi2(n//i, i):
#                     return True
#     return False
#
# def xyi2(n, old):
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0 and i!=old:
#             if prime(i):
#                 if (n//i)!=old and i!=n//i:
#                     if prime(n//i):
#                         return True
#     return False
# m,k=0,0
# for i in range(105673, 220784+1):
#     if xyi(i):
#         k+=1
#         m=max(i,m)
# print(k, m)

# c=0
# for i in range(0,10):
#     for j in range(0,100):
#         for z in range(10):
#             #s='1'+str(i)+'2'+str(j).zfill(2)+'3'+str(z)+'0'
#             s=f'1{i}2{j:02}3{z}0'
#             if int(s)<=10**8 and int(s)%2022==0:
#                 print(s, int(s)//2022)

# def prime(x):
#     for i in range(2, int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# from fnmatch import *
# def sum_num(n):
#     res=0
#     for i in str(n):
#         res+=int(i)
#     return res
# for i in range(1234, 10**10+1,1234):
#     if fnmatch(str(i), '14?127*0'):
#         if prime(sum_num(i)):
#             print(i, i//1234)


#26.1
# with open('text.txt') as f:
#     d,n = map(int, f.readline().split()) #1ая строка
#     a=[int(x) for x in f]
#     a.sort()
#     s, k,z=0,0,0
#     for x in a:
#         if s+x<=d:
#             s+=x
#             k+=1
#             pos=x
#         else:
#             break
#     maxt=pos+d-s #максимальный теоритический
#     for x in a:
#         if x>maxt:
#             z+=1
#     print(k,z)

#26.2
# with open('text.txt') as f:
#     money,kolvo =map(int, f.readline().split())
#     a=[int(x) for x in f]
#     redk = [int(x) for x in a if x>3000]
#     enc = [int(x) for x in a if 2000<=x<=3000]
#     ob = [int(x) for x in a if x<2000]
#     ob.sort()
#     zan = max(redk)+min(redk)+sum(enc)
#     svo=money-zan
#     s,res1=0,0
#     for x in ob:
#         if s+x<=svo:
#             s+=x
#             res1+=1
#             pos=x
#     ost_dr=[int(x) for x in ob if x<=(svo-s+pos)]
#     print(res1+2+len(enc), max(ost_dr))

#26.3
# with open('text.txt') as f:
#     kolvo=int(f.readline())
#     a = [int(x) for x in f]
#     a.sort(reverse=True)
#     tmp=max(a)
#     z = [tmp]
#     for i in range(len(a)-1):
#         if tmp-a[i+1]>=7:
#             z.append(a[i+1])
#             tmp=a[i+1]
#     print(len(z), min(z))

#26.4
# with open('text.txt') as f:
#     kolvo=int(f.readline())
#     a = [int(x) for x in f]
#     a.sort()
#     tmp=min(a)
#     print(a)
#     z = [tmp]
#     for i in range(len(a)-1):
#         if -tmp+a[i+1]>=7:
#             z.append(a[i+1])
#             tmp=a[i+1]
#     print(len(z), max(z))

#26.5
# with open('text.txt') as f:
#     kolvo=int(f.readline())
#     matr=[]
#     for s in f:
#         a=[int(x) for x in s.split()]
#         matr.append(a)
#     matr.sort()
#     res1,res2=0,0
#     for i in range(len(matr)-1):
#         if matr[i][0]==matr[i+1][0]:
#             if matr[i+1][1]-matr[i][1]==14:
#                 res1=matr[i][0]
#                 res2=matr[i][1]+1
#                 print(res1,res2) #берём 1ое вхождение последнего ряда

#26.6
# from math import ceil
# with open('text.txt') as f:
#     kolvo=int(f.readline())
#     a = [int(x) for x in f]
#     a.sort()
#     do100=[x for x in a if x<=100]
#     s= [x for x in a if x>100]
#     ksale=len(s)//2
#     ssale=sum(s[:ksale])
#     sost=sum(s)-ssale
#     res1= sum(do100)+ssale*0.7+sost
#     res2= max(s[:ksale])
#     print(ceil(res1), res2)

#26.10
# with open('text.txt') as f:
#     n,km =map(int, f.readline().split())
#     matr=[]
#     for s in f:
#         a=[int(x) for x in s.split()]
#         su=sum(a)
#         a.append(su)
#         matr.append(a)
#     matr.sort(key= lambda x: [x[3], x[1], x[2]], reverse=True)
#     res1=matr[km-1][0]
#     res2=matr[km-1][1]
#     print(res1,res2)

#26.11
# with open('text.txt') as f:
#     n,km =map(int, f.readline().split())
#     matr=[]
#     for s in f:
#         a=[int(x) for x in s.split()]
#         su=sum(a)-a[0]
#         a=[su, a[3], a[0], a[1],a[2]]
#         matr.append(a)
#     matr.sort()
#     matr.sort(key= lambda x: [x[0], x[1]], reverse=True)
#     res1=matr[km-1][0]
#     res2=matr[km-1][1]
#     print(matr[km-1][2])
#     k= len([1 for x in matr if x[0]==matr[km-1][0]])
#     print(k)

#2
# from itertools import *
# def f(a,b,c,d):
#     return ((not a) and (not b)) or (b==c) or d
#
# for i in product([0,1], repeat=4):
#     table=[
#         (i[0], i[1],1,i[2]),
#         (1,0,i[3],1),
#         (0,0,1,1)
#     ]
#     if len(table)==len(set(table)):
#         for p in permutations('abcd'):
#             if [f(**dict(zip(p,row))) for row in table]==[0,0,0]:
#                 print(p)


#26.71
# with open('text.txt') as f:
#     k=int(f.readline())
#     n=int(f.readline())
#     a=[]
#     for s in f:
#         s=[int(x) for x in s.split()]
#         a.append(s)
#     a.sort()
#     res1,res2=0,0
#     kam=[-1]*k
#     for x in a:
#         st=x[0]
#         fin=x[1]
#         for i in range(len(kam)):
#             if st>kam[i]:
#                 kam[i]=fin
#                 res1+=1
#                 res2=i+1
#                 break
#    print(res1, res2)

#26.72
# with open('text.txt') as f:
#     res1,res2=0,0
#     n= int(f.readline())
#     l=80
#     m=20
#     a=[]
#     for s in f:
#         x=s.split()
#         x=[int(x[0]), int(x[1]), x[2]]
#         a.append(x)
#     park=[-1]*100
#     a.sort()
#     for x in a:
#         st, fin, vid= x[0], x[0]+x[1], x[2]
#         if vid=='A':
#             for i in range(len(park)):
#                 if st>park[i]:
#                     res1 += 1
#                     park[i]=fin
#                     break
#                 elif st==park[i] and i<=80:
#                     res1 += 1
#                     park[i] = fin
#                     break
#             else:
#                 res2+=1
#         else:
#             for i in range(l, len(park)):
#                 if st>=park[i]:
#                     park[i]=fin
#
#                     break
#             else:
#                 res2+=1
#     print(res1,res2)

#26.73
# with open('text.txt') as f:
#     res1,res2=0,0
#     m,n= map(int, f.readline().split())
#     a=[]
#     kolch=[0]*m
#     for s in f:
#         x=[int(x) for x in s.split()]
#         a.append(x)
#     a.sort(key = lambda x:[x[0]])
#     maxoj=-1
#     poslch=[0]*m
#     bank=[-1]*m
#     for x in a:
#         st,dl = x[0], x[1]
#         mink=min(bank)
#         iban= bank.index(mink)
#         kolch[iban]+=1
#         if st>=mink:
#             bank[iban]=st+dl
#             poslch[iban]=st
#         else:
#             bank[iban]= mink+dl
#             maxoj=max(mink-st, maxoj)
#             poslch[iban]=mink
#             res1=maxoj
#     maxi=0
#     for i in range(len(kolch)):
#         if maxi<kolch[i]:
#             maxi=kolch[i]
#             res2=poslch[i]
#     print(res1,res2)

#6.74
# with open('text.txt') as f:
#     res1,res2=0,0
#     n= int(f.readline())
#     a=[]
#     for s in f:
#         x=[int(x) for x in s.split()]
#         a.append(x)
#     a.sort()
#     ok1=[0]*24*60
#     ok2 = [0] * 24 * 60
#     tsv1,tsv2=0,0
#     for x in a:
#         st=x[0]
#         dl=x[1]
#         ok=x[2]
#         if ok==1 or (ok==0 and ok1[st]<=ok2[st]):
#             if ok1[st]<14:
#                 tsv1 = max(st, tsv1)+dl
#                 for i in range(st,tsv1):
#                     ok1[i]+=1
#             else:
#                 res2+=1
#         elif ok==2 or (ok==0 and ok1[st]>ok2[st]):
#             if ok2[st]<14:
#                 tsv2 = max(st, tsv2)+dl
#                 res1+=1
#                 for i in range(st,tsv2):
#                     ok2[i]+=1
#             else:
#                 res2+=1
#     print(res1,res2)

#12
# for n in range(3,100):
#     a='2'+'5'*n
#     while '25' in a or '355' in a or '555' in a:
#         if '25' in a:
#             a=a.replace('25', '5', 1)
#         if '355' in a:
#             a=a.replace('355', '52', 1)
#         if '555' in a:
#             a=a.replace('555', '3', 1)
#     if a.count('3')==2:
#         print(n)
#         break

#не более одной точки
# with open('text.txt') as f:
#     a=f.readline()
# a=a.split('.')
# m=0
# for i in range(len(a)-1):
#     t=len(a[i])+len(a[i+1])+1
#     m=max(m,t)
# print(m)

#не более 2 точек
# with open('text.txt') as f:
#     a=f.readline()
# a=a.split('.')
# m=0
# for i in range(len(a)-2):
#     t=len(a[i])+1+len(a[i+1])+1+len(a[i+2])
#     m=max(m,t)
# print(m)

# with open('text.txt') as f:
#     a=f.readline()
# a=a.split('A')
# m=0
# for i in range(len(a)-1):
#     if a[i].count('B')+a[i+1].count('B')>=3:
#        m=max(m, len(a[i])+1+len(a[i+1]))
# print(m)

#не более 140 х
# with open('text.txt') as f:
#     a=f.readline()
# a=a.split('X')
# m=0
# for i in range(len(a)-140):
#     t=a[i:i+141]
#     z=140
#     for j in range(i,i+141):
#         z+=len(a[j])
#     m=max(m,z)
# print(m)

#не менее 140 х
# f = open('text.txt')
# s = f.readline() # считываем файл
# s = s.split('X') # сплитим по иксам
# k = 140 # количество х
# tk = k
# mink = 10**6
#
# for i in range (1, k): # создаем первую сумму 0...140
#     tk += len(s[i])
#
# mink = tk # первое минимальное количество
# for i in range(2, len(s) - k + 1): # проходимся по элементам s
#     tk = tk - len(s[i - 1]) + len(s[i + k-2]) # удаляем предыдущий элемент и прибавляем следующий
#     mink = min(mink, tk) # проверяем на максимальность
# print(mink)

#a 35 раз
# with open('text.txt') as f:
#     s=f.readline()
# const=35
# kmin=10**10
# s=s.split('A')
# for i in range(1, len(s)-const-2):
#     kt=const
#     for j in range(i, i+const-1):
#         kt+=len(s[j])
#     kmin=min(kmin, kt)
# print(kmin)

#a не менее 500
# f=open('text.txt')
# s=f.readline()
# f.close()
# s=s.split('A')
# k=500
# kmin=10**10
# tk=k
# for i in range(1, k):
#     tk+=len(s[i])
# kmin=min(tk, kmin)
# for i in range(2, len(s)-k+1):
#     tk=tk-len(s[i-1])+len(s[i+k-2])
#     kmin=min(kmin, tk)
# print(kmin)

#AB 21 раз
# with open('text.txt') as f:
#     s=f.readline()
# s=s.replace('AB', 'A*B')
# s=s.split('*')
# maxk=0
# k=21
# tk=0
# for i in range(k+1):
#     tk+=len(s[i])
# maxk=tk
# for i in range(1, len(s)-k):
#     tk=tk-len(s[i-1])+len(s[i+k])
#     maxk=max(maxk, tk)
# print(maxk)

#не более 700 A и без E
# with open('text.txt') as f:
#     sn=f.readline()
# sn=sn.split('E')
# maxt=0
# for x in sn:
#     s=x
#     s=s.split('A')
#     k=700
#     su=k
#     if len(s)>k+1:
#         for i in range(0,k+1):
#             su+=len(s[i])
#         maxt=su
#         for i in range(0, len(s)-(k+1)):
#             su=su-len(s[i])+len(s[i+k+1])
#             maxt=max(maxt, su)
# print(maxt)

#a 2024 раз
# f = open('text.txt')
# a = f.readline()
# a = a.split('A')
# ka = 2024
# print(a[0])
# ta = a[1:ka]
# mins = ka
# for i in range(len(ta)):
#     mins += len(ta[i])
# td = mins
# for i in range(2, len(a) - 1 - (ka - 2)):
#     td = td + len(a[i +ka - 2]) - len(a[i-1])
#     mins = min(mins,td)
# print(mins)

#a не менее 490
# f=open('text.txt')
# s=f.readline()
# f.close()
# s=s.split('A')
# k=490
# kmin=10**10
# tk=k
# for i in range(1, k):
#     tk+=len(s[i])
# kmin=min(tk, kmin)
# for i in range(2, len(s)-k+1):
#     tk=tk-len(s[i-1])+len(s[i+k-2])
#     kmin=min(kmin, tk)
# print(kmin)

#не более 700 A и без E
# with open('text.txt') as f:
#     sn=f.readline()
# sn=sn.split('E')
# maxt=0
# for x in sn:
#     s=x
#     s=s.split('A')
#     k=500
#     su=k
#     if len(s)>k+1:
#         for i in range(0,k+1):
#             su+=len(s[i])
#         maxt=su
#         for i in range(0, len(s)-(k+1)):
#             su=su-len(s[i])+len(s[i+k+1])
#             maxt=max(maxt, su)
# print(maxt)

#a 35 раз
# f = open('24.txt')
# s = f.readline()
# s = 'A' + s + 'A'
# s = s.replace('A',' A')
# s = s.replace('B',' B')
# s = s.split()
# maxs = 0
# for i in range(1, len(s) - 1):
#     if s[i][0] + s[i+1][0] == 'AB' or s[i][0] + s[i+1][0] == 'BA':
#         maxs = max(maxs, len(s[i]) + len(s[i+1]) + len(s[i-1]) - 1)
# print(maxs)

# from sys import setrecursionlimit
# setrecursionlimit(99999999)
# def F(n):
#
#   if n > 0:
#
#     F(n // 3)
#
#     print(n, end="")
#
#     F(n - 3)
# print(F(9))

#шаблон 27
# def dist(x1,y1,x2,y2):
#   return ((x1-x2)**2+(y1-y2)**2)**0.5
#
# def cent(a):
#   minr=10**10
#   for i in range(len(a)):
#     s=0
#     for j in range(len(a)):
#       x1=a[i][0]
#       y1=a[i][1]
#       x2 = a[j][0]
#       y2 = a[j][1]
#       s+=dist(x1,y1,x2,y2)
#     if s<minr:
#       minr=s
#       res = a[i]
#   return res
#
# f= open('17.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>5:
#         a1.append(s)
#     else:
#         if s[1]>6:
#             a2.append(s)
#         else:
#             a3.append(s)
#
# res1=cent(a1)
# res2=cent(a2)
# res3=cent(a3)
# print((res1[0]+res2[0]+res3[0])/3*10000)
# print((res1[1]+res2[1]+res3[1])/3*10000)

# f=open('17.txt')
# a=[int(x) for x in f]
# r1,r2=0,10**10
# for i in range(len(a)-1):
#   if a[i]>0 and int(a[i]**0.5)==a[i]**0.5 or a[i+1]>0 and int(a[i+1]**0.5)==a[i+1]**0.5:
#     r1+=1
#     r2=min(r2, a[i]+a[i+1])
# print(r1,r2)


# f=open('17.txt')
# a=[int(x) for x in f]
# mpos=0
# r1,r2=0,0
# for i in a:
#     if 10000<=i<=99999 and i%10==3:
#         mpos=max(i, mpos)
# print(mpos)
# for i in range(len(a)-2):
#     c1,c2,c3=0,0,0
#     if abs(a[i])%10==3:
#         c1=1
#     if abs(a[i+1])%10==3:
#         c2=1
#     if abs(a[i+2])%10==3:
#         c3=1
#     if c1+c2+c3 and a[i]+a[i+1]+a[i+2]<=mpos:
#       print(a[i],a[i+1],a[i+2])
#       r1+=1
#       r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# f=open('17.txt')
# a=[int(x) for x in f]
# mpos=[]
# r1,r2=0,0
# for i in a:
#     if i%2!=0:
#         mpos.append(i)
# ch=sum(mpos)//len(mpos)
#
# for i in range(len(a)-2):
#     c1, f=0, []
#     f.append(a[i]%3)
#     f.append(a[i+1] % 3)
#     f.append(a[i+2] % 3)
#     f.sort()
#     if a[i]<ch:
#         c1+=1
#     if a[i+1]<ch:
#         c1+=1
#     if a[i+2]<ch:
#         c1+=1
#     if f==[0,1,2] and c1==1:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# f=open('17.txt')
# a=[int(x) for x in f]
# r1,r2=0,-10**10
# mpos=10**10
# for i in a:
#     if abs(i)%100==25:
#         mpos=min(mpos, i)
# print(mpos)
# for i in range(len(a)-2):
#     flag=0
#     if 10<=a[i]<=99:
#         flag+=1
#     if 10<=a[i+1]<=99:
#         flag+=1
#     if 10<=a[i+2]<=99:
#         flag+=1
#     if flag==1 and a[i]+a[i+1]+a[i+2]<mpos:
#         r1+=1
#         r2=max(r2, a[i]+a[i+1]+a[i+2])
# print(r1,r2)

# from sys import setrecursionlimit
# setrecursionlimit(9999999)
# c=0
# def f(n):
#     if n>0:
#         g(n-1)
# def g(n):
#     global c
#     c+=1
#     if n>1:
#         c+=1
#         f(n-2)
# f(13)
# print(c)

# def dist(x1,y1,x2,y2):
#     return ((x1-x2)**2+(y1-y2)**2)**0.5
#
# def cent(a):
#     maxr=0
#     for i in range(len(a)):
#         for j in range(len(a)):
#             s=dist(a[i][0], a[i][1], a[j][0], a[j][1])
#             if s>maxr:
#                 r=[a[i],a[j]]
#                 maxr=s
#     return r
#
# f= open('matrix/web_files/27A_veb3_1.txt')
# a1,a2=[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[0]>2:
#         a1.append(s)
#     else:
#         a2.append(s)
#
# res1=cent(a1)
# res2=cent(a2)
#
# print((res1[0][0]+res1[1][0]+res2[0][0]+res2[1][0])/4*10000)
# print((res1[0][1]+res1[1][1]+res2[0][1]+res2[1][1])/4*10000)
# f.close()
#
# f= open('matrix/web_files/27B_veb3_1.txt')
# a1,a2,a3=[],[],[]
# for s in f:
#     s=s.replace(',', '.')
#     s=s.split()
#     s=[float(x) for x in s]
#     if s[1]<0:
#         a1.append(s)
#     else:
#         if s[0]>0:
#             a2.append(s)
#         else:
#             a3.append(s)
# res1=cent(a1)
# res2=cent(a2)
# res3=cent(a3)
# print(res1,res2,res3)
# print((res1[0][0]+res1[1][0]+res2[0][0]+res2[1][0]+res3[0][0]+res3[1][0])/6*10000)
# print((res1[0][1]+res1[1][1]+res2[0][1]+res2[1][1]+res3[0][1]+res3[1][1])/6*10000)

# from itertools import *
#
# def f(x):
#     b = 30<=x<=41
#     c = 50<=x<=56
#     a = a1<=x<=a2
#     return not((b or c)<=a)
#
# ox=[i/4 for i in range(30*4, (56+1)*4)]
# r=[]
# for a1,a2 in combinations(ox,2):
#     if any(f(x) for x in ox)!=True: #для выражения равного 0
#         r.append(a2-a1)
# print(min(r))

# f=open('Flash2025.csv')
# r=0
# n=[]
# def check_st(ar,num,st):
#     res=0
#     for i in ar:
#         if i[st]==num:
#             res+=1
#             if res>150:
#                 return True
#     return False
#
# for i in f:
#     n.append([int(x) for x in i.split(',')])
#
# for i in n:
#     if len(set(i))==6:
#         uni=0
#         for j in range(6):
#             if check_st(n,i[j], j):
#                 uni+=1
#             if uni==5:
#                 r+=1
#                 break
# print(r)

#dbscan
from math import dist
def cent(cl):
    minr=10**10
    for p in cl:
        s=sum([dist(p1,p) for p1 in cl]) # ищем dist при помощи встроенной функции
        if s<minr:
            res=p
            minr=s
    return res

f=open('files/27A_4_1.txt')
a=[[float(x) for x in s.replace(',', '.').split()] for s in f]

vsecl=[]
E=0.8 # дистанция между точками

while len(a)>0:
    tcl=[a[-1]]
    a.pop()
    for p in tcl:
        bliz_t=[t1 for t1 in a if dist(t1,p)<E] # ищем соседей
        for x in bliz_t:
            tcl.append(x) # добавляем в текущий
            a.remove(x) # удаляем из общего
    vsecl.append(tcl)

print('check:', len(vsecl[0])+len(vsecl[1]),len(vsecl)) # все ли точки вошли
r1=[]
r2=[]
for cl in vsecl: # удаляем аномалии при помощи проверки длины, аномалия - кластер из одной точки
    if len(cl)>1:
        r1.append(cent(cl)[0])
        r2.append(cent(cl)[1])
print(sum(r1)/len(r1)*10_000)
print(sum(r2)/len(r2)*10_000)
f.close()


print()

# аналогично
f=open('files/27B_4_1.txt')
a=[[float(x) for x in s.replace(',', '.').split()] for s in f]

vsecl=[]
E=0.7

while len(a)>0:
    tcl=[a[-1]]
    a.pop()
    for p in tcl:
        bliz_t=[t1 for t1 in a if dist(t1,p)<E]
        for x in bliz_t:
            tcl.append(x)
            a.remove(x)
    vsecl.append(tcl)

print('check:',len(vsecl[0])+len(vsecl[1])+len(vsecl[2]),len(vsecl))
r1=[]
r2=[]
for cl in vsecl:
    if len(cl)>1:
        r1.append(cent(cl)[0])
        r2.append(cent(cl)[1])
print(sum(r1)/len(r1)*10_000)
print(sum(r2)/len(r2)*10_000)
f.close()