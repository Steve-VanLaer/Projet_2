# Trancher une chaîne de caractères
chaine = "Python"
sl     = slice(0,3)     # slicer de l'index 0 jusqu'à 2 exclu
print(chaine[sl])       # appliquer le tranchage

# Autre méthode
sl     = chaine[0:3]
print(sl)

# Appliquer un slice avec un pas 
mot = 'programmation'
sl  = slice(0,8,2)      # slicer de l'index 0 ('p') jusqu'à l'index 8 exclu ('a') avec un pas de deux (p,o,r,m)
print(mot[sl])

# Les chaînes de caractères peuvent s'utiliser comme une liste
print(chaine[0])

# Il est donc possible de trancher une chaîne de caractères tout comme une liste ...
# .. voir le fichier slice.py dans le sous-dossier 'Liste'