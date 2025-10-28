# Afficher l'ensemble des éléments de la liste, utiliser 2 méthodes avec for() et une avec while
liste = ['vache','souris','levure','bactérie']
# for() sur les éléments
for objet in liste:
    print(objet)

# for() sur les indices
for i in range(0,4):
    print(liste[i])

# while sur les indices
i = 0
while i <4:
    print(liste[i])
    i+= 1

semaine = ['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']
# afficher les jours de la semaine avec for()
for jour in semaine:
    print(jour)

# afficher les jours du week-end avec while
i = 0
while i < 3:
    print(semaine[-2:])
    i+=1

# afficher les nombres de 1 à 10 sur une seule ligne
for n in range(1,11):
    print(n,end=", ")

i = 1
while i < 11:
    print(i,end=", ") 
    i+=1
# afficher une liste de nombres pairs à partir d'une liste de nombres imapairs
N = list(range(22))
Impairs = []
for n in N:
    if n % 2 !=0:
        Impairs.append(n)
print(Impairs)
# liste compréhensive
Impairs = [n for n in N if n % 2 != 0]
print(Impairs)

# moyenne des notes d'un étudiant
notes = [14, 9, 6, 8, 12]
moyenne = sum(notes) / len(notes)
print(f"La moyenne est {moyenne:.2f}")

# Créer une liste contenant les nombres entiers pairs de 2 à 20 inclus
pairs = []
for n in range(1,21):
    if n % 2 == 0:
        pairs.append(n)
# Afficher le produit des nombres consécutifs deux à deux
for i in range(0,len(pairs)-1,2):
    a = pairs[i]
    b = pairs[i+1]
    print(f"{a} * {b} = {a*b}")
# méthode zip
for a, b in zip(pairs[::2], pairs[1::2]):       # pairs[::2] cherche l'indice du premier couple
    print(f"méthode zip : {a} * {b} = {a*b}")           # pairs[1::2] cherche l'indice du second couple

# afficher le signe '*' en l'incrémentant sur chaque ligne jusqu'à 10
for i in range(1,11):
    print('*' * i)
# faire l'inverse en partant de 10 jusqu'à 1
for i in range(10,0,-1):
    print('*'*i)
# utiliser un espace de 10 caractères avant d'aficher les * et décrémenter cet espace
n = 10
y = n+1
for i in range(1,n+1):
    y-=1
    print(" " * (y) + "*"*i)
# afficher 10 * sans espace et incrémenter cet espace tout en décrémentant le nombre de *
y = n+1
for i in range(1,n+1):
    y-=1
    print(' ' * i + "*" * y)
# afficher une pyramide
for i in range(1,n+1):
    etoiles = '*' * (2 * i - 1)     # nbre étoiles
    print(etoiles.center(2 * n -1))

# créer une suite qui contient une suite de nombres impairs
impairs = []
for i in range(1,5):
    impairs.append(2 * i - 1)   # va jusqu'à 7 (2 * 4 - 1)
print(impairs)
# autre méthode
for i in range(1,5,2):          # va jusqu'à 3
    print(i)

# boucle négative
for i in range(4,0,-1):
    print(i)

# Afficher les nombres de 1 à 20 en sautant les multiples de 3
liste = list(range(1,21))
for i in liste:
    if i % 3 == 0:
        continue
    print(i)

# Afficher une matrice carrée (1, 1, 2, 2 et 1, 2, 1, 2) avec des boucles for() imbriquées
print("ligne\tcolonne")
for i in range(1,3):
    for y in range(1,3):
        print(i,"\t",y)
# l'affichage de la matrice montre l'ordre dans laquel se fait les itérations avec deux boucles for() successives
# 1) élément 1 de i puis élément 1 de y --> 1 et 1
# 2) élément 1 de i puis élément 2 de Y --> 1 et 2
# 3) élément 2 de i puis élément 1 de y --> 2 et 1
# 4) élément 2 de i puis élément 2 de y --> 2 et 2
# boucles au carré -> 2 itérations par fonction
print("ligne\tcolonne")
i = 1
while i < 3:                # boucle externe
    y = 1
    while y < 3:            # boucle interne
        print(i,"\t",y)
        y += 1
    i += 1
# Parcours de l'itération dans les deux boucles imbriquées
# A la première itération dans la boucle externe, i a la valeur 1, l'itération passe alors à la boucle interne
# y a été initialisée dans la boucle externe, il a donc la valeur 1 -> premier affichage : 1 et 1
# à l'issue de cette première itération dans la boucle interne, y est incrémenté
# l'itération reste dans la boucle interne et y a la valeur 2 puisqu'il a été incrémenté au passage précédent -> 2è affichage : 1 et 2
# à l'issue de cette deuxième itération y a la valeur 3, i est ensuite incrémenté et a maintenant la valeur 2
# la boucle interne a terminé sa boucle et l'itération revient à la boucle externe
# idem avec i = 2

# demi matrice
i = 1
while i < 3:
    y = 1
    while y < 3:
        if i == 2 and y == 1:       # l'itération s'arrête dès qu'elle sort une première fois de la boucle interne
            break
        print(i,"\t",y)
        y += 1
    i += 1
print(" -- ")
# pour obtenir : 1(i) 2(y) puis 2(i) 2(y)
i = 1
while i < 3:
    y = 1
    while y < 3:
        if y == 1:          # uniquement si y = 1
            y += 1          # alors incrémenter et ..
            continue        # passer à l'itération suivante dans la boucle interne sans passer à l'instrution suivante (print)
        print(i, "\t", y)   # au 2è passage, y a la valeur 2 -> afficher
        y += 1              # y incrémenté = 3 -> fin de la boucle interne
    i += 1
print(" -- ")

# afficher des paires ordonnées croissantes de l'ensemsble {1, 2, 3, 4} pour former une matrice
# 2 colonnes et 6 lignes
# observations : le second membre de chaque couple (i, y) est tjs plus grand que le premier
for i in range(1,4):
    y = i+1
    while y < 5:
        print(i,"\t",y)
        y += 1
print(" --")
# même chose plus court
for i in range(1,4):
    for y in range(i+1,5):
        print(i,"\t",y)

# Simuler le nombre de sauts de puce pour atteindre le point 5 d'une ligne graduée depuis le point 5 à l'aide de la fonction random()
import random
x, y = 0, 0
while x < 5:
    saut = random.randint(0,1)
    if saut == 0:
        x -= 1
        y += 1
        print('x :',x,'nbre de sauts : ',y)
    elif saut == 1:
        x += 1
        y += 1
        print('x : ',x,'nbre de sauts :',y)
# Version Python de ce code
x, y = 0, 0
while x < 5:
    saut = random.choice([-1,1])    # direcment -1 ou 1
    if x == 0 and saut == -1:       # si la puce est à 0 et que le random la ferait partir en arrière (x < 0)
        continue                    # relancer jusqu'à un random de 1 -> but = éviter que la puce parte en arrière (x < 0) indéfiniment
    x += saut
    y += 1
    # print('x : ',x,'nbre sauts',y)

# Afficher la suite de Fibonacci jusqu'à son 15è terme
fibo = [0, 1]               # puisque la suite est constituée d'une somme (Xn = Xn-1 + Xn-2), on part de deux éléments
for i in range(0,13):       # et puisqu'il faut additionner deux éléments qui se suivent, on va boucler sur les index
    new = fibo[i] + fibo[i+1]
    fibo.append(new)
print(fibo, end=", ")

fibo = [0, 1]
n = 15  # nombre de termes voulus

for i in range(n - 2):   # on a déjà 2 termes, donc le calcul s'effectue pour 13 termes supplémentaires, par défaut boucle commence à 0
    fibo.append(fibo[-1] + fibo[-2])    # à la 1ère itération, la liste 'fibo' contient 2 éléments
print(fibo)                             # les valeurs recherchées sont la dernière et l'avant-dernière, donc le couple (0, 1)
                                        # on ajoute ensuite la somme de ce couple (1) à la liste -> elle a maintenant 3 éléments
                                        # à la seconde itération, la liste 'fibo' contient 3 éléments
                                        # les valeurs recherchées sont tj la dernière et l'avant-dernière, donc le couple (1,1)
                                        # on ajoute ensuitse la somme de ce couple (2) à la liste -> elle a maintenant 4 éléments
                                        # la boucle s'arrète à la 13è itération, donc au 15è élément
# afficher la constante de la suite de Fibonacci (nombre d'or)
print('n\tf(n)\tconstante')
for i in range(1,14):                    # partir de 1 pour éviter la division par 0 du premier élément
        constante = fibo[i+1] / fibo[i]             # calculer le rapport de deux termes consécutifs
        print(f"{i}\t{fibo[i]}\t{constante:.5f}")