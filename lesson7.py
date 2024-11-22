#7.13
# from itertools import *
# def f(x,y,z):
#     return (x and z or not y) and (y and not z or z)
#
# table=[
#     [0,1,0],
#     [0,1,1],
#     [1,1,1]
# ]
#
# for p in permutations('xyz'):
#     if [f(**dict(zip(p,row))) for row in table]==[1,1,1]:
#         print(p)

#7.15
#
# from itertools import *
# def f(x,y,z,w):
#     return not w or y or (not z and x)
#
# table=[
#     [1,0,0,0],
#     [1,0,0,1],
#     [1,0,1,1],
# ]
#
# for p in permutations('xyzw'):
#     if [f(**dict(zip(p,row))) for row in table]== [0,0,0]:
#         print(p)

#7.20

# from itertools import *
# def f(x,y,z,w):
#     return not (y<=(x==w))and (z<=x)
#
# for val in product([0,1], repeat=5):
#     table=[
#         (val[0],1,1,val[1]),
#         (0,val[2],val[3],0),
#         (val[4],0,1,0),
#     ]
#     if len(table)== len(set(table)):
#         for p in permutations('xyzw'):
#             if [f(**dict(zip(p,row))) for row in table]== [1,1,1]:
#                 print(p)

#7.22
from itertools import *
def f(x,y,z,w):
    return ((w<=y)<=x)or not z

for val in product([0,1], repeat=7):
    table=[
        (val[0],val[1],1,val[2]),
        (val[3],0,val[4],val[5]),
        (val[6],1,0,0),
    ]
    if len(table)== len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,row))) for row in table]== [0,0,0]:
                print(p)
