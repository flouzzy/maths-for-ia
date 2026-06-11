# Exercice 1 - Difficulté: Niveau 1

## 1. Énoncé
Démontrer par contraposition que pour tout entier $n \in \mathbb{N}$, si $n^2$ est pair, alors $n$ est pair.

## 2. Démonstration (Zéro Ellipse)
Soit $n \in \mathbb{N}$. On veut montrer : $(n^2 \text{ pair}) \implies (n \text{ pair})$. La contraposée est : $(n \text{ impair}) \implies (n^2 \text{ impair})$. Supposons $n$ impair. Alors il existe $k \in \mathbb{N}$ tel que $n = 2k + 1$. Élevons au carré : $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$. Posons $K = 2k^2 + 2k \in \mathbb{N}$. On a $n^2 = 2K + 1$. Donc $n^2$ est impair. La contraposée est vraie, donc l'implication originale l'est aussi.
