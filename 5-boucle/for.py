# Les boucles servent à itérer des objets, elles s'utilisent donc exclusivement avec des objets itérables (liste ou chaîne de caractères)

# for()
for i in range(0,10):   # 'for'     : début de la boucle -> à noter la deux points (:) à la fin de la ligne
    a = i               # 'i        : variable d'itération
                        # 'in'      : pour indiquer de quoi les objets doivent-ils être itérés
                        # 'range'   : à partir de quel index et jusqu'à quel index il faut itérer
                        # 'a = 10'  : une boucle suppose une instruction, ici 'a = i' -> respecer l'indentation
# La fonction range()
for i in range(10):     # par défaut l'itération commence par '0'
    i = i + 1           
for i in range(1,10):   # (index de début, index de fin -1 = index 10 exclu)
    i = i - 1           
for i in range(1,10,2): # avec un pas de deux
    i = i + 1 

# La boucle for() peut tourner sur les index ou les éléments d'une liste ou d'une chaîne de caratères
liste = list(range(10))     # il est préférable de travailler sur les éléments
for i in liste:
    print(i)
for i in range(1,10):
    print(i)

# Il est possible de remplacer la fonction range() par enumerate()
mot = 'python'
for i in enumerate(mot):    # l'itération se fait directement à partir d'un objet itérable
    print(i)