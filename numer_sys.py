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