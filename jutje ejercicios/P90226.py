n=input()
nn=n.split()
n1,n2=n.split()
nn.sort()
if n1==n2:
    print(n1,'=',n2)
elif n1==nn[0] and n2==nn[1]:
    print(n1,'<',n2)
elif n2==nn[0] and n1==nn[1]:
    print(n1,'>',n2)
