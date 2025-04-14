#перевоз по 600
# with open('26.txt') as file:
#     n,s =[int(i) for i in file.readline().split()]
#     f= [int(i) for i in file.readlines()]
# f.sort(reverse=True)
# r=[[]]
# for i in range(0,n):
#     was=0
#     for j in range (0,len(r)):
#         if sum(r[j])+f[i]<=s:
#             r[j].append(f[i])
#             was=1
#             break
#     if was == 0:
#         r.append([f[i]])
# print(len(r), sum(r[-1]))
# print(r)
from doctest import master


#несколько коробок
# with open('26.txt') as file:
#     N=int(file.readline())
#     items=[]
#     boxes=[]
#     for line in file.readlines():
#         items.append(int(line.split()[0]))
#         boxes.append(int(line.split()[1]))
# items.sort(reverse=True)
# boxes.sort(reverse=True)
# k=0
# max_item=0
# for item in items:
#     for box in boxes:
#         if item<=box:
#             k+=1
#             max_item=max(max_item, item)
#             boxes.remove(box)
#             break
# print(k,max_item)

#мастера
# with open('26.txt')as file:
#     K=int(file.readline())
#     n=int(file.readline())
#     clients=[[int(i) for i in j.split()] for j in file.readlines()]
# masters=[0]*K
# clients.sort(key=lambda x:x[0])
# k=0
# last=0
# for client in clients:
#     for m in range(len((masters))):
#         if masters[m]<=client[0]:
#             masters[m]=client[1]
#             k+=1
#             last=m+1
#             break
# print(k,last)

# with open('26.txt')as file:
#     N=int(file.readline())
#     K=int(file.readline())
#     details=[int(file.readline()) for i in range(N)]
#     containers = [int(file.readline()) for i in range(K)]
# passed=[]
# for det in details:
#     for i in range(len(containers)):
#         if containers[i]>=det:
#             containers[i]-=det
#             passed.append(det)
#             break
# print(sum(passed), len(passed))


# with open('26.txt') as file:
#     N=int(file.readline())
#     items=[int(i) for i in file.readlines()]
# items.sort()
# planned=[]
# real=[]
# ptr=0
# rptr=-1
# items.sort()
# while len(items)-(ptr+abs(rptr))>=5:
#     planned.append(items[ptr]+items[ptr+1]+items[ptr+2]+items[ptr+3])
#     ptr+=4
#     rptr-=1
# print(sum(planned)+sum(items[ptr:rptr+1]))
# items.sort(reverse=True)
# ptr=0
# while len(items)-ptr>=5:
#     real.append(items[ptr]+items[ptr+1]+items[ptr+2]+items[ptr+3])
#     ptr+=5
# print(sum(real)+sum(items[ptr:]))

#не работает
# file=open('26.txt', 'r')
# N=int(file.readline())
# details=[]
# ind=1
# for i in file.readlines():
#     details.append(['s', int(i.split()[0]), ind])
#     details.append(['o', int(i.split()[1]), ind])
# line=[0]*N
# counter=0
# last=0
# for detail in details:
#     if detail[2] in line:
#         continue
#     if detail[0]=='s':
#         counter=line.index(0)
#         line[line.index(0)]=detail[2]
#     else:
#         for j in range(len(line-1),0,-1):
#             if line[j]==0:
#                 counter=j
#                 line[j]=detail[2]
#                 break
#     last=detail[2]
# print(last, counter)

# file=open('17.txt')
# def dist(x1,y1,x2,y2):
#   return ((x1-x2)**2+(y1-y2)**2)**0.5
# clusters=[[],[],[]]
# for point in file.readlines():
#     x,y=[float(i) for i in point.split()]
#     if 1600<=y<=4400 and x<=2400:
#         clusters[0].append([x,y])
#     if 3600 <= y <= 5600 and x >= 6400:
#         clusters[1].append([x, y])
#     if 1600 <= y <= 4400 and x <= 2400:
#         clusters[1].append([x, y])
#     if 5200<=y<=8000 and 3000<=x<=5400 and y< 3/4*x+5150 and y>(-1)*2/3*x+7600:
#         clusters[2].append([x,y])
# def deltaavg(cluster):
#     summ,k,max_val=0,0,0
#     for p0 in range(len(cluster)-1):
#         for p1 in range(p0+1, len(cluster)):
#             tmp=dist(*cluster[p0], *cluster[p1])
#             summ+=tmp
#             k+=1
#             print(k)
#             if max_val<tmp:
#                 max_val=tmp
#     return [summ/k, max_val]
#
# Davg=[deltaavg(cl) for cl in clusters]
# P=[el[0]/el[1] for el in Davg]
# print(int(min(P)*10_000))
# print(int(sum(P)/ len(P) *10_000))
#13b

f = open('../../17.txt')
n=int(f.readline())
bags=[]
for i in f.readlines():
    tmp=[int(j) for j in i.split()]
    tmp[1]= tmp[1]//36 if tmp[1]%36==0 else tmp[1]//36+1
    bags.append(tmp)
s=0
for i in range(n):
    s+=abs(bags[0][0]-bags[i][0])*bags[i][1]
minsum=s
left=bags[0][1]
right=sum(el[1] for el in bags[1:])
for i in range(1,n):
    diff= bags[i][0]-bags[i-1][0]
    s=s+diff*(left-right)
    left+=bags[i][1]
    right-=bags[i][1]
    if minsum>s:
        print(i)
        minsum=min(minsum,s)