from turtle import *
setworldcoordinates(-80,-80,50,50)
tracer(0)
left(90)
for i in range(9):
    forward(22)
    right(90)
    forward(6)
    right(90)
penup()
forward(1)
right(90)
forward(5)
left(90)
pendown()
for i in range(9):
    forward(53)
    right(90)
    forward(75)
    right(90)
penup()
for x in range(-80,50):
    for y in range(-80,50):
        setpos(x,y)
        dot(3, 'red')
done()