"""
Chaîne de caractères
"""
# Formater une chaîne de caractères
prenom = "Andrée"
print(f"Bonjour {prenom}")           # dans f-string, les variables doivent toujours être renseignées entre {}

# Utiliser le saut de ligne avec un format
print(f"Bonjour \n {prenom}")

# Formater plusieurs variables
nom     = "Gilbert"
print(f"Bonjour {prenom} {nom}")

"""
Float
"""
# Faire apparaître les décimales d'une valeur float dans une chaîne de textes
cours = 1.22
print("cours :",f"{cours:.5f}")

# Faire apparaître les décimales d'une valeur float dans un format
print(f"cours : {cours:.5f}")