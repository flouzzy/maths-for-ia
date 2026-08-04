---
title: "Exercice 5 : Différentiabilité et Gradient"
difficulty: "★★★☆☆"
---

# Exercice 5 : Différentielle de la fonction trace

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

L'espace $M_n(\mathbb{R})$ des matrices carrées d'ordre $n$ est identifié à $\mathbb{R}^{n^2}$. Soit l'application trace $\text{Tr} : M_n(\mathbb{R}) \to \mathbb{R}$ définie par $\text{Tr}(A) = \sum_{i=1}^n a_{ii}$. Montrer que $\text{Tr}$ est différentiable et déterminer sa différentielle.

---
## Correction Détaillée

L'espace $M_n(\mathbb{R})$ est un espace vectoriel de dimension finie $n^2$.
Soit $A \in M_n(\mathbb{R})$ et $H \in M_n(\mathbb{R})$ un accroissement (une matrice).

**1. Écriture de la différence :**
L'application $\text{Tr}$ est une forme linéaire sur $M_n(\mathbb{R})$.
En utilisant la linéarité de la trace, on a pour tout $H$ :
$$ \text{Tr}(A + H) = \text{Tr}(A) + \text{Tr}(H) $$

**2. Identification de la différentielle :**
La relation s'écrit sous la forme $f(A + H) = f(A) + L(H) + R(H)$ en posant :
- $L(H) = \text{Tr}(H)$ qui est une application linéaire par rapport à $H$.
- $R(H) = 0$ (le reste est identiquement nul).

Puisque le reste est nul, il vérifie trivialement $\lim_{H \to 0} \frac{\|R(H)\|}{\|H\|} = 0$.

**Conclusion :**
Toute application linéaire en dimension finie est différentiable en tout point, et sa différentielle en tout point est égale à elle-même.
Ainsi, l'application $\text{Tr}$ est différentiable en tout point $A \in M_n(\mathbb{R})$, et pour tout $H \in M_n(\mathbb{R})$ :
$$ d\text{Tr}_A(H) = \text{Tr}(H) $$
