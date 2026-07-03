---
title: "Exercice 9 : Sommation d'une série absolument convergente"
difficulty: ★★★★★
---
# Exercice 9 : Sommation d'une série absolument convergente

## Énoncé
Montrer que la série $\sum_{n=2}^\infty \frac{1}{n^2 - 1}$ converge absolument et calculer sa somme.

## Correction
1. **Convergence absolue :** Le terme général est $u_n = \frac{1}{n^2 - 1}$. Il est strictement positif pour $n \ge 2$. Au voisinage de l'infini, $u_n \sim \frac{1}{n^2}$.
Par équivalence avec une série de Riemann convergente ($\alpha = 2 > 1$), la série $\sum u_n$ converge (donc absolument).
2. **Décomposition en éléments simples :**
   $u_n = \frac{1}{(n-1)(n+1)} = \frac{A}{n-1} + \frac{B}{n+1}$.
   On trouve $A = 1/2$ et $B = -1/2$, d'où $u_n = \frac{1}{2}(\frac{1}{n-1} - \frac{1}{n+1})$.
3. **Calcul de la somme partielle par télescopage :**
   $S_N = \sum_{n=2}^N \frac{1}{2}(\frac{1}{n-1} - \frac{1}{n+1}) = \frac{1}{2} [ (1 - 1/3) + (1/2 - 1/4) + (1/3 - 1/5) + ... + (\frac{1}{N-2} - \frac{1}{N}) + (\frac{1}{N-1} - \frac{1}{N+1}) ]$.
   Presque tous les termes s'annulent. Il reste les premiers termes positifs et les derniers termes négatifs :
   $S_N = \frac{1}{2} (1 + \frac{1}{2} - \frac{1}{N} - \frac{1}{N+1})$.
4. **Passage à la limite :**
   $\lim_{N\to\infty} S_N = \frac{1}{2} (1 + 1/2 - 0 - 0) = \frac{3}{4}$.
   La somme de la série est $3/4$.
