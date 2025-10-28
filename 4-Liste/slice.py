"""
Le slicing s'effectue sur le modèle : liste[m:n+1] 
        m   = le numéro d'index à partir duquel effectuer le tranchage
        n+1 = le numéro d'index jusqu'où effectuer le tranchage + 1 puisque
                !!! m est compris dans la tranche et n en est exlu !!!
        Liste = [1, 2, 3, 4, 5] --> éléments de la liste
                [0, 1, 2, 3, 4] --> numéros d'index associés à chaque élément
                pour trancher la liste des éléments 2 à 4 ...
                ... m = 1
                ... n = 4 -> 4 exclu
"""
liste = []
for i in range(1,11):                   # remplir la liste des nombres 1 à 10 (11 exclu)
    liste.append(i)

print('Liste complète ',liste)          # affiche toute la liste
print(liste[1])                         # affihce l'élément de l'index 1
print(liste[1:4])                       # l'élément de l'index 1 à 4 exclu
print(liste[0:])                        # l'élément de l'index 0 jusqu'à la fin = toute la liste
print(liste[:])                         # idem
print(liste[2:-5])                      # de l'index 2 jusqu'à l'index -5 exclu (donc affiche l'index -6)

# Afficher une tranche avec un pas
print('Afficher les nombres pairs entre 2 et 8 : ',liste[1:8:2])
print('Afficher tout : ',liste[::1])
print('Afficher tous les nombres impairs : ',liste[::2])
print('Afficher la liste en ordre inverse : ',liste[::-1])

# structure
# [start, stop, step]
# valeurs par défaut [début, fin, 1]
# [:] -> ni start, ni stop -> toute la liste
# [::2] -> toute la liste avec un pas de 2 -> pair ou impair
# [1::2] -> du 1er élément jusqu'à la fin avec un pas de 2

