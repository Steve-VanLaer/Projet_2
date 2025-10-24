# Afficher un pourcentage à deux décimales
cote = int(input('Introduisez vortre note sur 30 : '))
pc   = cote/30*100
print(f"Votre cote en pc est {pc:.2f} %.")      

# Afficher la cotation de l'EUR/USD avec 5 décimales
eurusd = float(input('Introduisez le cours de l\'euro : '))
print(f"Le cours de l\'EUR/USD à 5 décimales est {eurusd:.5f}.")