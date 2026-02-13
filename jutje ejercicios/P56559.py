i=input()
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
print(pr)

