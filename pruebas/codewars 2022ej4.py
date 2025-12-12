totalgames=int(input('introduce el numero de partidos en total'))
e1=input('introduce datos equipo 1')
e2=input('introduce datos equipo 2')
e1n, e1w, e1l=e1.split()


e2n, e2w, e2l=e2.split()
e1w=int(e1w)
e2l=int(e2l)
magic=totalgames-e1w-e2l+1
print(f'chicago won {magic} matches')
