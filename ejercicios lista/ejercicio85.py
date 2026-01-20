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

print(mc,mac,mi)
#mediana
mec,meca,mei=0,0,0

lc=len(c)
lca=len(ca)
li=len(i)

i.sort()
ca.sort()
c.sort()


print(i, ca, c)
    



