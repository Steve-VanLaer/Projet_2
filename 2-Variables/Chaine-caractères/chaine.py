# Trouver le nombre de caractères d'un texte
texte = input("Entrez une chaîne de caractères : ")
longueur = len(texte)
print("Le nombre de caractères introduits est de ",str(longueur))

# Compter le nombre d'occurance d'un mot dans une phrase
phrase  = "bonjour tout le monde, bonjour à tous"
occ     = phrase.count("bonjour")
print(f"Le mot 'bonjour' apparaît {occ} fois.")

# Mettre une chaîne de caractères en majuscules
texte = 'Python'
print(texte.upper())

# Mettre une chaîne de caractères en minuscules
print(texte.lowe())

# Remplacser le caractère d'un mot par un autre
texte = 'Python'
print(texte.replace("P","p"))   # (le caractère à remplacer, le caractère qui remplace)

# Remplacer plusieurs fois le même caractère (s'il y en a) par un autre
mot = "ananas"
print(mot.replace("a","b"))

# Remplacer un caractère par un autre un certain nombre de fois
mot = "ceoceb"
print(mot.replace("ce","ba",2))

# Spliter une chaîne de caractères
texte = 'Bonjour à tous'
print(texte.split())        # par défaut split() découpe en fonction des espaces
                            # le résultat obtenu est une LISTE (voir Projet_2/Liste)

# Spliter à l'aide d'un séprateur
date = "20.10.25"
print(date.split("."))      # le split s'effectue en fonction des point (".")

# Enlever les espaces au début et à la fin d'une chaîne de caractères
texte = " Python "
print(texte.strip())