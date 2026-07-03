# Exercice 3: Calcul de la base duale de polynômes
## Énoncé
Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes de degré inférieur ou égal à 2.
Soit la base canonique $\mathcal{B} = (1, X, X^2)$. On définit les formes linéaires suivantes sur $E$ :
$\varphi_1(P) = P(0)$
$\varphi_2(P) = P'(0)$
$\varphi_3(P) = \frac{1}{2}P''(0)$
Montrer que la famille $(\varphi_1, \varphi_2, \varphi_3)$ est exactement la base duale $\mathcal{B}^*$.


## Correction détaillée
La base duale $\mathcal{B}^* = (e_1^*, e_2^*, e_3^*)$ associée à $\mathcal{B} = (e_1, e_2, e_3) = (1, X, X^2)$ est l'unique famille de formes linéaires vérifiant $e_i^*(e_j) = \delta_{i,j}$.
Vérifions que $\varphi_1, \varphi_2, \varphi_3$ satisfont ces conditions.

1. **Évaluation de $\varphi_1$ :**
   $\varphi_1(P) = P(0)$.
   $\varphi_1(e_1) = \varphi_1(1) = 1$.
   $\varphi_1(e_2) = \varphi_1(X) = 0$.
   $\varphi_1(e_3) = \varphi_1(X^2) = 0^2 = 0$.
   Donc $\varphi_1$ correspond bien à $e_1^*$.

2. **Évaluation de $\varphi_2$ :**
   $\varphi_2(P) = P'(0)$.
   $e_1'(X) = 0 \implies \varphi_2(e_1) = 0$.
   $e_2'(X) = 1 \implies \varphi_2(e_2) = 1$.
   $e_3'(X) = 2X \implies \varphi_2(e_3) = 2(0) = 0$.
   Donc $\varphi_2$ correspond bien à $e_2^*$.

3. **Évaluation de $\varphi_3$ :**
   $\varphi_3(P) = \frac{1}{2}P''(0)$.
   $e_1''(X) = 0 \implies \varphi_3(e_1) = 0$.
   $e_2''(X) = 0 \implies \varphi_3(e_2) = 0$.
   $e_3''(X) = 2 \implies \varphi_3(e_3) = \frac{1}{2}(2) = 1$.
   Donc $\varphi_3$ correspond bien à $e_3^*$.

Puisque les formes $\varphi_1, \varphi_2, \varphi_3$ vérifient les relations de Kronecker avec la base $\mathcal{B}$, elles constituent bien la base duale $\mathcal{B}^*$.
