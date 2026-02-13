i=input()
p=0
a1,b1,a2,b2=i.split()
pr=''
if a1==a2 and b1==b2:
    pr='='
elif (a2<a1 and b1<=b2) or (a2<=a1 and b1<b2):
    pr='1'
elif (a1<a2 and b2<=b1) or (a1<=a2 and b2<b1) :
    pr='2'
else:
    pr='?'
    p=1
if p==1:
    pr='?'



if a1>a2:
    x=a1

elif a2>a1:
    x=a2
else:
    x=a1
 

if b1>b2:
    y=b2
   
elif b2>b1:
    y=b1

else:
    y=b2

if int(a2)>int(b1) or int(x)>int(y):
    inter='[]'
else:
    inter=f'[{x},{y}]'

print(f'{pr} , {inter}')