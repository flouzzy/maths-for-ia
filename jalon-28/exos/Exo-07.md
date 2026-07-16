---
title: "Exercice 7 : Endomorphisme nilpotent et trace"
difficulty: 4
---

# Exercice 7 : Endomorphisme nilpotent et trace (★★★★☆)

## Énoncé

Soit $E$ un espace vectoriel complexe de dimension finie $n$. Soit $u \in \mathcal{L}(E)$.
On rappelle que $u$ est nilpotent s'il existe un entier $k \ge 1$ tel que $u^k = 0_{\mathcal{L}(E)}$.
1. Montrer que si $u$ est nilpotent, alors son unique valeur propre est 0.
2. En déduire le polynôme caractéristique d'un endomorphisme nilpotent.
3. Montrer que $\text{Tr}(u) = 0$.
4. (Réciproque) Supposons que pour tout $k \in \{1, 2, \dots, n\}$, $\text{Tr}(u^k) = 0$. Montrer que $u$ est nilpotent.

## Solution Rigoureuse

### 1. Unique valeur propre d'un nilpotent
Soit $\lambda \in \mathbb{C}$ une valeur propre de $u$, et $x \in E \setminus \{0_E\}$ un vecteur propre associé, de sorte que $u(x) = \lambda x$.
Par une récurrence immédiate, pour tout entier $m \ge 1$, on a $u^m(x) = \lambda^m x$.
L'endomorphisme $u$ étant nilpotent, il existe $k \ge 1$ tel que $u^k = 0_{\mathcal{L}(E)}$.
En appliquant cette propriété au vecteur $x$ :
$$u^k(x) = \lambda^k x$$
$$0_E = \lambda^k x$$
Comme $x \neq 0_E$, il en découle nécessairement que la quantité scalaire $\lambda^k = 0$.
Dans le corps $\mathbb{C}$ (intègre), cela implique $\lambda = 0$.
La seule valeur propre possible pour un endomorphisme nilpotent est donc $0$.

### 2. Polynôme caractéristique
Sur le corps $\mathbb{C}$ algébriquement clos, tout polynôme caractéristique est scindé.
Le polynôme caractéristique $\chi_u(X)$ de l'endomorphisme $u$ (qui est de degré $n$) s'écrit alors sous la forme :
$$\chi_u(X) = \prod_{i=1}^n (X - \lambda_i)$$
où les $\lambda_i$ sont les racines de $\chi_u$, c'est-à-dire les valeurs propres de $u$, comptées avec multiplicité.
Or, nous avons établi à la question précédente que la seule valeur propre est 0. Donc pour tout $i$, $\lambda_i = 0$.
Par substitution directe, le polynôme caractéristique est :
$$\chi_u(X) = \prod_{i=1}^n (X - 0) = X^n$$

### 3. Nullité de la trace
La trace d'un endomorphisme (ou de toute matrice la représentant) est égale, de façon invariante, à la somme de ses valeurs propres comptées avec multiplicité (au signe près, c'est le coefficient de $X^{n-1}$ dans $\chi_u$).
$$\text{Tr}(u) = \sum_{i=1}^n \lambda_i = \sum_{i=1}^n 0 = 0$$

### 4. Réciproque (Identités de Newton)
Supposons que pour tout $k \in \{1, \dots, n\}$, $\text{Tr}(u^k) = 0$.
Nous sommes dans un espace complexe, donc le polynôme caractéristique $\chi_u$ est scindé de racines $\lambda_1, \dots, \lambda_n$.
La matrice représentative $M$ de $u$ est trigonalisable dans $\mathbb{C}$. Les éléments diagonaux de la matrice triangulaire sont les valeurs propres $\lambda_1, \dots, \lambda_n$.
La matrice $M^k$ est également triangulaire supérieure, et ses éléments diagonaux sont $\lambda_1^k, \dots, \lambda_n^k$.
Par conséquent, la condition $\text{Tr}(u^k) = 0$ se traduit par le système d'équations (sommes de Newton) :
$$\sum_{i=1}^n \lambda_i^k = 0 \quad \text{pour tout } k \in \{1, \dots, n\}$$
Les formules de Newton (liant les fonctions symétriques élémentaires aux sommes de puissances) permettent d'exprimer les coefficients du polynôme caractéristique en fonction de ces sommes.
Soit $\sigma_k$ la $k$-ème fonction symétrique élémentaire des racines. Les relations s'écrivent :
$$k \sigma_k = S_k - \sigma_1 S_{k-1} + \sigma_2 S_{k-2} - \dots + (-1)^{k-1} \sigma_{k-1} S_1$$
où $S_k = \sum \lambda_i^k$.
Puisque $S_1 = S_2 = \dots = S_n = 0$, on obtient par récurrence sur $k$ (de 1 à $n$) :
- $1 \sigma_1 = S_1 = 0 \implies \sigma_1 = 0$
- $2 \sigma_2 = S_2 - \sigma_1 S_1 = 0 - 0 = 0 \implies \sigma_2 = 0$
- ...
- $n \sigma_n = 0 \implies \sigma_n = 0$

Ainsi, toutes les fonctions symétriques élémentaires des racines sont nulles.
Or, le polynôme caractéristique s'écrit $\chi_u(X) = X^n - \sigma_1 X^{n-1} + \sigma_2 X^{n-2} + \dots + (-1)^n \sigma_n$.
Donc $\chi_u(X) = X^n$.
D'après le théorème de Cayley-Hamilton, $\chi_u(u) = 0_{\mathcal{L}(E)}$.
Donc $u^n = 0_{\mathcal{L}(E)}$.
Ceci démontre par définition que $u$ est nilpotent d'indice au plus $n$. $\blacksquare$
