---
title: "Exercice 6 - Suite de Cauchy de fonctions non convergente"
difficulty: $\bigstar\bigstar\bigstar\star\star$
---

# Exercice 6 - Suite de Cauchy de fonctions

**Énoncé :**
Soit $f_n$ la suite de l'Exercice 4. Montrer que $(f_n)$ est une suite de Cauchy dans l'espace $\mathcal{R}([0,1])$ muni de la norme $\|g\|_1 = \int_0^1 |g(x)| dx$.

**Démonstration pas à pas :**
1. On a $\|f_n - f_m\|_1 = \int_0^1 |f_n(x) - f_m(x)| dx$.
2. Pour $m \ge n$, $f_m - f_n = 1_{\{q_{n+1}, \dots, q_m\}}$.
3. C'est l'indicatrice d'un ensemble fini. Donc d'après l'Exercice 3, son intégrale de Riemann vaut 0.
4. Ainsi, $\|f_n - f_m\|_1 = 0$ pour tous $n, m$.
5. C'est bien une suite de Cauchy (trivialement !).
6. Cependant, sa limite ponctuelle est la fonction de Dirichlet, qui n'est pas dans $\mathcal{R}([0,1])$. Cela montre que $\mathcal{R}([0,1])$ muni de $\|\cdot\|_1$ n'est pas complet (les éléments de la complétion, ici la classe d'équivalence de $0$, ne coïncident pas ponctuellement avec la limite).
