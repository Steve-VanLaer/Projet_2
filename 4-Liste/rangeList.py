# Introduire une suite d'entiers dans une liste allant de 0 à 10
liste = list(range(11))                     
print('Liste d\'entiers de 0 à 10 : ',liste)

liste2 = liste          # voir plus bas (ligne 13)
liste3 = list(liste)    # voir plus bas (ligne 13)
print('Liste 2 : ',liste2)

# Ajouter une liste à une liste
liste+=list(range(11,16))
print('Liste de 0 à 15 : ',liste)

# la liste 2 étant une copie de la liste 1 (liste), ses éléments changent au fur et à mesure des modifications de la liste 1
print('Liste 2 après modifications de la liste 1 : ',liste2)
print('Liste 3 après modifications de la liste 1 : ',liste3)    # voir ligne 6 pourquoi les éléments de la liste 3 ne changent pas
                                                                # !!! cette astuce ne fonctionne qu'avec les liste à 1 dimension

pair = liste[0::2]                              # initialiser une liste de nombres pairs à patir d'une première
print('Nombres pairs de la liste de 0 à 20 ',pair+list(range(16,21,2)))     # lui ajouter des nombres pairs jusqu'à 20

# Afficher une liste de 0 à 1000 avec un pas de 200
print(list(range(0,1000,200)))

# Cette instruction renvoie à une liste vide
print(list(range(10,0)))    # la séquence part de 10 et n'arrivera jamais à 0

# Afficher une liste d'entiers par ordre décroissant
print(list(range(10,0,-1)))

