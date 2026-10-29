# Exercice 10 : Opérateur de Shift

## Énoncé

Soit $S$ l'opérateur de shift à droite sur $\ell^2(\mathbb{Z})$ défini par $S((x_n)) = (x_{n-1})$. Montrer que c'est un opérateur unitaire.

*Niveau de difficulté :* $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Correction

1. **Définition unitaire :** Un opérateur $S$ sur un Hilbert est unitaire s'il est surjectif et préserve le produit scalaire (isométrie).
2. **Isométrie :** Calculons $\langle Sx, Sy \rangle$. Par définition, $(Sx)_n = x_{n-1}$. Donc $\langle Sx, Sy \rangle = \sum_{n=-\infty}^\infty x_{n-1} \overline{y_{n-1}}$.
3. **Changement d'indice :** Posons $k = n-1$. La somme devient $\sum_{k=-\infty}^\infty x_k \overline{y_k} = \langle x, y \rangle$. L'opérateur préserve donc le produit scalaire et la norme.
4. **Surjectivité :** Pour tout $y \in \ell^2$, il existe $x \in \ell^2$ tel que $Sx = y$. Il suffit de poser $x_n = y_{n+1}$.
5. **Conclusion :** L'opérateur $S$ est isométrique et bijectif, c'est donc un automorphisme isométrique de l'espace de Hilbert $\ell^2(\mathbb{Z})$, c'est-à-dire un opérateur unitaire.
