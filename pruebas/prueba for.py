password='ale4jk'
total=0
vocales='aeiouAEIOU'
totv=0

for i in password:
    if i.isnumeric():
        total=total + int(i)
    if i in vocales:
        totv=totv+1

print(total)
print(totv)
   

