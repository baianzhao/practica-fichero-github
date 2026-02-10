n=input()
n1,n2,n3=n.split()
mayor=0
if float(n1)>float(n2):
    mayor=n1
    if float(n1)>float(n3):
        mayor=n1
    elif float(n2)<float(n3):
        mayor=n3
elif float(n1)<float(n2):
    mayor=n2
    if float(n2)>float(n3):
        mayor=n2
    elif float(n2)<float(n3):
        mayor=n3
print(mayor)