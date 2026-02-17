i=input()
a1,b1,a2,b2=i.split()

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
    print('[]')
else:
    print(f'[{x},{y}]')
