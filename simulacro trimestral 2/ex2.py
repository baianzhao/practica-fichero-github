a,b,c=input().split('-')
cs=[]
ci=[]
cinv=[]
ea,ea2,na,la=0,0,0,0
eb=0
ec=0

for x in a:
    if x.isnumeric()==False and x.isalpha()==False:
        ea+=1
for y in a:
    if x.isnumeric()==True:
        na+=1
for z in a:
    if x.isalpha()==True:
        la+=1

if len(a)<8:
    ea2+=1
if ea==0 and ea2==0 and na>0 and la>0:
    cs.append(a)
elif ea2>0:
    ci.append(a)
elif na<=0 or la<=0:
    ci.append(a)
elif ea>0:
    cinv.append(a)
    
print(cs,ci,cinv)
