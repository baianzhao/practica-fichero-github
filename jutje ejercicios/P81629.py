i=input()
e,c=i.split()
e,c=int(e),int(c)
euros=[500,200,100,50,20,10,5,2,1]
l=[]
cc=[]
ct=[50,20,10,5,2,1]
tot=e
for x in euros:
    n= tot//x
    l.append(n)
    tot=tot%x
totc=c
for y in ct:
    nc= totc//y
    cc.append(nc)
    totc=totc%y

print('Banknotes of 500 euros:',l[0])
print('Banknotes of 200 euros:',l[1])
print('Banknotes of 100 euros:',l[2])
print('Banknotes of 50 euros:',l[3])
print('Banknotes of 20 euros:',l[4])
print('Banknotes of 10 euros:',l[5])
print('Banknotes of 5 euros:',l[6])
print('Coins of 2 euros:',l[7])
print('Coins of 1 euros:',l[8])
print('Coins of 50 cents:',cc[0])
print('Coins of 20 cents:',cc[1])
print('Coins of 10 cents:',cc[2])
print('Coins of 5 cents:',cc[3])
print('Coins of 2 cents:',cc[4])
print('Coins of 1 cent:',cc[5])
