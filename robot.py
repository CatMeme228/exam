#23 type
ways=[]
def f(s,p,way):
    global ways
    if s==13: return ways.append(way)
    if p==0: return False
    f(s-2,p-1,way+'1')
    f(s*3, p - 1, way + '2')

f(11,5,'')
print(ways)

#13.30
def f(s,e):
    if s==e: return 1
    if s>e: return 0
    return f(s+1,e)+f(s+2,e)+f(s+4,e)
print(f(21,30))

#13.33
#4->11->17->20
def f(s,e):
    if s==e: return 1
    if s>e: return 0
    return f(s+1,e)+f(s+3,e)+f(s*2,e)
print(f(4,11)*f(11,17)*f(17,20))

def f(s,e):
    if s==e: return 1
    if s>e: return 0
    if s==25: return 0
    return f(s+1,e)+f(s*2,e)
print(f(14,29)*f(2,14))


#13.15
#происходит сортировка

from turtle import *
setworldcoordinates(-7,-7,7,7)
tracer(0)
left(90)
penup()
forward(5)
pendown()
for i in range(4):
    right(120)
    forward(5)
penup()
for x in range(-7,7):
    for y in range(-7,7):
        goto(x,y)
        dot(5,'red')
done()
