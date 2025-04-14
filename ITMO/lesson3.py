from itertools import *
alph=sorted("УРОК")
# a=list(product(alph, repeat=4))
# print(a.index(('И', 'Т', 'М', 'О'))+1)
ind=1
res=[''.join(el) for el in product(alph, repeat=4)]
for el in res:
    if "К" not in el and "ОО" not in el:
        print(ind)
        break
    ind+=1
#3.21
print(len([el for el in product('01', repeat=4) if el.count("1")==2]))

# def change_sys(num, base):
#     res=""
#     alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
#     alph= sorted(alph)
#     while num>0:
#         if num%base>9:
#             res = alph[int(num%base)-10] + res
#         else:
#             res=str(num%base)+res
#         num=num//base
#     return res
# counter=0
# for i in range(int("10000000", 6), int("100000000",6)):
#     if change_sys(i, 6)[0]!="2" or change_sys(i, 6)[0]!="3":
#         for j in range(len(change_sys(i,6))-2):
#             count_tmp=0
#             i_bin=bin(i)[2:]
#             if i_bin[j]!=i_bin[j+1] and i_bin[j]!=i_bin[j+2] and i_bin[j+1]!=i_bin[j+2]:
#                 count_tmp+=1
#             if count_tmp+2==len(change_sys(i,6)):
#                 counter+=1
# print(counter)

counter=0
for i in range(int("10000",9), int("100000",9)):
    checked=1
    for j in range(len(str(i))-1):
        tmp=str(i)
        if tmp[j]==tmp[j+1] or (int(tmp[j])+int(tmp[j+1]))%3!=0:
            checked=0
    if i%10!=9 and checked==1 and str(i).count("6")!=0 and str(i).count("9")==0:
        print(i)
        counter+=1
print(counter)
