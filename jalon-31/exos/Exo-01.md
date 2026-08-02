# Exercice 01 : Nilpotence basique en dimension 2 (⭐)

## Énoncé
Soit $N \in \mathcal{M}_2(\mathbb{R})$ la matrice définie par :
$$N = \begin{pmatrix} 2 & -1 \\ 4 & -2 \end{pmatrix}$$
1. Calculer $N^2$. Que peut-on en déduire sur l'endomorphisme canoniquement associé à $N$ ?
2. Déterminer le polynôme caractéristique $\chi_N(X)$ de $N$ et vérifier le lien avec la nilpotence.

## Corrigé Rigoureux : Démonstration Complète

### 1. Calcul de $N^2$
Posons $N = \begin{pmatrix} 2 & -1 \\ 4 & -2 \end{pmatrix}$.
Nous calculons le produit matriciel $N \times N$ :
$$N^2 = \begin{pmatrix} 2 & -1 \\ 4 & -2 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 4 & -2 \end{pmatrix}$$
Calcul des coefficients de $N^2 = (c_{i,j})$ :
- $c_{1,1} = 2 \times 2 + (-1) \times 4 = 4 - 4 = 0$
- $c_{1,2} = 2 \times (-1) + (-1) \times (-2) = -2 + 2 = 0$
- $c_{2,1} = 4 \times 2 + (-2) \times 4 = 8 - 8 = 0$
- $c_{2,2} = 4 \times (-1) + (-2) \times (-2) = -4 + 4 = 0$
Ainsi,
$$N^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = 0_{\mathcal{M}_2(\mathbb{R})}$$
L'endomorphisme canoniquement associé à $N$ s'annule pour la puissance $2$. Puisque $N \neq 0$, son indice de nilpotence est exactement $p = 2$. $N$ est une matrice nilpotente.

### 2. Polynôme caractéristique
Par définition, le polynôme caractéristique de $N$ est $\chi_N(X) = \det(X I_2 - N)$.
$$\chi_N(X) = \det \begin{pmatrix} X - 2 & 1 \\ -4 & X + 2 \end{pmatrix}$$
Calculons ce déterminant :
$$\chi_N(X) = (X - 2)(X + 2) - (1 \times (-4))$$
$$\chi_N(X) = (X^2 - 4) + 4$$
$$\chi_N(X) = X^2$$
Puisque le polynôme caractéristique est $\chi_N(X) = X^2$, le théorème de caractérisation spectrale des matrices nilpotentes en dimension $n=2$ s'applique : l'unique valeur propre de $N$ est $0$. Ceci est cohérent avec le fait que $N$ est nilpotente (et, réciproquement, en dimension finie, une unique valeur propre nulle implique la nilpotence par le théorème de Cayley-Hamilton qui donne $N^2 = 0$).
