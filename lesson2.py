def change_sys(num, base):
    res=""
    alph = "qwertyuiopasdfghjklzxcvbnm"
    list(alph).sort
    alph= "0123456789"+alph
    while num>0:
        res = alph[int(num%base)] + res
        num=num//base
    return res
print(change_sys(5,25))
