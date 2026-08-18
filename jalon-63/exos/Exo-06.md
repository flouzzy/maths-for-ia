---
uuid: "exo-jalon-63-06"
title: "Exercice 6 : L'ensemble de Cantor et la mesure de Lebesgue"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# L'ensemble de Cantor et la mesure de Lebesgue

## Énoncé

L'ensemble triadique de Cantor $\mathcal{C}$ est construit à partir du segment $C_0 = [0, 1]$. À chaque étape $n$, on retire le tiers central ouvert de chaque segment de l'étape précédente pour former $C_n$. Ainsi, $C_1 = [0, 1/3] \cup [2/3, 1]$, etc. L'ensemble de Cantor est défini par $\mathcal{C} = \bigcap_{n=0}^{+\infty} C_n$. On admet que la mesure de Lebesgue $\lambda$ d'un intervalle $[a, b]$ est $b-a$. Démontrer que la mesure de Lebesgue de l'ensemble de Cantor est nulle : $\lambda(\mathcal{C}) = 0$.

## Correction Détaillée

Observons la construction itérative :
- Étape $0$ : $C_0 = [0, 1]$. On a $\lambda(C_0) = 1$.
- Étape $1$ : $C_1$ est l'union de $2$ intervalles disjoints de longueur $1/3$. Sa mesure est $\lambda(C_1) = 2 \times \frac{1}{3} = \frac{2}{3}$.
- Étape $n$ : $C_n$ est constitué par une union disjointe de $2^n$ intervalles de longueur $(1/3)^n$. Par additivité finie de la mesure de Lebesgue sur les intervalles disjoints, on a :
  $$ \lambda(C_n) = 2^n \times \left( \frac{1}{3} \right)^n = \left( \frac{2}{3} \right)^n $$

La suite d'ensembles $(C_n)_{n \in \mathbb{N}}$ est strictement décroissante pour l'inclusion : $C_{n+1} \subset C_n$.
De plus, la mesure du premier terme est finie : $\lambda(C_0) = 1 < +\infty$.
Nous pouvons donc appliquer de plein droit le théorème de continuité décroissante de la mesure :
$$ \lambda(\mathcal{C}) = \lambda\left( \bigcap_{n=0}^{+\infty} C_n \right) = \lim_{n \to +\infty} \lambda(C_n) = \lim_{n \to +\infty} \left( \frac{2}{3} \right)^n $$
Puisque $0 < 2/3 < 1$, cette limite géométrique est nulle.
Ainsi, $\lambda(\mathcal{C}) = 0$.

*Remarque :* L'ensemble de Cantor est paradoxal ; il est non dénombrable (en bijection avec $\mathbb{R}$) tout en occupant un "volume" strictement nul sur la droite réelle. $\blacksquare$
