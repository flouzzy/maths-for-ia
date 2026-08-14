# Borne inférieure sur la taille

### Énoncé $\quad \bigstar\bigstar\bigstar\bigstar\bigstar$

Pour approcher l'indicatrice d'un hypercube en dimension $d$ avec une activation sigmoïde de type heaviside approchée, quel est le nombre minimal de neurones requis dans une seule couche cachée ?

### Démonstration Détaillée

L'hypercube possède $2^d$ sommets et $2d$ faces. Chaque neurone de la couche cachée décrit un hyperplan affine qui divise l'espace. Pour découper un volume fini et borné (l'intersection de $2d$ demi-espaces), il faut au strict minimum $2d$ hyperplans. Donc il faut au moins $2d$ neurones dans la couche cachée pour créer la primitive de la localisation spatiale en dimension $d$. C'est un argument géométrique (théorème de Cover).
