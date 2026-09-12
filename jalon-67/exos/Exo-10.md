# Exercice 10 : Opérateurs de Fredholm et séries

**Difficulté :** $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\bigstar$

## Énoncé
Soit $K(x, y)$ un noyau positif. On définit $Tf(x) = \int K(x, y) f(y) dy$. Montrer que $T(\sum u_n) = \sum T(u_n)$ pour $u_n$ positives.

## Correction Détaillée
1. On écrit $T(\sum u_n)(x) = \int K(x, y) \left( \sum u_n(y) \right) dy = \int \sum \left( K(x,y) u_n(y) \right) dy$.
2. Comme $K$ et $u_n$ sont positifs, on applique le corollaire du TCM (sommation de Beppo-Levi).
3. Cela donne $\sum \int K(x,y) u_n(y) dy = \sum T(u_n)(x)$.
