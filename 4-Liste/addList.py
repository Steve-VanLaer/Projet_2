# Une liste est modifiable, on dit qu'elle est mutable

# Ajouter un élément à une liste
liste = [1,2,3]
liste.append(5)     # l'élément ajouté prend automatiquement la dernière place
print(liste)

# Ajouter un élément 
liste.insert(0,0)    # (élément à ajouter,index où placer l'élément)
                     # ici l'élément '0' à l'index 0, c'est-à-dire en début de liste
print(liste)

# Ajouter plusieurs éléments à une liste
liste += [4, 5, 6, 7]
print(liste)

# Remplacer un élément d'une liste
liste = [1,2,3]
liste[1] = 0       # remplacer 'élément à l'index 1 (donc 2) par 0
                   # principe de l'écrasement
print(liste)

# Remplacer tous les éléments d'une liste
liste = [0,1,2]     # les données initiales ont été écrasées
print(liste)

# Supprimer un élément d'une liste avec sa valeur
liste.remove(2)     # introduire l'ément à supprimer
print(liste)
# Autre méthode, avec l'index
del liste[3]         # supprimer le 3è élément

# Trouver l'index d'une valeur
list.index(0)

# Trouver le nombre d'occurences d'une valeur
liste.count(2)

