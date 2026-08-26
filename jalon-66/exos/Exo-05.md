---
title: "Exercice 05 : Invariance par translation de la mesure de Lebesgue"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 05 : Invariance par translation de la mesure de Lebesgue

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

On se place sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Pour $t \in \mathbb{R}$, on définit l'opérateur de translation $T_t(x) = x - t$.
Soit $f \in \mathcal{M}_+$. Montrer que $\int_{\mathbb{R}} f(x - t) \, d\lambda(x) = \int_{\mathbb{R}} f(x) \, d\lambda(x)$.
On assumera connue l'invariance par translation de la mesure de Lebesgue : $\lambda(A + t) = \lambda(A)$ pour tout borélien $A$.

### Correction détaillée

1. **Cas des fonctions indicatrices :** Soit $f = \mathbf{1}_A$ avec $A$ un borélien.
   La fonction translatée est $g(x) = f(x - t) = \mathbf{1}_A(x - t)$.
   Or $x - t \in A \iff x \in A + t$. Donc $g = \mathbf{1}_{A+t}$.
   L'intégrale est $\int g \, d\lambda = \lambda(A+t)$.
   Par invariance de la mesure, $\lambda(A+t) = \lambda(A) = \int f \, d\lambda$.
2. **Cas des fonctions étagées positives :** Soit $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$.
   Par linéarité immédiate pour les fonctions étagées, $s(x - t) = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i+t}(x)$.
   Son intégrale est $\sum \alpha_i \lambda(A_i+t) = \sum \alpha_i \lambda(A_i) = \int s \, d\lambda$.
3. **Cas d'une fonction mesurable positive :** Soit $f \in \mathcal{M}_+$.
   L'intégrale de la translatée $f_t(x) = f(x-t)$ est :
   $$ \int f_t \, d\lambda = \sup \left\lbrace \int s \, d\lambda \mid s \in \mathcal{E}_+, 0 \le s \le f_t \right\rbrace $$
   On remarque la bijection : $0 \le s(x) \le f(x-t) \iff 0 \le s(x+t) \le f(x)$.
   Si $s \in \mathcal{E}_+$ minore $f_t$, alors $\tilde{s}(x) = s(x+t)$ est dans $\mathcal{E}_+$ et minore $f$.
   De plus, par l'étape 2, $\int s \, d\lambda = \int \tilde{s} \, d\lambda$.
   Le passage au supremum se fait donc sur des ensembles de valeurs identiques.
   On conclut rigoureusement que $\int f(x-t) \, d\lambda(x) = \int f(x) \, d\lambda(x)$.
