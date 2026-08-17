## Exercice 10 : Approximation par réseaux de largeur fixe et profondeur arbitraire \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Le théorème de Cybenko considère une largeur arbitraire et une seule couche cachée. Quel est le résultat analogue (théorème de Lu et al. 2017) pour une largeur fixe et une profondeur arbitraire, utilisant la fonction ReLU ?

**Correction :**
Lu et al. ont prouvé que pour approcher n'importe quelle fonction continue de $I_n$ vers $\mathbb{R}^m$ avec une précision arbitraire, un réseau ReLU avec une largeur maximale $W$ et une profondeur arbitraire est un approximateur universel si et seulement si $W \ge n + m + 1$.
C'est le théorème d'approximation universelle par largeur (Width-Bounded Universal Approximation Theorem).
Pour une fonction de $\mathbb{R}^n \to \mathbb{R}$, il suffit d'une largeur de $n+2$. Si la largeur est strictement inférieure à ce seuil, il existe des fonctions lisses qui ne peuvent pas être approximées, peu importe la profondeur du réseau (la "bande passante" de l'information s'étrangle à chaque couche, détruisant la topologie du signal d'entrée).
