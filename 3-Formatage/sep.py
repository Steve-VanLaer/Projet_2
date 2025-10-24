# Par défaut Pyton ajoute à l'affichage un espace entre les arguments de la fonction print()
print("Foramt par défaut : ","A","B","C")
# Séparer les arguments par un espace
print("Avec un espace : ","A","B","C",sep=" ")
# Sans espace entre les guillemets du mot-clé 'sep', les arguments sont concaténés
print("Concaténation des arguments : ","A","B","C",sep="")
# Séparer les arguments par un tiret (-) ou n'importe quel autre caractère
print("Avec un tiret : ","A","B","C",sep="-")
print("Avec | :","A","B","C",sep="|")
# Concaténer une adresse e-mail
nom  = input('Introduisez votre nom : ')
prenom = input('Introduisez votre prénom : ')
partie_locale = prenom+"."+nom
print(partie_locale,"gmail.com",sep="@")