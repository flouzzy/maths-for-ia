# Exercice 2 : Indépendance avec l'événement certain et impossible

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soit $A \in \mathcal{F}$ un événement quelconque.
1. Démontrer que $A$ est indépendant de l'événement certain $\Omega$.
2. Démontrer que $A$ est indépendant de l'événement impossible $\emptyset$.
3. Montrer qu'un événement $A$ est indépendant de lui-même si et seulement si $\mathbb{P}(A) = 0$ ou $\mathbb{P}(A) = 1$.

---
**Correction détaillée :**

**Question 1 : Indépendance avec $\Omega$**
1. L'intersection d'un ensemble quelconque avec l'espace entier $\Omega$ est l'ensemble lui-même : $A \cap \Omega = A$.
2. En appliquant la mesure de probabilité : $\mathbb{P}(A \cap \Omega) = \mathbb{P}(A)$.
3. Par ailleurs, par axiome des probabilités, $\mathbb{P}(\Omega) = 1$.
4. Donc, $\mathbb{P}(A) \times \mathbb{P}(\Omega) = \mathbb{P}(A) \times 1 = \mathbb{P}(A)$.
5. Nous avons bien l'égalité $\mathbb{P}(A \cap \Omega) = \mathbb{P}(A) \times \mathbb{P}(\Omega)$, ce qui prouve l'indépendance.

**Question 2 : Indépendance avec $\emptyset$**
1. L'intersection d'un ensemble quelconque avec l'ensemble vide est l'ensemble vide : $A \cap \emptyset = \emptyset$.
2. En appliquant la mesure de probabilité : $\mathbb{P}(A \cap \emptyset) = \mathbb{P}(\emptyset) = 0$.
3. Par ailleurs, par axiome des probabilités, $\mathbb{P}(\emptyset) = 0$.
4. Donc, $\mathbb{P}(A) \times \mathbb{P}(\emptyset) = \mathbb{P}(A) \times 0 = 0$.
5. L'égalité $\mathbb{P}(A \cap \emptyset) = \mathbb{P}(A) \times \mathbb{P}(\emptyset)$ est vérifiée, prouvant l'indépendance.

**Question 3 : Indépendance d'un événement avec lui-même**
1. Supposons que $A$ soit indépendant de lui-même. Par définition, cela signifie :
$$ \mathbb{P}(A \cap A) = \mathbb{P}(A) \times \mathbb{P}(A) $$
2. Or, l'intersection d'un ensemble avec lui-même est lui-même : $A \cap A = A$. L'équation devient donc :
$$ \mathbb{P}(A) = (\mathbb{P}(A))^2 $$
3. Posons $x = \mathbb{P}(A)$. L'équation polynomiale du second degré est $x = x^2$, soit $x^2 - x = 0$.
4. En factorisant, on obtient $x(x - 1) = 0$.
5. Les seules solutions réelles sont $x = 0$ et $x = 1$.
6. Ainsi, $A$ est indépendant de lui-même si et seulement si $\mathbb{P}(A) = 0$ ou $\mathbb{P}(A) = 1$ (c'est-à-dire si $A$ est un événement presque impossible ou presque certain). $\blacksquare$
