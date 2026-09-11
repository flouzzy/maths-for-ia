# Exercice 9 : Convergence monotone pour les mesures

**Difficulté :** $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$

## Énoncé
Soit $\mu_n$ une suite croissante de mesures sur $(X, \mathcal{F})$. Montrer que $\mu(A) = \lim \mu_n(A)$ définit une mesure, en s'inspirant de Beppo-Levi.

## Correction Détaillée
1. $\mu(\emptyset) = \lim 0 = 0$.
2. Pour des ensembles disjoints $A_k$, $\mu(\cup A_k) = \lim_n \sum_k \mu_n(A_k)$. On utilise une variante du TCM (ou l'interversion limite-somme double sur des termes positifs) pour obtenir $\sum_k \lim_n \mu_n(A_k) = \sum_k \mu(A_k)$.
