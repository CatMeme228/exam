with open('16.txt') as f:
    n,m=map(int, (f.readline().rstrip()).split(' '))
    a=[int(x) for x in f]
a.sort(reverse=True)
c=0
while sum(a)>=m:
    cable= a.pop(0)
    while cable+a[0]<m:
        cable+=a[0]
        a.pop(0)
        c+=1
    piece = [i for i in a if cable+i>=m][-1]
    if cable+piece>m:
        a.append(cable+piece-m)
    c+=1
    a.remove(piece)
    a.sort(reverse=True)
print(c, len(a))
