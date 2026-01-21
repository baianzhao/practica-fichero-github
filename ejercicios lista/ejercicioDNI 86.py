resto=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
l='T,R,W,A,G,M,Y,F,P,D,X,B,N,J,Z,S,Q,V,H,L,C,K,E'
letras=l.split(',')
s='s'
while s=='s':
    dni=input('introduce tu DNI')
    DNI=[ch for ch in dni]
    lf=DNI[-1]
    break
print(letras)
print(DNI)
print(lf)