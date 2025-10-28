# Addition
print("2 + 2 = ",2+2)

# Différence 
print("3 - 1 = ",3-1)

# Multiplication
print("3 x 2 = ",3*2)

# Division
print("6 / 2 = ",6/2)

# Afficher le quotient d'une fraction
quotient = 6 // 2
print('quotient de 6 / 2 = ',quotient)

# Afficher le reste d'une fraction
reste = 6 % 2
print('reste de 6 / 2 = ',reste)

# Utilié de l'opérateur // et du modulo %
nombre = int(input('Introduisez un nombre en secondes : '))
minutes = nombre // 60
secondes = nombre % 60
print('Le nombre introduit en secondes équivaut à',minutes,'minutes et',secondes,'secondes.')

# Autre usage du modulo
n = 4
if n % 4 == 0:          # pour l'usage des mots clé 'if' ...
    print(n,'est pair')
else:                   # ... et 'else', voir le fichier bool.py du même sous-dossier 'Variables'
    print(n,' est impair')  

# Vérfier si une année est bissextile
annee = 2025
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0 :
    print('année bissextile')
else:
    print('année normale')
