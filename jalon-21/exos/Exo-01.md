---
uuid: "exo-21-01"
title: "Exercice 1 : Convergence simple de x^n"
difficulty: 1
---

# Exercice 1 : Convergence simple de x^n

**Niveau :** $★☆☆☆☆$

## Problème

Étudier la convergence simple de $f_n(x) = x^n$ sur $[0,1]$.

## Démonstration et Solution (Zéro Ellipse)

Pour étudier la convergence simple de la suite de fonctions $f_n(x) = x^n$ sur le segment $[0,1]$, nous devons fixer un réel $x \in [0,1]$ arbitraire et étudier la limite de la suite numérique $(f_n(x))_{n \in \mathbb{N}}$.

Nous distinguons deux cas rigoureux :

**Cas 1 : $x \in [0, 1[$**
Si $x \in [0, 1[$, alors la valeur de $x$ est strictement inférieure à 1. La suite numérique $(x^n)_{n \in \mathbb{N}}$ est une suite géométrique de raison $q = x$. Puisque $0 \leq x < 1$, nous avons $|q| < 1$. D'après le théorème sur les limites des suites géométriques, si la raison appartient à l'intervalle ouvert $]-1, 1[$, la limite de $q^n$ lorsque $n$ tend vers l'infini est strictement égale à 0.
Ainsi, pour tout $x \in [0, 1[$, $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} x^n = 0$.

**Cas 2 : $x = 1$**
Si $x = 1$, alors pour tout entier naturel $n$, $f_n(1) = 1^n = 1$. La suite numérique considérée est donc la suite constante égale à 1. La limite d'une suite constante est sa valeur, donc :
$\lim_{n \to \infty} f_n(1) = 1$.

**Conclusion de l'étude de la convergence simple :**
La suite de fonctions $(f_n)$ converge simplement sur $[0,1]$ vers une fonction limite $f$ définie par :
$f(x) = 0$ si $x \in [0, 1[$
$f(x) = 1$ si $x = 1$
