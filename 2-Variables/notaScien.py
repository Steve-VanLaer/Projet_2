# Utiliser la notation  scientifique pour initialiser un grand nombre
milliard = 10e12
print('milliard',milliard)          # les nombres qui ont la forme scientifique sont affichées en type float

# Afficher le nombre 63 253 754 en notation scientifique
nbre = 6.3253754e6                    # voir le fichier Nota_Scient.pdf pour comprendre le principe de la notation scientifique
print('63 253 754',nbre)

# Même chose avec un petit nombre
petit = 1.23e-4        
print(petit)   

# Afficher nombre négatif en notation scientifique
nbre = -4.3e5
print(nbre)

# Par facilité, Python autorise d'écrire les grand nombre sous cette forme
milliard = 1_000_000_000
print(milliard)
