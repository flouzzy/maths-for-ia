---
title: "Exercice 4 - Limite d'indicatrices finies"
difficulty: $\bigstar\bigstar\star\star\star$
---

# Exercice 4 - Limite d'indicatrices finies

**Énoncé :**
Soit $(q_n)_{n \ge 1}$ une énumération des rationnels de $[0, 1]$. Posons $f_n = 1_{\{q_1, \dots, q_n\}}$. Montrer que $f_n \to f$ (Dirichlet) simplement, que chaque $f_n$ est Riemann-intégrable d'intégrale 0, mais que $f$ n'est pas intégrable.

**Démonstration pas à pas :**
1. D'après l'Exercice 3, $f_n$ est l'indicatrice d'un ensemble fini, elle est donc Riemann-intégrable et $\int_0^1 f_n = 0$.
2. Soit $x \in [0, 1]$. Si $x \in \mathbb{Q}$, alors il existe $N$ tel que $x = q_N$. Pour $n \ge N$, $f_n(x) = 1$. Donc $\lim_{n} f_n(x) = 1$.
3. Si $x \notin \mathbb{Q}$, pour tout $n$, $f_n(x) = 0$. Donc $\lim_{n} f_n(x) = 0$.
4. La limite simple est bien $f$, la fonction de Dirichlet.
5. On a vu (Exercice 1) que $f$ n'est pas Riemann-intégrable. Cela illustre l'échec du passage à la limite sous l'intégrale de Riemann sans convergence uniforme.
