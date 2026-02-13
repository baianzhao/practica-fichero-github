d=input()
e,ct=d.split()
l=[]
res=[e]
re,rc=0,0
b,c=[500,200,100,50,20,10,5,2,1],[1,2,5,10,20,50]
e=int(e)
ct=int(ct)
for x in b:
    for y in range(9):
        y=int(y)
        
        r=res[y-1]//x
        rr=rr[y]%x
        l.append(r)
        res.append(rr)

        
print('Banknotes of 500 euros:',l[0])
print('Banknotes of 200 euros:',l[1])
print('Banknotes of 100 euros:',l[2])
print('Banknotes of 50 euros:',l[3])
print('Banknotes of 20 euros:',l[4])
print('Banknotes of 10 euros:',l[5])
print('Banknotes of 5 euros:',l[6])
print('Coins of 2 euros:',l[7])
print('Coins of 1 euros:',l[8])






