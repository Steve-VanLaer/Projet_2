# Tous les éléments d'une liste sont indexés, ce qui permet de les retrouver grâce à leur index
liste = list(range(10))
liste[0]                    # affiche l'élément situé à l'index 0, c'est-à-dire le premier
liste[-1]                   # l'indexation peut se faire de droite à gauche, le prmier index en partant de la droite ...
                            # ... est numéroté '-1', les index suivants en partant de la droite sont < -1
                            # ici on veut donc afficher le dernier élément de la liste
liste[-4]                   # affiche le 4é élément en partant de la droite
liste[:]                    # affiche toute la liste, taper le nom de la liste dans la fonction print() = toute la liste affiché
# pour savoir si un élément est présent dans une liste
3 in liste                  # print() pour afficher le résultat bool

# copier une liste
y = liste                   # en procédant de la sorte, toute modification apportée à la liste 'y' modifiera la liste initiale

# Copier une liste indépendante de la liste initiale
y = liste[:]

# Indexation à deux dimensions
printemps   = ['mars', 'avril', 'mai']
ete         = ['juin','juillet','août']
automne     = ['septembre','octobre','novembre']
hiver       = ['décembre','janvier','février']
saison      = [printemps, ete, automne, hiver]
saison[1][0]    # affiche le premier élément de la deuxième liste ('juin')
                # puisque la liste 'saison' est une liste de listes, il faut préciser dans quelle liste appartient l'élément à indexer
                # [1er crochet : index de la sous-liste] [2è crochet : index de l'élément de la sous-liste]
# Aafficher une sous-liste avec la méthode du tranchage (voir Liste/slsice.py)
saison[1:2]     # affiche une tranche de la liste 'saison' depuis le deuxième élément jusqu'au troisième EXCLU
                                   # de juin à août
