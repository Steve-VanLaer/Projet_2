# Trouver le quotient d'une division euclidienne
numerateur = int(input('Introduisez un entier : '))
denominateur = int(input('Introduisez un entier plus petit que le premier : '))
quotient = numerateur // denominateur
print("Le quotient de ",numerateur,"/",denominateur,"est",quotient)

# Trouver le reste d'une division euclidienne
reste = numerateur % denominateur
print('Le reste de ',numerateur,'/',denominateur,'est',reste)