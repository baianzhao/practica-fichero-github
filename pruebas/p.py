ni=int(input('introduce'))
nf=int(input('introduce'))
inc=int(input('itroduce'))
num=''
for a in range(ni, nf, inc):
    if a%4==0:
        num=num
    elif a%6==0:
        nca=f'*{a}*'
        num=str(num+f'{nca},')
        
    else:
        a=str(a)
        num=num+f'{a},'
        
print(num[:-1])