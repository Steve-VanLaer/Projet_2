# In n'est pas possible de concaténer des nombres ni des nombres des chaînes de caractères

# Concaténer des chaînes de caractères
a = 'to'
b = 'to'
print(a+b)

# Des chaînes de textes séparées par un espace sont automatiquement concaténées
texte = 'Py' 'thon' ' ' 'est' ' ' 'génial'
print(texte)

# Application de ce qui précède
texte = ('Mon texte à exécuter est bien trop long pour tenir sur une ligne, '
         'c\'est pourquoi j\'écris la suite à la ligne dans mon fichier. Mais '
         'il apparaîtra sur une ligne lors de l\'exécution du fichier.')
print(texte)

# Répéter (dupliquer) des chaînes de caractères
a = 'la'
print(a*3)

# Concaténer une adresse e-mail
nom = 'albert'
prenom = 'marc'
print(nom,prenom,sep=".",end="@")
print("yahoo.com")



