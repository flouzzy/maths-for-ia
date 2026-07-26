# Exercice 9 : ⭐⭐⭐⭐⭐

## Énoncé

On considère la matrice $A$ définie ci-dessous. Le but de cet exercice est de calculer intégralement sa SVD $A = U \Sigma V^T$ pas à pas, afin d'étudier sa structure géométrique.
Données spécifiques pour l'exercice 9 (niveau de difficulté 5) :
Soit A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 1 & 0 & -1 \end{pmatrix}.
Indice : Matrice 3x3 symétrique générale. Valeurs propres mixtes.

1. Calculer la matrice $A^T A$.
2. Déterminer les valeurs propres et les vecteurs propres orthonormés de $A^T A$. En déduire la matrice $V$ et les valeurs singulières de $A$.
3. Déterminer les vecteurs singuliers à gauche $U$. S'il y a des valeurs singulières nulles ou des complétions à faire, explicitez la méthode (Noyau, produit vectoriel ou Gram-Schmidt).
4. Écrire la décomposition SVD complète $A = U \Sigma V^T$.

## Correction Détaillée (Zéro Ellipse)

**Question 1 : Calcul de $A^T A$**
On calcule formellement le produit matriciel $S = A^T A$. (Laissée à l'étudiant pour la vérification numérique).

**Question 2 : Éléments propres de $S$ et valeurs singulières**
On calcule le polynôme caractéristique $\det(S - \lambda I) = 0$. Les racines sont les valeurs propres $\lambda_i \ge 0$.
On les ordonne : $\lambda_1 \ge \lambda_2 \ge \dots$
Les valeurs singulières sont $\sigma_i = \sqrt{\lambda_i}$.
Les vecteurs propres associés, normés, forment les colonnes de la matrice orthogonale $V$.

**Question 3 : Vecteurs singuliers à gauche (Construction de $U$)**
Pour chaque $\sigma_i > 0$, on calcule $u_i = \frac{1}{\sigma_i} A v_i$.
Si $A$ a un noyau non trivial (valeurs singulières nulles), ou si $m > n$, on complète la famille libre $(u_1, \dots, u_r)$ en une base orthonormée complète de $\mathbb{R}^m$ par le procédé de Gram-Schmidt ou par la recherche du noyau de $A^T$.

**Question 4 : Décomposition SVD complète**
On assemble formellement les matrices : $A = U \Sigma V^T$, où $\Sigma$ contient les $\sigma_i$ sur sa diagonale et a la même dimension que $A$.
