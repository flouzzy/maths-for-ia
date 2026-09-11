---
title: "Exercice 1 : TCM"
difficulty: "★☆☆☆☆"
---
# Exercice 1 : Calcul de limite simple d'une intégrale

**Niveau :** $\bigstar\star\star\star\star$

**Énoncé :**
On pose pour $n \ge 1$ et $x \in ]0, 1[$, $f_n(x) = x^{1/n}$. Montrer que la limite $\lim_{n \to \infty} \int_0^1 f_n(x) dx$ existe et la calculer.

**Correction détaillée :**
1. Posons $f_n(x) = x^{1/n}$ sur $]0, 1[$. Comme $x < 1$ et que la fonction $t \mapsto x^t$ est décroissante, pour $n \le n+1 \implies 1/n \ge 1/(n+1) \implies x^{1/n} \le x^{1/(n+1)}$. Ainsi la suite $(f_n)$ est croissante.
2. La limite simple de $f_n(x)$ est $f(x) = \lim x^{1/n} = x^0 = 1$ pour tout $x \in ]0, 1[$.
3. Par le théorème de convergence monotone, $\lim_{n \to \infty} \int_0^1 x^{1/n} dx = \int_0^1 \lim_{n \to \infty} x^{1/n} dx = \int_0^1 1 dx = 1$.
4. On peut vérifier par le calcul direct : $\int_0^1 x^{1/n} dx = \left[\frac{x^{1/n + 1}}{1/n + 1}\right]_0^1 = \frac{1}{1/n + 1} = \frac{n}{n+1}$, dont la limite quand $n \to \infty$ est bien 1.
