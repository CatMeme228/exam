file=open("91.csv","r")
#content=file.read() #весь файл одной строкой
#content=file.readlines() #весь файл массивом

#8.24
# content= [[int(el) for el in line.rstrip().split(';')] for line in file.readlines()]
# c=0
# for line in content:
#     if len(set(line))==len(line) and min(line)%2==0:
#         c+=1
# print(c)
# file.close()

#8.25
# def check(line):
#     duplicate=0
#     for el in line:
#         if line.count(el)==2:
#             duplicate=el
#             break
#     return sum([el for el in line if el!=duplicate])/len([el for el in line if el !=duplicate])<=duplicate*2
#
# content= [[int(el) for el in line.rstrip().split(';')] for line in file.readlines()]
# c=0
# for line in content:
#     if len(set(line))==5 and check(line):
#         c+=1
# print(c)