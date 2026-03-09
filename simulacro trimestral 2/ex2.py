inp=input().split('-')
print(inp)
cs,ci,cinv=[],[],[]
for x in inp:
    num=0
    alfa=0
    inv=0
    inclen=0
    splited=[ch for ch in x]
    if len(splited)<8:
        inclen=1
    for y in splited:
        if y.isalpha()==True:
            alfa+=1
        elif y.isnumeric()==True:
            num+=1
        elif y.isalpha()==False and y.isnumeric()==False:
            inv=1
    if inv!=0:
        cinv.append(x)
    elif inclen==1:
        ci.append(x)
    elif num>0 and alfa==0:
        ci.append(x)
    elif alfa>0 and num==0:
        ci.append(x)
    elif inv==0 and num>0 and alfa>0 and inclen==0 and inv==0:
        cs.append(x)
maxlen=max(inp, key=len)
print(cs)
print(ci)
print(cinv)
print(maxlen)
