st=int(input())
h=st//60
horas=h//60
m=(horas*60)
min=m//60
s=(st-horas*60*60-min*60)/60
print(horas,min,s)
