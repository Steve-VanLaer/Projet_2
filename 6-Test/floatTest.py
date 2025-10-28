# 
test = (3 - 2.7) == 0.3
print(test)     # la valeur renvoyée == faux
                # les valeurs float sont approchées 
f = 0.3
print(f" {f:.5f}")
print(f"{f:.60f}")
                # ne jamais utiliser un testeur booléen pour comparer deux valeurs float
                # toujours utiliser un intervalle avec une certaine précision (delta)
# Vérifier le test suivant
delta = 1e-5        # on teste jusqu'à la 5 décimale
var   = 3.0 - 2.7   # le test
test = 0.3 - delta < var < 0.3 + delta  # 0.3 puisque c'est la valeur approchée
     # 0.3 - 0.00001 < var < 0.3 = 0.00001
     # 0.29999 < var < 0.30001
print('résultat : ',test)
# Autre méthode pour le test
test = abs(var - 0.3) < delta
        # ((3.0 - 2.7) - 0.3) < 0.00001
        # (le résultat) doit < 0.00001
print(test)
# Autre méthode pour le test    --> préférer cette méthode (plus compacte, lisible)
import math
var = 3.0 - 2.7
test = math.isclose(var,0.3,abs_tol=1e5)    # (le test, la valeur approhcée, la tolérance en valeur absolue)
print(test)