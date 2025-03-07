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

with open('text.txt') as f:
    a=f.readline()
k,m=1,0
a = a.replace('CA', '*')
a = a.replace('CO', '*')
a = a.replace('DA', '*')
a = a.replace('DO', '*')
a = a.replace('FA', '*')
a = a.replace('FO', '*')
for i in range(len(a)-1):
    if a[i]==a[i+1]=='*':
        k+=1
    else:
        m=max(m,k)
        k=1
print(m)
