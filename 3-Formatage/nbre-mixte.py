"""
Exercice sur les nombres mixtes

Intruction : afficher une fraction sous la forme '7/3 = 2 + 1/3'

Formule = a / b = q + r/b    où q = quotient et r = reste   avec 0 <= r < b
    voir le fichier Nbre-mixte.pdf pour comprendre la notation algégrique d'un nombre mixte
"""
numerateur   = int(input('Introduisez un entier : '))
denominateur = int(input('Introduisez encore un entier mais plus petit que le premier et supérieur à 0 : '))
quotient     = numerateur//denominateur
reste        = numerateur%denominateur
n1           = quotient
n2           = f"{reste}/{denominateur}" 
print(f"{numerateur}/{denominateur} = {n1} + {n2}")

# Intérêt d'utiliser le modulo
temps_secondes = int(input('Introduisez un entier supérieur à 1000 mais inférieur à 3600 : '))
minutes        = temps_secondes // 60   # 60 secondes dans 1 minute
secondes       = temps_secondes % 60    # secondes restantes
print(f" {temps_secondes} secondes = {minutes} minutes {secondes} secondes")