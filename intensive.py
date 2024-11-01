
#№25
#a= int(input())
# res=0
# for i in range(1,a+1):
#     if a%i==0:
#         res+=1
#         print(i)
# print('count:', res)

#task 14
# def change_sys(num, base):
#     res=''
#     while num>0:
#         res=str(num%base)+res
#         num=num//base
#     return(res)
#
# a=change_sys((17**23-12**14)*2+37**16, 3)
# print(str(a).count('2'))

#task25
#нужен перебор от 1 до корня числа, делители парные
#36: 1-36, 2-18, 2-13...
# for i in range(1000000, 1100000):
#     res=0
#     for j in range(1, int(i**0.5)):
#         if i%j==0:
#             res+=2
#         if res>3:
#             break
#     if res<=3:
#         print(i)


#Пусть д-0, и-1, к-2, м-3, о-4. Тогда кодим - 24013
#print(int('24013', 5)+1)
#1759
#или
# from itertools import product, repeat
# a= 'дикмо'
# z=list(product(a, repeat=5))
# print(z.index(('к', 'о', 'д', 'и', 'м'))+1)


#task5 (hw)
# n=1
# r=0
# while r<=999:
#     if n%2==0:
#         z=n**3
#         if z%3==0:
#             r=int('1'+str(z))//45
#         else:
#             r=int('2'+str(z))//43
#     n+=1
# print(r)
#4898


# a='AaBbCcAa'
# #replace
# z=a.replace('Aa', '1', 1)
# #split (возвращает массив)
# k=a.split('Aa')
# print(z,k)


#25
#водится строка из rus, найти r кроме ru
# s= input()
# k= s.count("R")-s.count("RU")
# print(k)
# #или
# s=s.replace("RU", '1')
# k=s.count("R")
# print(k)

#25
#кот макс к подряд
# s=input()
# s=s.replace('Т', 'О')
# z= s.split("О")
# print(z)
# a=[]
# for i in z:
#     a.append(len(i))
# print(max(a))

#insert(эл-мент, индекс)- остальные смещаются
#remove - удаление по значению, если значения нет в списке- ошибка
#pop([i]) - удаление по индексу

#сделать квадрат
#a=list(map(int, input().split()))
# b=[]
# for i in a:
#     b.append(i**2)
# print(*b)

#удалить 20
a=[1,3,20,5,6,20,12,20,6]
while (20 in a):
    a.remove(20)
print(a)
