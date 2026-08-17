---
title: "Exercice 1 - Analyse de la fonction de Dirichlet"
difficulty: $\bigstar\star\star\star\star$
---

# Exercice 1 - Analyse de la fonction de Dirichlet

**Énoncé :**
Soit $f : [0, 1] \to \mathbb{R}$ la fonction de Dirichlet définie par $f(x) = 1$ si $x \in \mathbb{Q}$ et $0$ sinon. Soit $\sigma = (x_0, x_1, \dots, x_n)$ une subdivision de $[0, 1]$. Démontrer rigoureusement que les sommes de Darboux inférieure et supérieure ne convergent pas.

**Démonstration pas à pas :**
1. Considérons un intervalle quelconque $[x_{k-1}, x_k]$ de la subdivision, avec $x_{k-1} < x_k$.
2. Par la densité de $\mathbb{Q}$ dans $\mathbb{R}$, il existe un rationnel $q \in [x_{k-1}, x_k]$. Ainsi, $\sup_{t \in [x_{k-1}, x_k]} f(t) = 1$.
3. Par la densité de $\mathbb{R} \setminus \mathbb{Q}$ dans $\mathbb{R}$, il existe un irrationnel $p \in [x_{k-1}, x_k]$. Ainsi, $\inf_{t \in [x_{k-1}, x_k]} f(t) = 0$.
4. La somme supérieure est $S(f, \sigma) = \sum_{k=1}^n 1 \cdot (x_k - x_{k-1}) = 1$.
5. La somme inférieure est $s(f, \sigma) = \sum_{k=1}^n 0 \cdot (x_k - x_{k-1}) = 0$.
6. L'intégrale supérieure vaut $\inf S = 1$ et l'intégrale inférieure vaut $\sup s = 0$. Comme elles sont différentes, $f$ n'est pas Riemann-intégrable.
