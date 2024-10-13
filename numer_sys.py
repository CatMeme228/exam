def change_sys(num, base):
    res=""
    alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
    alph= sorted(alph)
    while num>0:
        if num%base>9:
            res = alph[int(num%base)-10] + res
        else:
            res=str(num%base)+res
        num=num//base
    return res

def digit_sum(n):
    res=0
    n=str(n)
    for i in range(len(n)):
        res=res+int(n[i])
    return res

'''
a=int("111", 16)
b=bin(a)
f= change_sys(a,4)
o=oct(a)
h=hex(a)
print("bin:",b[2:])
print("four:", f)
print("oct:",o[2:])
print("ten:",a)
print("hex:",h[2:])'''

'''num=9999
while True:
    first=num//1000
    second=(num//100)%10
    third=(num//10)%10
    fourth=num%10
    tmp=[]
    s1=first+second
    s2=second+third
    s3=third+fourth
    tmp=[s1,s2,s3]
    tmp.sort()
    print(tmp)
    if tmp[0]==15 and tmp[1]==17:
        print(num)
        break
    num=num-1'''

'''n=1
while True:
    t=change_sys(n, 2)
    t=int(str(t)+str(digit_sum(t)))
    t=int(str(t)+str(digit_sum(t)))
    if int(str(t),2)>239:
        print(n)
        break
    n+=1'''

'''res=[]
for i in range (12):
    t=bin(i)[2:]
    if i%2==0:
        t="10"+t
    else:
        t="1"+t+"01"
    res.append(int(t,2))
print(max(res))'''
res=set()
for i in range(1,1000000):
    i_tmp=str(i)
    i_sum=digit_sum(i)
    for j in range(len(i_tmp)):
        if i_tmp[j]!="0":
            sum_dev_num=str(i_sum%int(i_tmp[j]))
            if int(i_tmp+ sum_dev_num)>99999 and int(i_tmp+ sum_dev_num)<1000000:
                res.add(i_tmp+ sum_dev_num)
                print(i_tmp+ sum_dev_num)

print(len(res))
