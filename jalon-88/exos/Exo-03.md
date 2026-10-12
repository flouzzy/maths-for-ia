# Exercice 3 : Indépendance et complémentaire

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soient $A$ et $B$ deux événements indépendants dans un espace de probabilité $(\Omega, \mathcal{F}, \mathbb{P})$.
Démontrer rigoureusement que les événements $A$ et $B^c$ (le complémentaire de $B$) sont également indépendants.

---
**Correction détaillée :**

Pour prouver que $A$ et $B^c$ sont indépendants, nous devons montrer, par définition, que :
$$ \mathbb{P}(A \cap B^c) = \mathbb{P}(A) \times \mathbb{P}(B^c) $$

1. **Partition de l'événement $A$ :**
Les événements $B$ et $B^c$ forment une partition de l'univers $\Omega$, car $B \cup B^c = \Omega$ et $B \cap B^c = \emptyset$.
Par conséquent, on peut décomposer l'événement $A$ de la manière suivante :
$$ A = A \cap \Omega = A \cap (B \cup B^c) = (A \cap B) \cup (A \cap B^c) $$

2. **Additivité de la probabilité :**
Puisque $(A \cap B)$ et $(A \cap B^c)$ sont des sous-ensembles respectivement de $B$ et de $B^c$, et que $B$ et $B^c$ sont disjoints, les ensembles $(A \cap B)$ et $(A \cap B^c)$ sont également disjoints (leur intersection est vide).
D'après le troisième axiome de Kolmogorov (additivité dénombrable pour des événements disjoints), nous avons :
$$ \mathbb{P}(A) = \mathbb{P}((A \cap B) \cup (A \cap B^c)) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c) $$

3. **Isolement du terme d'intérêt :**
Réarrangeons cette équation pour isoler $\mathbb{P}(A \cap B^c)$ :
$$ \mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B) $$

4. **Utilisation de l'hypothèse d'indépendance de $A$ et $B$ :**
Par hypothèse, $A$ et $B$ sont indépendants, ce qui se traduit par $\mathbb{P}(A \cap B) = \mathbb{P}(A) \times \mathbb{P}(B)$. Substituons cette expression dans l'équation de l'étape 3 :
$$ \mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B) $$

5. **Factorisation et conclusion :**
En factorisant par $\mathbb{P}(A)$, on obtient :
$$ \mathbb{P}(A \cap B^c) = \mathbb{P}(A) \times (1 - \mathbb{P}(B)) $$
Or, par la loi du complémentaire, nous savons que $\mathbb{P}(B^c) = 1 - \mathbb{P}(B)$. En substituant ceci :
$$ \mathbb{P}(A \cap B^c) = \mathbb{P}(A) \times \mathbb{P}(B^c) $$
L'égalité est bien vérifiée. Les événements $A$ et $B^c$ sont donc indépendants. $\blacksquare$
