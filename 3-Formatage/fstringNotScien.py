# Syntaxe des grands nombres
grand_nombre = 10_000_000_000   # pour faciliter la lecture des grands nombres, Python autorise l'emploi du _

# Afficher l'écriture scientifique d'un grand nombre (123 000)
print(1.23e5)       # Python affiche par défaut une décimale

# Afficher l'écriture scientifique d'un petit nombre (0.00043)
print(4.3e-4)

# Afficher une écriture scientifique dans un f-string
print(f"{1.23e5}")
print(f"{grand_nombre:e}")

# Afficher un nombre désiré de décimales à l'écriture scientifique
print(f"{1.23e5:.3f}")