t=input()
h,m,s=t.split()
h,m,s=int(h),int(m),int(s)
if s==59:
    s=0
    if m==59:
        m=0
        h+=1
        m=0
        s=0
        if h==24:
            m=0
            h=0
            s=0
    else:
        m+=1
else:
    s+=1
h,m,s=str(h),str(m),str(s)
if len(h)==1:
    horas=str(0)+str(h)
else:
    horas=h
if len(m)==1:
    min=str(0)+str(m)
else:
    min=m
if len(s)==1:
    seg=str(0)+str(s)
else:
    seg=s
print(f'{horas}:{min}:{seg}')