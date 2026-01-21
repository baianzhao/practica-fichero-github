#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos

na=0
i,c,ca=[],[],[]
s='si'
while s=='si':
    v=input('introduce el nombre del estudiante')
    na+=1
    v2=int(input('introduce nota de castellano'))
    c.append(v2)
    v3=int(input('introduce nota de catalan'))
    ca.append(v3)
    v4=int(input('introduce nota de ingles'))
    i.append(v4)
    s=input('quiere introducir nota de otro alumno? si/no')
#media
mc,mac,mi=0,0,0

for x in c:
    mc+=x
mc=mc/na

for y in ca:
    mac+=y
mac=mac/na

for z in i:
    mi+=z
mi=mi/na

mc=round(mc, 2)
mi=round(mi,2)
mac=round(mac,2)

#mediana
mec,meca,mei=0,0,0

l=len(c)

i.sort()
ca.sort()
c.sort()

#mediana par
if l%2==0:
    ll=(l/2)-1
    ll=int(ll)
    mec=int(c[ll]+c[ll+1])/2
    meca=int(ca[ll]+ca[ll+1])/2
    mei=int(i[ll]+i[ll+1])/2
#mediana impar
else:
    
    ll=(l/2)-0.5
    ll=int(ll)
    mec=int(c[ll])
    meca=int(ca[ll])
    mei=int(i[ll])

print(c,ca,i)

print(f'la media de castellano es de {mc}')
print(f'la media de catalan es de {mac}')
print(f'la media de ingles es de {mi}')
print(f'la mediana de castellano es de {mec}')
print(f'la mediana de catalan es de {meca}')
print(f'la mediana de ingles es de {mei}')
    

    



