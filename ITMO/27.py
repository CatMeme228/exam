# 7 остаток суммы пар на расстоянии
# f = open('files/727b.txt')
# N = int(f.readline())
# ost = [0]*11
# nums = [int(f.readline())for i in range(17)]
# k = 0
# for i in range(17, N):
#     tmp = int(f.readline())
#     ost[nums[i-17] % 11] += 1
#     k += ost[(11-tmp % 11) % 11]
#     nums.append(tmp)
# print(k)

# 17 лаборатория перевозка
# f = open('files/1727b.txt')
# N = int(f.readline())
# bags = []
# for i in f.readlines():
#     tmp = [int(j) for j in i.split()]
#     tmp[1] = tmp[1]//36 if tmp[1] % 36 == 0 else tmp[1]//36+1
#     bags.append(tmp)

# s = 0
# for i in range(N):
#     s += abs(bags[0][0]-bags[i][0])*bags[i][1]

# minsum = s
# a=[]
# left = bags[0][1]
# right = sum(el[1] for el in bags[1:])
# for i in range(1,N):
#     diff = bags[i][0]-bags[i-1][0]
#     s = s + diff * (left - right)
#     left += bags[i][1]
#     right -= bags[i][1]
#     if minsum > s:
#         a.append(s)
# print(min(a))

#демо dbscan
file = open('files/17demob.txt')
content = [[float(i) for i in el.replace(',', '.').split()] for el in file.readlines()]
def dist(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def dbscan(p0):
    cluster = [p for p in content if dist(*p0,*p)<1]
    if len(cluster)>0:
        for p in cluster: content.remove(p)
        next_cluster=[dbscan(p) for p in cluster]
        for p in next_cluster:
            cluster.extend(p)
    return cluster

clusters=[]
while len(content)>0:
    p0=content.pop()
    clusters.append([p0]+dbscan(p0))

import turtle
t=turtle.Pen()
t.up()
turtle.tracer(100)
color=['red', 'darkgreen', 'darkblue']
col=-1
for cl in clusters:
    col+=1
    for x,y in cl:
        t.goto(x*20, y*20)
        t.dot(5, color[col])

turtle.done()

def centr(cluster):
    res=[]
    for p in cluster:
        summ = sum(dist(*p,*p0) for p0 in cluster)
        res.append([summ, *p])
    return min(res)

Centr= [centr(cluster) for cluster in clusters]
px=sum(x for summ, x,y in Centr)
py=sum(y for summ, x,y in Centr)
print(px/len(clusters)*10_000, py/len(clusters)*10_000)
