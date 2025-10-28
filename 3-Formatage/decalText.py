# Décaler du texte de 5 caractères (espaces) vers la droite
print(f"atome {"HN":>4s}")      # affiché à droite dans un champ de 5 caracères
print(f"atome {"HN":<4s}")      # affiché à gauche dans un champ de 5 caractères

# important pour résoudre le problème de la tabulation
# certains éléments de la liste 'semaine' ont 8 caractères, de ce fait le mot suivant est décalé à l'affichage par rapport à la tabulation
# la solution consiste à ne pas utiliser la tabulation et 
# à choisir de placer le premier mot à gauche avec un décalage de 10 caractères (10 - 8 = 2 champs libres)
semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
for i in semaine:
    if i == 'vendredi':
        print(f"{i:<10s} chouette c'est vrendredi")
    elif i == 'samedi' or i == 'dimanche':
        print(f"{i:<10s} repos c'est week end")
    else:
        print(f"{i:<10s} au travail")