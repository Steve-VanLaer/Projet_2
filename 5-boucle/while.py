# Structure de la boucle while
i = 1                   # déclarer et initialiser la variable d'itération
while i<= 6:            # écrire le test
                        # écrire ici le bloc d'instruction
    i = i + 1           # incrémenter la variable d'itération pour éviter que la boucle tourne à l'infini (mise à jour)
                        # Pour arrêter une boucle qui tourne à l'infini : Ctrl + C
                        # respecter l'indentation
# La boucle while() est indiquée lorsqu'on ne connaît pas à l'avance le nombre d'itérations

# Faire tourner la boucle tant que l'utilisateur n'a pas introduit la donnée corrcte
i = 0
while i < 18:
    reponse = int(input('Introduisez un nombre supérieur à 18 : '))
    i = reponse

