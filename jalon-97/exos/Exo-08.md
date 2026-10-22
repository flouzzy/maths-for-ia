# Exercice 8

**Difficulté :** $\star\star\star\star\☆$

**Énoncé :**
Soit $E = (\mathbb{R}^2, \|\cdot\|_1)$ où $\|(x,y)\|_1 = |x| + |y|$. Soit $T : E \to E$ l'application linéaire représentée matriciellement dans la base canonique par $A = \begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$. Calculer la norme d'opérateur $\|T\|_1$.

**Correction Détaillée :**
1. Pour la norme 1 sur $\mathbb{R}^n$, la norme d'opérateur d'une matrice $A$ correspond au maximum des normes 1 de ses vecteurs colonnes (la somme des valeurs absolues des éléments de chaque colonne). Démontrons-le.
2. Soit un vecteur unitaire $X = (x, y)$ tel que $\|X\|_1 = |x| + |y| = 1$.
3. Le vecteur image est $T(X) = (2x - y, 3x + 4y)$.
4. Évaluons sa norme 1 :
   $$ \|T(X)\|_1 = |2x - y| + |3x + 4y|. $$
5. Utilisons l'inégalité triangulaire :
   $$ \|T(X)\|_1 \le (|2x| + |-y|) + (|3x| + |4y|) = 2|x| + |y| + 3|x| + 4|y| = 5|x| + 5|y|. $$
6. En factorisant, $\|T(X)\|_1 \le 5(|x| + |y|) = 5 \|X\|_1 = 5$.
7. La norme de l'opérateur est donc au plus 5.
8. Pour voir si cette borne est atteinte, testons les vecteurs de la base canonique, qui sont de norme 1 :
   - $e_1 = (1, 0) \implies T(e_1) = (2, 3) \implies \|T(e_1)\|_1 = |2| + |3| = 5$.
   - $e_2 = (0, 1) \implies T(e_2) = (-1, 4) \implies \|T(e_2)\|_1 = |-1| + |4| = 5$.
9. La valeur 5 étant atteinte pour le vecteur $e_1$, le supremum est atteint.
10. La norme de l'opérateur est exactement $\|T\|_1 = 5$.
