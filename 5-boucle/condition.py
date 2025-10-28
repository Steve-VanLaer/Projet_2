# Faire suivre une condition à la suite de la première si celle-ci n'est pas remplie
age = 55
if age > 67:
    print('pensionné')  # Python renvoie l'une des trois conditions
elif age > 18:
    print('majeur')
else:
    print('mineur')     # s'utilise sans condition, forcément = à la dernière condition possible

# Vérifier si une mot commence par 'A'
mot = 'Anglais'
if mot[0,1] == 'A':
    print(mot,'commence par A')
sl = slice(0,1)
if mot[sl] == 'A':
    print(mot,'commence par A')

   
