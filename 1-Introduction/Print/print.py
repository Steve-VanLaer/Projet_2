# Par défaut le PS exécute deux (ou plusieurs) corps de texte sur deux lignes
print("A")
print("B")

# Rassembler deux (ou plusieurs) corps de textes sur une seule ligne
print("A",end="")       # chaque argument de la fonction print() est séparé par une virgule (,)
print("B")

# Relier deux (ou plusieurs) corps de textes par un signe
print("A",end=",")
print("B")

# Séparer un corps de textes par un saut de ligne
print("A",end="\n")
print("B")

# Utiliser plusieurs sauts de ligne
prenom = 'André'
print("Bonjour\n\n\n"+prenom)

# Séparer des chaînes de caractères par un espace ou un signe
print("A","B",sep=" ")      # si les guillemets ("") ne continnent pas d'espace, aucun espace ne sera affiché
print("A","B",sep="-")

# Afficher du texte avec une tabulation
print("\t","B","\t","B")    # tabulation = 8 espaces
