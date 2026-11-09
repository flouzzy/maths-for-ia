---
uuid: "jalon-90-exo-01"
title: "Convergence presque sûre d'une variable binaire constante"
---

# Exercice 1 : Convergence presque sûre d'une variable binaire constante (Difficulté $\bigstar\star\star\star\star$)

Dans un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$, on considère une suite de variables aléatoires indépendantes $(X_n)_{n \ge 1}$ telles que pour tout $n$, $\mathbb{P}(X_n = 1) = 1/n^2$ et $\mathbb{P}(X_n = 0) = 1 - 1/n^2$.

1. Calculer la somme des probabilités $\sum_{n=1}^\infty \mathbb{P}(X_n = 1)$.
2. En déduire la limite de la suite $(X_n)$ presque sûrement à l'aide du lemme de Borel-Cantelli.

## Correction Pas-à-Pas

1. Calcul de la somme des probabilités :
   $$ \sum_{n=1}^\infty \mathbb{P}(X_n = 1) = \sum_{n=1}^\infty \frac{1}{n^2} $$
   On reconnaît la série de Riemann (problème de Bâle) convergente pour $p = 2 > 1$.
   $$ \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < +\infty $$

2. Puisque la série des probabilités $\sum \mathbb{P}(X_n = 1)$ converge, le premier lemme de Borel-Cantelli permet de conclure.
   Soit l'événement $A_n = \{X_n = 1\}$. Le lemme énonce que la probabilité que l'événement $A_n$ se produise une infinité de fois est nulle :
   $$ \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0 $$
   Cela signifie qu'avec une probabilité de $1$, seul un nombre fini d'événements $A_n$ se réalisent. Il existe donc un entier aléatoire $N(\omega)$ tel que pour tout $n \geq N(\omega)$, $\omega \notin A_n$.
   Ainsi, pour $n \geq N(\omega)$, on a $X_n(\omega) = 0$.
   La suite $(X_n(\omega))$ stationne donc à $0$ pour $n$ assez grand, ce qui implique que la limite est $0$.
   Par conséquent, la suite converge presque sûrement vers $0$ :
   $$ X_n \xrightarrow{p.s.} 0 $$
   $\blacksquare$

