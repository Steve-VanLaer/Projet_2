# La fonction input() permet d'introduire des données par l'utilisateur qui seront ensuite traitées par le script
prénom = input("Introduisez votre prénom : ")      
print("Bonjour",prénom)
                                                        # les exercices suivants montrent comment introduire des données chiffrées

age = input('Introduisez votre âge : ')
print(age)      # L'utilisateur va introduire un entier. Cependant, la fonction input() étant de type string, la valeur renvoyée ...
                # ... sera de type string. Le nombre introduit par l'utilisateur pourra donc être introduit comme argument dans ...
                # ... fonction print() qui n'accepte que des chaînes de caractères. 
