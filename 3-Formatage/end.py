# Ecrire une phrase dans deux fonctions print() à l'aide du mot-clé 'end'
prenom = input('Introduisez votre prénom : ')
print("Bonjour",prenom,end='')
print(". Comment vas-tu ?")

# Challenge : afficher une suite de nombres séparés par une virgule (,) sur une ligne
for i in range(0,6):    # de 0 à 6 exclu
    print(i)            # sans formatage, Python affiche chaque nombre ligne par ligne
for i in range(0,6):
    print(i,end=', ')     # afficher sur une ligne et séparer les nombre affichés par une virgule