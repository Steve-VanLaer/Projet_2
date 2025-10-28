# Les comparateurs s'utilisent avec le testeur 'if'
a = 10

# est égal
if a == 10:             # les deux points (:) sont nécessaires
    print(a,' = 10')    # Le testeur 'if' suppose (implique) une instruction qui suit, ...
                        # ... pour ne pas la confondre avec une instruction qui ne dépend pas du test logique ...
                        # ... l'indentation (4 espaces) est nécessaire
                        
# n'est pas égal
if a != 10:
    print(a,' pas égal à 10')   # n'affiche rien puisque la condition n'est pas remplie

# est strictement plus grand
if a > 10:
    print(a,'> 10')

# est plus grand ou égal
if a >= 10:
    print(a,'>= 10')

# est strictement plus petit
if a < 10:
    print(a,'< 10')

# est plus petit ou égal 
if a <= 10:
    print(a,' <= 10')

# Affiner une comparaison avec 'and' (P et Q)
if a < 20 and a > 0:
    print(a,'est dans l\intervalle 0:20')
# Même test mais avec une variable bool pour effectuer le test
test = a < 20 and a > 0     # le résultat du test est stockée sous un type bool (vrai ou faux)
print(test)

# Avec 'or'
if a == 20 or a == 10:
    print(a,'est = à 10 ou 20')
test = a == 20 or a == 10
print(test)

# Il est possible de comparer des châines de caractères
mot1 = 'python'
mot2 = 'programmation'
if len(mot1) > len(mot2):
    print(mot2)

# Vérifier l'égalité entre deux chaînes de caractères
mot2 = 'python'
if mot1 == mot2:
    print('même mot')

