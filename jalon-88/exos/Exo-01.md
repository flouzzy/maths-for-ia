# Exercice 1 : Indépendance et incompatibilité \quad $\bigstar\star\star\star\star$

**Énoncé :**

Soient $A$ et $B$ deux événements d'un espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$ tels que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$.
Montrer que si $A$ et $B$ sont incompatibles (i.e. disjoints, $A \cap B = \emptyset$), alors ils ne peuvent pas être indépendants.

**Correction Détaillée :**

1. Supposons par l'absurde que $A$ et $B$ sont à la fois incompatibles et indépendants.
2. Puisque $A$ et $B$ sont incompatibles, leur intersection est l'ensemble vide : $A \cap B = \emptyset$.
3. Par conséquent, la probabilité de leur intersection est nulle : $\mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0$.
4. D'autre part, puisque $A$ et $B$ sont indépendants, la probabilité de leur intersection est égale au produit de leurs probabilités : $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$.
5. En combinant les étapes 3 et 4, on obtient l'égalité : $\mathbb{P}(A) \cdot \mathbb{P}(B) = 0$.
6. Or, l'énoncé précise que $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$. Le produit de deux nombres strictement positifs est strictement positif, donc $\mathbb{P}(A) \cdot \mathbb{P}(B) > 0$.
7. Nous aboutissons à une contradiction manifeste : $0 > 0$.
8. L'hypothèse de départ est donc fausse. Des événements de probabilité non nulle ne peuvent pas être simultanément incompatibles et indépendants.
