\subsection*{Exercice 1 : Indépendance et événements incompatibles \quad $\bigstar\star\star\star\star$}

Soient $A$ et $B$ deux événements de probabilités strictement positives. Montrer que si $A$ et $B$ sont incompatibles, alors ils ne peuvent pas être indépendants.

**Correction :**
1. L'incompatibilité de $A$ et $B$ signifie que $A \cap B = \emptyset$.
2. Par conséquent, $\mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0$.
3. Supposons par l'absurde que $A$ et $B$ soient indépendants.
4. Alors $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$.
5. Puisque $\mathbb{P}(A) > 0$ et $\mathbb{P}(B) > 0$, le produit $\mathbb{P}(A)\mathbb{P}(B) > 0$.
6. On aboutit à une contradiction : $0 > 0$.
7. Donc $A$ et $B$ ne sont pas indépendants.