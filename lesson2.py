def change_sys(num, base):
    res=""
    alph = "0123456789qwertyuiopasdfghjklzxcvbnm"
    alph=sorted(alph)
    while num>0:
        res = alph[int(num%base)] + res
        num=num//base