---
uuid: "jalon-67-exo-01"
title: "Exercice 01 - Théorème de convergence monotone de base"
difficulty: "\bigstar\star\star\star\star"
---

# Exercice 01 - Théorème de convergence monotone de base

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $f$ une fonction mesurable positive. Démontrer que la suite de fonctions $f_n(x) = \min(f(x), n)$ converge vers $f$ presque partout, et vérifier que $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.

## Correction Détaillée

1. **Croissance :** Pour tout $x \in X$, $f_{n+1}(x) = \min(f(x), n+1) \ge \min(f(x), n) = f_n(x)$. La suite $(f_n)$ est donc bien croissante.
2. **Positivité et mesurabilité :** Comme $f \ge 0$, on a $f_n \ge 0$. Les $f_n$ sont mesurables comme minimum de fonctions mesurables.
3. **Convergence simple :** Pour tout $x \in X$, si $f(x)$ est finie, il existe un rang $N$ tel que $n \ge N \implies n \ge f(x)$. Alors pour $n \ge N$, $f_n(x) = f(x)$. Donc $f_n(x)$ converge vers $f(x)$. Si $f(x) = +\infty$, $f_n(x) = n \to +\infty$. Dans tous les cas, $f_n \to f$.
4. **Application du TCM :** Les conditions du Théorème de Convergence Monotone sont remplies. On en déduit immédiatement que $\lim_{n \to \infty} \int_X f_n d\mu = \int_X f d\mu$.
