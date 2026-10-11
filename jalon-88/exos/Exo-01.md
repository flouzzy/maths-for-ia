# Exercice 1

\subsection*{Exercice 1 : Indépendance et incompatibilité \quad $\bigstar\star\star\star\star$}

**Énoncé :**
Soit $(\Omega, \mathcal{F}, P)$ un espace probabilisé. Soient $A$ et $B$ deux événements tels que $P(A) > 0$ et $P(B) > 0$.
Montrer que $A$ et $B$ ne peuvent pas être à la fois indépendants et incompatibles (disjoints).

**Correction :**
1. Supposons par l'absurde que $A$ et $B$ sont à la fois indépendants et incompatibles.
2. Puisque $A$ et $B$ sont incompatibles, leur intersection est vide : $A \cap B = \emptyset$.
3. La probabilité de l'ensemble vide est nulle, donc $P(A \cap B) = 0$.
4. Puisque $A$ et $B$ sont indépendants, par définition, $P(A \cap B) = P(A)P(B)$.
5. En combinant (3) et (4), on obtient $P(A)P(B) = 0$.
6. Or, par hypothèse, $P(A) > 0$ et $P(B) > 0$, donc leur produit est strictement positif : $P(A)P(B) > 0$.
7. On aboutit à une contradiction manifeste : $0 > 0$.
8. L'hypothèse de départ est fausse. $A$ et $B$ ne peuvent donc pas être à la fois indépendants et incompatibles.
