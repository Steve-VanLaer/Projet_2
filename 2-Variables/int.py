# Afficher une variable int
x = 10      # le fait de taper un caractère ou une chaîne de caractères suivis du signe = suffit pour que Python interprète ...
print(x)    # ... qu'une variable est déclarée.
            # Mais sans affecter de valeur ('texte' ou nombre) à cette variable Python renvoie un message d'erreur (not defined).
            # Le fait d'affecter une valeur à cette variable après le signe = suffit pour que Python interprète le type de la ..
            # ... variable.

# Incrémenter une variable int
x+=1        # utiliser uniquement le signe égal aurait pour effet d'écraser la variable initiale

# Déclarer et initialiser plusieurs variables à la fois
a, b, c = 1, 2, 3
print(a,b,c,sep=" ")
