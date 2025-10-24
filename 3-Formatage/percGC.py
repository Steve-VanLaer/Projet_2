"""
Afficher le pourcentage de GC avec 0, 1, 2 et 3 décimales sous forme arrondie
Aligner les signes %
"""
perc_GC = ((4500+2575)/14800)*100
texte   = 'Le pourcentage de GC est'
print(f"{texte} {perc_GC:.0f} {'%':>5s}")   # les escpaces comptent pour 1 caractère
print(f"{texte} {perc_GC:.1f} {'%':>3s}")
print(f"{texte} {perc_GC:.2f} {'%':>2s}")
print(f"{texte} {perc_GC:.3f} {'%':>1s}")