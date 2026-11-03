# Exercice 4 : Adjoint de l'opérateur de décalage bilatéral $\bigstar\bigstar\star\star\star$
## Énoncé
Soit $\ell^2(\mathbb{Z})$ l'espace de Hilbert des suites bilatérales complexes de carré sommable, muni du produit scalaire :
$$ \langle x, y \rangle = \sum_{n=-\infty}^{+\infty} x_n \overline{y_n} $$
On définit l'opérateur de décalage bilatéral à droite (Right Shift) $S : \ell^2(\mathbb{Z}) \to \ell^2(\mathbb{Z})$ par :
$$ (Sx)_n = x_{n-1} $$
1. Montrer que $S$ est une isométrie (et donc un opérateur continu).
2. Déterminer l'adjoint $S^*$ de $S$. L'opérateur $S$ est-il unitaire ?

## Correction
1. Soit $x \in \ell^2(\mathbb{Z})$. Calculons la norme au carré de $Sx$ :
$$ \|Sx\|^2 = \sum_{n=-\infty}^{+\infty} |(Sx)_n|^2 = \sum_{n=-\infty}^{+\infty} |x_{n-1}|^2 $$
En effectuant le changement de variable (ou décalage d'indice) $k = n - 1$, la somme parcourant tous les entiers relatifs reste invariante :
$$ = \sum_{k=-\infty}^{+\infty} |x_k|^2 = \|x\|^2 $$
On a donc $\|Sx\| = \|x\|$ pour tout $x$. L'opérateur $S$ préserve la norme, c'est une isométrie, et sa norme d'opérateur est exactement 1 (il est continu).

2. Pour déterminer l'adjoint, calculons le produit scalaire $\langle Sx, y \rangle$ pour $x, y \in \ell^2(\mathbb{Z})$ :
$$ \langle Sx, y \rangle = \sum_{n=-\infty}^{+\infty} (Sx)_n \overline{y_n} = \sum_{n=-\infty}^{+\infty} x_{n-1} \overline{y_n} $$
Le but est d'écrire cette expression sous la forme $\langle x, S^*y \rangle = \sum_m x_m \overline{(S^*y)_m}$.
Faisons le changement d'indice $m = n - 1$, ce qui implique $n = m + 1$. La somme sur $m$ parcourt également $\mathbb{Z}$ :
$$ = \sum_{m=-\infty}^{+\infty} x_m \overline{y_{m+1}} $$
Par identification terme à terme, on obtient $\overline{(S^*y)_m} = \overline{y_{m+1}}$, c'est-à-dire :
$$ (S^*y)_m = y_{m+1} $$
L'adjoint de l'opérateur de décalage à droite est donc l'opérateur de décalage à gauche.
Pour vérifier si $S$ est unitaire, il faut vérifier si $S^* S = I$ et $S S^* = I$.
$$ (S^* Sx)_n = (S^*(Sx))_n = (Sx)_{n+1} = x_{(n+1)-1} = x_n $$
Donc $S^*S = I$.
$$ (SS^*x)_n = (S(S^*x))_n = (S^*x)_{n-1} = x_{(n-1)+1} = x_n $$
Donc $SS^* = I$.
Puisque $S^* S = SS^* = I$, on a bien $S^* = S^{-1}$. L'opérateur de décalage bilatéral est un opérateur **unitaire**.
