*** 1.3) formatage de chaînes de caractères ***

Cette partie aborde l'affichage de valeurs à partir de la fonction print().

La fonction print() peut contenir des valeurs de tout type, par défaut elles sont converties en string.

-- **hello.py** : afficher 'Hello World !'
-- **int.py**   : afficher un entier
--**float.py**  : afficher un nombre décimal

La fonction print() peut contenir plusieurs arguments. Pour indiquer à Python qu'on veut introduire plusieurs arguments dans la fonction print(), séparer les arguments par une virgule (,). A l'affichage Python ajoute un espace entre les arguments et les affiche par défaut sur une ligne. Ces arguments peuvent être de tout type.

-- **bonjour.py** : demander le prénom de l'utilisateur et afficher 'Bonjour, {prénom}.'
-- **arg.py**     : afficher plusieurs arguments de type différent

Les arguments de la fonction print() peuvent être séparés par un/plusieurs caractère(s) de son choix à l'aide du mot-clé 'sep'.

- **sep.py**      : utiliser le mot-clé 'sep'

Il est possible d'écrire deux ou plusieurs fonctions print() sur une ligne, dans ce cas séparer les fonctions print() par un point virgule (;). Python affiche ces fonctions sur autant de lignes qu'il y a de fonctions print().

Pour indiquer à Python qu'il faut afficher le résultat de plusieurs fonctions print(), utiliser le mot-clé 'end'.

- **end.py** : écrire une phrase dans deux fonctions print() à l'aide du mot-clé 'end'
- **end.py** : combiner les mot-clés 'sep' et 'end'

Les arguments de la fonction print() peuvent aussi être concaténés à l'aide du signe '+'

- **concat.py** : concaténer à l'aide du signe '+'

Pour faciliter le formatage d'une chaîne de caractères Python offre la possibilité d'utiliser les 'f-string'. La syntaxe de base est : print(f"texte"). Pour introduire une variable : print(f" texte {variable}).

- **fstringVariable.py** : introduire une variable dans un f-string

Par défaut Python affiche les nombres décimaux avec une décimale. Mais il est possible de choisir le nombre de décimales à afficher.

- **fstringDecimal.py** : 

Avec les f-string il est possible de décaler l'affichage des chaînes de caractères vers la droite ou vers la gauche.

- **fstringDecalInt.py**   : décaler des entiers
- **fstringDecalFloat.py** : décaler des nombres décimaux
- **fstringDecalTexte.py** : décaler du texte

Pour faire apparaître des accolades {} dans un f-string il suffit de les doubler. Dans Python on accède à la notation scientifique à l'aide de la lettre 'e'.

- **fstringAccol.py** : afficher des accolades {} dans un f-string
- **fstringNotScien** : utililser la notation scientifique dans un f-string

On a vu dans la partie 2 consacrée aux variables l'emploi des symboles '//' et '%' pour obtenir le quotient et le reste d'une division. Par ce moyen il est possible de réalier des calculs particulièrement pratiques.

- **nbre-mixte.py** : Afficher un nombre mixte

Le fichier Nbre-mixte.pdf aide à comprendre la formule utilisée dans le dernier exerice à partir de la forme algébrique d'une division euclidienne.