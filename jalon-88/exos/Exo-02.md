# Exercice 2 : Indépendance avec l'événement certain et impossible \quad $\bigstar\star\star\star\star$

**Énoncé :**

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé et $A \in \mathcal{F}$ un événement quelconque.
1. Montrer que $A$ et l'événement certain $\Omega$ sont indépendants.
2. Montrer que $A$ et l'événement impossible $\emptyset$ sont indépendants.

**Correction Détaillée :**

1. **Pour l'événement certain $\Omega$ :**
   - Calculons l'intersection : $A \cap \Omega = A$, puisque $A \subset \Omega$.
   - Donc $\mathbb{P}(A \cap \Omega) = \mathbb{P}(A)$.
   - Par ailleurs, par les axiomes de Kolmogorov, $\mathbb{P}(\Omega) = 1$.
   - Calculons le produit : $\mathbb{P}(A) \cdot \mathbb{P}(\Omega) = \mathbb{P}(A) \cdot 1 = \mathbb{P}(A)$.
   - Ainsi, $\mathbb{P}(A \cap \Omega) = \mathbb{P}(A) \cdot \mathbb{P}(\Omega)$, ce qui prouve l'indépendance de $A$ et $\Omega$.
2. **Pour l'événement impossible $\emptyset$ :**
   - Calculons l'intersection : $A \cap \emptyset = \emptyset$.
   - Donc $\mathbb{P}(A \cap \emptyset) = \mathbb{P}(\emptyset) = 0$.
   - Par ailleurs, $\mathbb{P}(\emptyset) = 0$.
   - Calculons le produit : $\mathbb{P}(A) \cdot \mathbb{P}(\emptyset) = \mathbb{P}(A) \cdot 0 = 0$.
   - Ainsi, $\mathbb{P}(A \cap \emptyset) = \mathbb{P}(A) \cdot \mathbb{P}(\emptyset)$, ce qui prouve l'indépendance de $A$ et $\emptyset$.
