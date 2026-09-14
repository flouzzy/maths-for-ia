## Exercice 8 : Le problème du produit infini non mesurable \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Montrer par un contre-exemple simple que l'union de deux rectangles mesurables n'est pas nécessairement un rectangle mesurable.

**Correction :**
1. Soit $X_1 = X_2 = \mathbb{R}$.
2. Considérons $R_1 = [0, 1] \times [0, 1]$ et $R_2 = [2, 3] \times [2, 3]$.
3. Supposons par l'absurde que $R_1 \cup R_2 = A \times B$.
4. Le point $(0, 0)$ appartient à $R_1$, donc à $A \times B$. Ainsi $0 \in A$ et $0 \in B$.
5. Le point $(2, 2)$ appartient à $R_2$, donc à $A \times B$. Ainsi $2 \in A$ et $2 \in B$.
6. Si $A \times B$ est un produit cartésien contenant $0$ et $2$ en $X$, et $0$ et $2$ en $Y$, il doit contenir le point $(0, 2)$.
7. Or $(0, 2)$ n'appartient ni à $R_1$ ni à $R_2$. C'est une contradiction.
8. L'ensemble des rectangles mesurables n'est pas stable par union, c'est pourquoi on doit considérer la tribu *engendrée* par ces rectangles.
