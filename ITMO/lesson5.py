print("k", "t", "p")
for a in range(2):
    for b in range(2):
        for c in range(2):
            if((a and (not(c))) or b and (a==c))==1:
                print(a,b,c)