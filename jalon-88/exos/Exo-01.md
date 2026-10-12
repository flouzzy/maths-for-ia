# Exercice 1 : Indépendance et incompatibilité

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soient $A$ et $B$ deux événements tels que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.
Montrer que si $A$ et $B$ sont incompatibles (ou mutuellement exclusifs, c'est-à-dire $A \cap B = \emptyset$), alors ils ne peuvent pas être indépendants.

---
**Correction détaillée :**

1. **Définition de l'incompatibilité :**
Puisque $A$ et $B$ sont incompatibles, on a par définition $A \cap B = \emptyset$.
La probabilité de l'événement impossible étant nulle, on en déduit que :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0 $$

2. **Hypothèse par l'absurde (supposons l'indépendance) :**
Supposons, par l'absurde, que $A$ et $B$ soient des événements indépendants.
Par définition de l'indépendance, on devrait avoir :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \times \mathbb{P}(B) $$

3. **Évaluation de l'équation :**
En substituant l'égalité trouvée à l'étape 1, on obtient :
$$ 0 = \mathbb{P}(A) \times \mathbb{P}(B) $$
Puisque nous sommes dans l'ensemble des nombres réels, le produit de deux nombres est nul si et seulement si l'un des deux nombres est nul.
Cela implique que $\mathbb{P}(A) = 0$ ou $\mathbb{P}(B) = 0$.

4. **Conclusion :**
Cependant, l'énoncé stipule explicitement que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.
Nous aboutissons donc à une contradiction manifeste.
L'hypothèse initiale d'indépendance est donc fausse.
Par conséquent, deux événements de probabilités non nulles et incompatibles **ne peuvent jamais** être indépendants. $\blacksquare$
