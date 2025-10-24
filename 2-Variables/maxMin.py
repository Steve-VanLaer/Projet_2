# trouver le plus grand et le plus petit de deux nombres
n1 = int(input('Introduisez un nombre :'))
n2 = int(input('Introduisez encore un nombre : '))
grand = max(n1,n2)
petit = min(n1,n2)
print('Le plus grand des deux nombres introduits (',n1,'et',n2,') est',grand,end='')
print(' et le plus petit',petit)