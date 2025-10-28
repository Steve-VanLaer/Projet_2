#
semaine = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
for i in semaine:
    if i == 'vendredi':
        print(f"{i:<10s} chouette c'est vrendredi")
    elif i == 'samedi' or i == 'dimanche':
        print(f"{i:<10s} repos c'est week end")
    else:
        print(f"{i:<10s} au travail")

# remplacer une séquence d'un brin d'ADN par sa séquence complémentaire
# -> remplacer les lettres 'A' par 'T', 'T' par 'A', 'C' par 'G' et 'G' par 'C'
sequence = ['A', 'C', 'G', 'T', 'T', 'A', 'G','C', 'T', 'A', 'A', 'C', 'G']
for i, j in enumerate(sequence):    # il faut boucler sur les élémnents et les index
    if j == 'A':
        sequence[i] = 'T'
    elif j == 'T':
        sequence[i] = 'A'
    elif j == 'C':
        sequence[i] = 'G'
    else :
        sequence[i] = 'C'
print(sequence)

# Afficher le minimum et le maxium d'une suite de nombres sans recourir à la foncton min() et max
N = [8, 4, 6, 1, 5]
min, max = 8, 8         # initialiser a la première valeur de la liste
for i in N:
    if i > max:
        max = i
    if i < min:
        min = i
print('max :',max,'min :',min)

# Calculer la fréquence des acides aminés alanine (A), arginine (R), tryptophane (W) et glycine (G) dans cette séquence
sequence = ['R','A','W','W','A','W','A','R','W','W','R','A','G']
occ_A, occ_R, occ_W, occ_G = 0, 0, 0, 0
for i in sequence:
    occ_A = sequence.count('A')
    occ_R = sequence.count('R')
    occ_W = sequence.count('W')
    occ_G = sequence.count('G')
print(f'fréquence A {occ_A}, fréquence R {occ_R}, fréquence W {occ_W}, fréquence G {occ_G}')

# A partir d'une liste de nombre de 1 à 20, ...
# ... afficher les nombres pairs inférieurs ou égaux à 10 et ...
# ...les nombres impairs strictement supérieurs à 10
liste = list(range(0,21))
for i in liste:
    if (i % 2 == 0) and (i <= 10):
        print('pair :',i)
    elif (i % 2 != 0) and (i > 10):
        print('imapair :',i)

# Afficher une suite de Syracuse à partir d'un nombre n
n = 14
Syracuse = [14]
i = 0
while i < 20:
    if n % 2 == 0:
        n = n // 2      # obtenir seulement le quotient --> la divison normale donne un résultat float
    else:
        n = n * 3 + 1
    Syracuse.append(n)
    i = i + 1
print(Syracuse)
# version plus compacte
n = 14
Syracuse = [n]
i = 0 
while i < 20:
    n = n // 2 if n % 2 == 0 else 3 * n + 1     # pas de (:) à la fin
    Syracuse.append(n)
    i = i + 1
print(Syracuse)
# astuce, puisque dans cet exemple la variable d'itération n'est pas utilisée dans des calculs
n = 14
Syracuse = [n]
for _ in range(21):     # _ -> pour indiquer que la variable d'itération n'est pas nécessaire
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    Syracuse.append(n)
print(Syracuse)

# Test de primalité de 0 100
liste = list(range(0, 50))
nbre_prem = []

for n in liste:
    if n < 2:           # 0 et 1 sont exclus par définition
        continue
    premier = True
    for div in range(2, int(n**0.5) + 1):   # intervalle =[2, quotient de racine carrée de n + 1 pour l'indexation]
        if n % div == 0:                                                # racine carrée de n pr obtenir le + grand multiple de n
            premier = False         # si n est divisible par un autre entier que 1 et lui-même
            break
    if premier:
        nbre_prem.append(n)

print(nbre_prem)

