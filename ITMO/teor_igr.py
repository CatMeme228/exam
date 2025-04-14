#12.6
#def f(s,p):
#     if s>=50:
#         return p%2==0
#     if p==0:
#         return False
#     act=[f(s+5, p-1), f(s*3, p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19a',[s for s in range(1, 50) if f(s,1)])
# print('19b',[s for s in range(1, 50) if f(s,2)])
# print('20',[s for s in range(1, 50) if f(s,3) and not f(s,1)])
# print('21',[s for s in range(1, 50) if f(s,4) and not f(s,2)])

#12.7
# def f(s,p):
#     if 20<=s<=30: return p%2==0
#     elif s>30: return not(p%2==0)
#     if p==0:
#         return False
#     act=[f(s+1, p-1), f(s*2, p-1)]
#     return any(act) if (p-1)%2==0 else all(act)
# print('19a', [s for s in range(1,20) if f(s,1)])
# print('19b', [s for s in range(1,20) if f(s,2)])
# print('20',[s for s in range(1, 20) if f(s,3) and not f(s,1)])
# print('21',[s for s in range(1, 20) if f(s,4) and not f(s,2)])
#12.11
def f(a,b,p):
    if a==b: return p%2==0
    if p==0:
        return False
    if a<b:
        act=[f(a+1, b, p-1), f(a+3, b, p-1)]
    elif a>b:
        act = [f(a, b+1, p - 1), f(a, b+3, p - 1)]
    return any(act) if (p-1)%2==0 else any(act)
print('19a', [s for s in range(1,32) if f(17,s,2)])
print('20', [s for s in range(1,32) if f(17,s,3) and not f(14,s,1)])
print('21', [s for s in range(1,32) if f(17,s,4) and not f(14,s,2)]) #надо менять all на any all-any
