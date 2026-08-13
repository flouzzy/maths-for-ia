# Exercice 1 : Convergence simple vs uniforme

## Énoncé
Soit $f_n(x) = \frac{nx}{1 + n^2x^2}$ sur $[0, 1]$.
1. Déterminer la limite simple $f$ de la suite de fonctions $(f_n)_{n \in \mathbb{N}}$.
2. La convergence est-elle uniforme sur $[0, 1]$ ? Justifier rigoureusement.

## Correction Détaillée

1. **Limite simple :**
Pour $x = 0$, $f_n(0) = 0 \to 0$.
Pour $x \in ]0, 1]$, on a $f_n(x) = \frac{nx}{n^2x^2(1/(n^2x^2) + 1)} \sim \frac{nx}{n^2x^2} = \frac{1}{nx}$.
Donc $\lim_{n \to +\infty} f_n(x) = 0$.
Ainsi, la suite $(f_n)$ converge simplement vers la fonction nulle $f=0$ sur $[0, 1]$.

2. **Convergence uniforme :**
Calculons la dérivée pour trouver le maximum :
$$f_n'(x) = \frac{n(1+n^2x^2) - nx(2n^2x)}{(1+n^2x^2)^2} = \frac{n - n^3x^2}{(1+n^2x^2)^2}$$
$f_n'(x) = 0 \iff 1 - n^2x^2 = 0 \iff x = \frac{1}{n}$.
La fonction $f_n$ atteint son maximum en $x_n = \frac{1}{n}$.
On calcule $f_n(x_n) = \frac{n(1/n)}{1 + n^2(1/n^2)} = \frac{1}{1+1} = \frac{1}{2}$.
Ainsi, $\sup_{x \in [0, 1]} |f_n(x) - f(x)| = \frac{1}{2}$, qui ne tend pas vers 0 lorsque $n \to +\infty$.
La convergence n'est donc **pas uniforme** sur $[0, 1]$.
