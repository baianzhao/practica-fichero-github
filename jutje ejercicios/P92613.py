x=float(input())
import math
floor=math.trunc(x)
cell=math.ceil(x)
r=round(x)
if x==r:
    r=r
elif (x-r)==0.5:
    r+=1


print(floor,cell,r)
