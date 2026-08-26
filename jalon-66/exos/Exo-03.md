---
title: "Exercice 03 : La mesure de Dirac"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 03 : La mesure de Dirac

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soit $\mathbb{R}$ muni de sa tribu borélienne. Soit $\delta_a$ la mesure de Dirac au point $a \in \mathbb{R}$, définie par $\delta_a(A) = 1$ si $a \in A$, et $0$ sinon.
Soit $f : \mathbb{R} \to [0, +\infty]$ une fonction mesurable positive quelconque.
Démontrez que $\int_{\mathbb{R}} f \, d\delta_a = f(a)$.

### Correction détaillée

1. Supposons d'abord que $f$ est une fonction simple, $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$, où les $A_i$ forment une partition de $\mathbb{R}$.
2. Le point $a$ appartient nécessairement à un et un seul des sous-ensembles de la partition, disons $A_{i_0}$.
3. Par définition de la mesure de Dirac :
   $\delta_a(A_{i_0}) = 1$ et $\delta_a(A_i) = 0$ pour tout $i \neq i_0$.
4. L'intégrale de $s$ est :
   $$ \int_{\mathbb{R}} s \, d\delta_a = \sum_{i=1}^n \alpha_i \delta_a(A_i) = \alpha_{i_0} \cdot 1 = \alpha_{i_0} $$
   Or, puisque $a \in A_{i_0}$, la valeur de $s(a)$ est précisément $\alpha_{i_0}$. Donc $\int_{\mathbb{R}} s \, d\delta_a = s(a)$.
5. Passons au cas général où $f$ est une fonction mesurable positive.
   Par définition, $\int_{\mathbb{R}} f \, d\delta_a = \sup \left\lbrace \int_{\mathbb{R}} s \, d\delta_a \mid s \in \mathcal{E}_+, 0 \le s \le f \right\rbrace$.
6. D'après ce qui précède, cela devient :
   $$ \int_{\mathbb{R}} f \, d\delta_a = \sup \{ s(a) \mid s \in \mathcal{E}_+, 0 \le s \le f \} $$
7. Soit $\alpha$ un réel tel que $\alpha < f(a)$. On peut définir une fonction simple $s = \alpha \mathbf{1}_{\{a\}}$.
   Clairement $0 \le s \le f$ partout (car $s(x)=0 \le f(x)$ si $x \neq a$, et $s(a) = \alpha \le f(a)$).
   Pour cette fonction, $s(a) = \alpha$.
   Ainsi, le supremum des $s(a)$ atteint exactement $f(a)$.
   Donc $\int_{\mathbb{R}} f \, d\delta_a = f(a)$.
