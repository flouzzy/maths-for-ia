---
title: "Exercice 10 : Croissance non stricte et Lebesgue"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Croissance non stricte et Lebesgue

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $(f_n)$ une suite de fonctions mesurables positives de $[0, 1]$ dans $\mathbb{R}$. On ne suppose plus que $f_n(x) \le f_{n+1}(x)$, mais on définit $g_n(x) = \sup_{1 \le k \le n} f_k(x)$ et $h(x) = \sup_{n \ge 1} f_n(x)$. Montrer rigoureusement que $\int_0^1 h(x) dx = \lim_{n \to \infty} \int_0^1 g_n(x) dx$.

## Correction Détaillée

1. Analysons la fonction $g_n$. Pour tout $x$, $g_n(x)$ est le maximum de $n$ fonctions évaluées en $x$.
   Comme le supremum fini de fonctions mesurables est mesurable, $g_n$ est mesurable.
   De plus, comme $f_k \ge 0$, on a $g_n \ge 0$.
2. Étudions la monotonie de la suite $(g_n)$.
   $g_{n+1}(x) = \sup_{1 \le k \le n+1} f_k(x) = \max( \sup_{1 \le k \le n} f_k(x), f_{n+1}(x) ) = \max(g_n(x), f_{n+1}(x))$.
   Donc, pour tout $x$, $g_{n+1}(x) \ge g_n(x)$.
   La suite de fonctions $(g_n)$ est **croissante**.
3. Déterminons la limite de $g_n(x)$.
   Par définition, $h(x) = \sup_{n \ge 1} f_n(x)$.
   Puisque $g_n(x)$ est une suite numérique croissante, elle converge vers son supremum sur $n$.
   Donc $\lim_{n \to \infty} g_n(x) = \sup_{n \ge 1} g_n(x) = \sup_{n \ge 1} \left( \sup_{1 \le k \le n} f_k(x) \right) = \sup_{k \ge 1} f_k(x) = h(x)$.
4. Nous avons maintenant une suite de fonctions $(g_n)$ qui est mesurable, positive, **croissante** et qui converge simplement vers $h$.
5. Nous sommes exactement dans les hypothèses du théorème de Beppo Levi (Convergence Monotone).
6. Par application directe du théorème :
   $$\int_0^1 \left( \lim_{n \to \infty} g_n(x) \right) dx = \lim_{n \to \infty} \int_0^1 g_n(x) dx$$
   Ce qui donne :
   $$\int_0^1 h(x) dx = \lim_{n \to \infty} \int_0^1 g_n(x) dx$$
7. Cet exercice illustre une technique puissante : on peut toujours transformer une suite quelconque $(f_n)$ en une suite croissante $(g_n)$ en prenant le supremum partiel. Cela permet d'appliquer Beppo Levi à la nouvelle suite, et sert notamment d'étape préliminaire pour démontrer le Lemme de Fatou.
