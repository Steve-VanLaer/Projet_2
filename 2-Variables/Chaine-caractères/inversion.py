# Inverser les caractères d'une chaîne
texte   = "Bonjour"
inverse = texte[::-1]       # voir le sous-dossiers 'Liste'
print(inverse)

# Autre méthode
inverse = "".join(reversed(texte))
print(inverse)

# Avec une boucle
inverse = ""
for c in texte:
    inverse = c + inverse   # si la variable d'itération 'c' avait seulement été utilisée sans '+ inverse', ...
print(inverse)              # ... le résultat aurait donné 'Bonjour'.
                            # Explication du processus menant à l'inversion de la variable 'texte'
                            # 1ère itération : inverse = B + inverse = B + "" = B
                            # 2ème itération : inverse = O + inverse = o + inverse = O + B = oB
                            # 3ème itération : inverse = n + iversee = n + inverse = n + o + B = noB
                            # etc.
                            