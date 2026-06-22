# Exercice 5 : Inversibilité et inverse d'une matrice paramétrée, application à un système linéaire
**Difficulté :** ★★★☆☆

## Énoncé
Soit $x$ un scalaire réel, c'est-à-dire $x \in \mathbb{R}$.
Considérons la matrice $M_x \in \mathcal{M}_{2}(\mathbb{R})$ définie par :
$$ M_x = \begin{pmatrix} x & 1 \\ 1 & x \end{pmatrix} $$

1.  Déterminer l'ensemble des valeurs de $x \in \mathbb{R}$ pour lesquelles la matrice $M_x$ est inversible.
2.  Pour tout $x$ appartenant à cet ensemble, calculer l'inverse $M_x^{-1}$ de la matrice $M_x$.
3.  Soit le vecteur colonne $\mathbf{b} = \begin{pmatrix} 2 \\ 4 \end{pmatrix} \in \mathbb{R}^2$. Pour la valeur spécifique $x = 3$, résoudre le système d'équations linéaires $M_3 \mathbf{v} = \mathbf{b}$, où $\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \in \mathbb{R}^2$.

## Correction Détaillée

### Question 1 : Détermination de l'ensemble des valeurs de $x$ pour lesquelles $M_x$ est inversible.

Une matrice carrée est inversible si et seulement si son déterminant est non nul. Nous allons donc calculer le déterminant de la matrice $M_x$.

Pour une matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathcal{M}_{2}(\mathbb{R})$, son déterminant est donné par la formule :
$$ \det(A) = ad - bc $$

Appliquons cette formule à la matrice $M_x = \begin{pmatrix} x & 1 \\ 1 & x \end{pmatrix}$. Ici, nous avons $a=x$, $b=1$, $c=1$, et $d=x$.
$$ \det(M_x) = (x)(x) - (1)(1) $$
$$ \det(M_x) = x^2 - 1 $$

La matrice $M_x$ est inversible si et seulement si son déterminant est non nul :
$$ \det(M_x) \neq 0 $$
$$ x^2 - 1 \neq 0 $$
Cette inégalité peut être factorisée en utilisant l'identité remarquable $a^2 - b^2 = (a-b)(a+b)$ :
$$ (x - 1)(x + 1) \neq 0 $$
Pour qu'un produit de deux facteurs soit non nul, il faut que chacun des facteurs soit non nul. Ainsi, nous avons :
$$ x - 1 \neq 0 \quad \text{et} \quad x + 1 \neq 0 $$
Ce qui implique :
$$ x \neq 1 \quad \text{et} \quad x \neq -1 $$

Par conséquent, la matrice $M_x$ est inversible pour toutes les valeurs de $x \in \mathbb{R}$ à l'exception de $x = 1$ et $x = -1$.
L'ensemble des valeurs de $x$ pour lesquelles $M_x$ est inversible est $\mathbb{R} \setminus \{-1, 1\}$.

### Question 2 : Calcul de l'inverse $M_x^{-1}$ pour les valeurs où $M_x$ est inversible.

Pour une matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathcal{M}_{2}(\mathbb{R})$ inversible (c'est-à-dire $\det(A) = ad-bc \neq 0$), son inverse $A^{-1}$ est donnée par la formule :
$$ A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} $$

Nous avons déjà calculé $\det(M_x) = x^2 - 1$.
Pour la matrice $M_x = \begin{pmatrix} x & 1 \\ 1 & x \end{pmatrix}$, nous avons $a=x$, $b=1$, $c=1$, et $d=x$.

En substituant ces valeurs dans la formule de l'inverse, pour $x \in \mathbb{R} \setminus \{-1, 1\}$ :
$$ M_x^{-1} = \frac{1}{x^2 - 1} \begin{pmatrix} x & -1 \\ -1 & x \end{pmatrix} $$

Nous pouvons également écrire cette matrice en distribuant le facteur scalaire $\frac{1}{x^2-1}$ à chaque élément de la matrice :
$$ M_x^{-1} = \begin{pmatrix} \frac{x}{x^2 - 1} & \frac{-1}{x^2 - 1} \\ \frac{-1}{x^2 - 1} & \frac{x}{x^2 - 1} \end{pmatrix} $$

### Question 3 : Résolution du système linéaire $M_3 \mathbf{v} = \mathbf{b}$ pour $x=3$.

Pour $x=3$, la matrice $M_x$ devient $M_3$.
$$ M_3 = \begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix} $$

Vérifions d'abord si $M_3$ est inversible. D'après la question 1, $M_x$ est inversible pour $x \in \mathbb{R} \setminus \{-1, 1\}$. Puisque $3 \notin \{-1, 1\}$, la matrice $M_3$ est bien inversible.
Son déterminant est $\det(M_3) = 3^2 - 1 = 9 - 1 = 8$. Puisque $\det(M_3) = 8 \neq 0$, $M_3$ est inversible.

Le système d'équations linéaires est $M_3 \mathbf{v} = \mathbf{b}$. Puisque $M_3$ est inversible, nous pouvons multiplier les deux côtés de l'équation par $M_3^{-1}$ à gauche pour isoler le vecteur $\mathbf{v}$ :
$$ M_3^{-1} (M_3 \mathbf{v}) = M_3^{-1} \mathbf{b} $$
Par associativité de la multiplication matricielle, nous avons :
$$ (M_3^{-1} M_3) \mathbf{v} = M_3^{-1} \mathbf{b} $$
Puisque le produit d'une matrice par son inverse est la matrice identité ($M_3^{-1} M_3 = I_2$, où $I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ est la matrice identité d'ordre 2) :
$$ I_2 \mathbf{v} = M_3^{-1} \mathbf{b} $$
La multiplication par la matrice identité ne change pas le vecteur, donc :
$$ \mathbf{v} = M_3^{-1} \mathbf{b} $$

Nous utilisons la formule de l'inverse trouvée à la question 2, en substituant $x=3$ :
$$ M_3^{-1} = \frac{1}{3^2 - 1} \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix} $$
$$ M_3^{-1} = \frac{1}{9 - 1} \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix} $$
$$ M_3^{-1} = \frac{1}{8} \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix} $$

Maintenant, nous calculons le produit $M_3^{-1} \mathbf{b}$ avec $\mathbf{b} = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$ :
$$ \mathbf{v} = \frac{1}{8} \begin{pmatrix} 3 & -1 \\ -1 & 3 \end{pmatrix} \begin{pmatrix} 2 \\ 4 \end{pmatrix} $$

Effectuons la multiplication matrice-vecteur. Le résultat est un vecteur colonne dont les éléments sont obtenus par le produit scalaire des lignes de la matrice (sans le facteur $\frac{1}{8}$ pour l'instant) avec le vecteur $\mathbf{b}$.

Le premier élément du vecteur résultant est :
$$ (3)(2) + (-1)(4) = 6 - 4 = 2 $$

Le second élément du vecteur résultant est :
$$ (-1)(2) + (3)(4) = -2 + 12 = 10 $$

Donc, le produit matriciel donne :
$$ \mathbf{v} = \frac{1}{8} \begin{pmatrix} 2 \\ 10 \end{pmatrix} $$

Enfin, nous distribuons le facteur scalaire $\frac{1}{8}$ aux éléments du vecteur :
$$ \mathbf{v} = \begin{pmatrix} \frac{2}{8} \\ \frac{10}{8} \end{pmatrix} $$
En simplifiant les fractions :
$$ \mathbf{v} = \begin{pmatrix} \frac{1}{4} \\ \frac{5}{4} \end{pmatrix} $$

La solution du système linéaire $M_3 \mathbf{v} = \mathbf{b}$ est donc $\mathbf{v} = \begin{pmatrix} 1/4 \\ 5/4 \end{pmatrix}$.
