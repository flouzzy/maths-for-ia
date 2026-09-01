---
title: "Exercice 3 : Limite d'une suite d'intégrales avec un supremum"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 3 : Limite d'une suite d'intégrales avec un supremum

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $f : \mathbb{R} \to \mathbb{R}_+$ une fonction mesurable. Montrer que $\lim_{n \to \infty} \int_{\mathbb{R}} f(x) e^{-x^2/n} dx = \int_{\mathbb{R}} f(x) dx$.

## Correction Détaillée

1. Posons $f_n(x) = f(x) e^{-x^2/n}$.
2. Les fonctions $f_n$ sont mesurables sur $\mathbb{R}$, car produit de fonctions mesurables.
3. Puisque $f \ge 0$ et $e^{-x^2/n} > 0$, chaque $f_n$ est positive sur $\mathbb{R}$.
4. Étudions la monotonie de la suite $(f_n)_{n \in \mathbb{N}^*}$ :
   Pour un $x \in \mathbb{R}$ fixé, la suite $n \mapsto -x^2/n$ est croissante (elle part de valeurs négatives et tend vers $0$).
   L'exponentielle étant une fonction croissante, la suite $n \mapsto e^{-x^2/n}$ est croissante.
   Comme $f(x) \ge 0$, la suite $f_n(x) = f(x)e^{-x^2/n}$ est croissante.
5. Déterminons la limite ponctuelle :
   Pour tout $x \in \mathbb{R}$, $\lim_{n \to \infty} -x^2/n = 0$, donc $\lim_{n \to \infty} e^{-x^2/n} = 1$.
   Par conséquent, $\lim_{n \to \infty} f_n(x) = f(x)$.
6. Toutes les hypothèses du théorème de convergence monotone (Beppo Levi) sont vérifiées : suite de fonctions mesurables, positives, et croissante partout vers $f$.
7. On peut donc conclure que :
   $$\lim_{n \to \infty} \int_{\mathbb{R}} f_n(x) dx = \int_{\mathbb{R}} \left( \lim_{n \to \infty} f_n(x) \right) dx = \int_{\mathbb{R}} f(x) dx$$
