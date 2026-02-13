y=input()
yy=[ch for ch in y]
e=0
y=int(y)

if y % 4==0:
    e=e
else:
    e+=1

if y>=9999 or y<=1800:
    e+=1

if int(yy[2])==0 and int(yy[3])==0:
    if float(yy[0]+yy[1]) % 4==0:
        e+=0
    else:
        e+=1
if e==0:
    print('YES')
else:
    print('NO')

