# Exercice 3 : Noyau, Image, Théorème du Rang avec Paramètre (Difficulté : **)

Soit $\mathbb{K} = \mathbb{R}$ le corps des nombres réels.
Soit $E = \mathbb{R}^3$ l'espace vectoriel des triplets de nombres réels, muni de sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$, où $e_1 = (1, 0, 0)$, $e_2 = (0, 1, 0)$ et $e_3 = (0, 0, 1)$.

On considère l'application linéaire $f_a: E \to E$ définie, pour tout $a \in \mathbb{R}$, par sa matrice $M_a$ dans la base canonique $\mathcal{B}$ :
$$M_a = \begin{pmatrix} 1 & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{pmatrix}$$

1.  Déterminer les valeurs du paramètre $a \in \mathbb{R}$ pour lesquelles l'application $f_a$ est un automorphisme de $E$.
2.  Pour les valeurs de $a$ pour lesquelles $f_a$ n'est pas un automorphisme, déterminer une base du noyau $\ker(f_a)$ et une base de l'image $\text{Im}(f_a)$.
3.  Dans tous les cas (que $f_a$ soit un automorphisme ou non), vérifier le théorème du rang pour l'application $f_a$.

## Correction détaillée

### Question 1 : Détermination des valeurs de $a$ pour lesquelles $f_a$ est un automorphisme

Une application linéaire $f: E \to E$ est un automorphisme si et seulement si sa matrice représentative dans une base donnée est inversible. Pour une matrice carrée $M_a \in \mathcal{M}_3(\mathbb{R})$, cela équivaut à $\det(M_a) \neq 0$.

Calculons le déterminant de $M_a$:
$$M_a = \begin{pmatrix} 1 & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{pmatrix}$$

Nous pouvons effectuer des opérations élémentaires sur les lignes qui ne modifient pas le déterminant. Pour simplifier le calcul, nous allons rendre nuls les éléments sous le pivot de la première colonne.
Appliquons les opérations suivantes : $L_2 \leftarrow L_2 - L_1$ et $L_3 \leftarrow L_3 - L_1$.
$$\det(M_a) = \det \begin{pmatrix} 1 & 1 & 1 \\ 1-1 & a-1 & 1-1 \\ 1-1 & 1-1 & a-1 \end{pmatrix} = \det \begin{pmatrix} 1 & 1 & 1 \\ 0 & a-1 & 0 \\ 0 & 0 & a-1 \end{pmatrix}$$

Cette dernière matrice est triangulaire supérieure. Le déterminant d'une matrice triangulaire est égal au produit de ses éléments diagonaux.
$$\det(M_a) = 1 \cdot (a-1) \cdot (a-1) = (a-1)^2$$

L'application $f_a$ est un automorphisme si et seulement si $\det(M_a) \neq 0$.
L'équation $(a-1)^2 \neq 0$ est vérifiée si et seulement si $a-1 \neq 0$, ce qui implique $a \neq 1$.

Par conséquent, $f_a$ est un automorphisme de $E$ si et seulement si $a \neq 1$.

### Question 2 : Bases du noyau et de l'image pour $f_a$ lorsque $f_a$ n'est pas un automorphisme

D'après la question 1, $f_a$ n'est pas un automorphisme si et seulement si $a=1$. Nous allons donc étudier ce cas particulier.

Pour $a=1$, la matrice de l'application $f_1$ est obtenue en substituant $a=1$ dans $M_a$:
$$M_1 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$$

#### Détermination d'une base du noyau $\ker(f_1)$

Le noyau $\ker(f_1)$ est l'ensemble des vecteurs $X = (x, y, z)^T \in \mathbb{R}^3$ tels que $f_1(X) = 0_E$. Cela est équivalent à résoudre le système linéaire homogène $M_1 X = 0$:
$$\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
Ce système de trois équations à trois inconnues se réduit à une seule équation linéaire car toutes les lignes sont identiques :
$$x + y + z = 0$$

Les solutions de cette équation décrivent un plan dans $\mathbb{R}^3$. Nous pouvons exprimer une variable en fonction des deux autres, par exemple $z = -x - y$.
Un vecteur $X \in \ker(f_1)$ s'écrit alors :
$$X = \begin{pmatrix} x \\ y \\ -x-y \end{pmatrix}$$
Nous pouvons décomposer ce vecteur comme une combinaison linéaire de vecteurs fixes :
$$X = x \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + y \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$$
Les vecteurs $v_1 = (1, 0, -1)^T$ et $v_2 = (0, 1, -1)^T$ engendrent le noyau $\ker(f_1)$.
Pour vérifier s'ils forment une base, il faut montrer qu'ils sont linéairement indépendants. Supposons qu'il existe des scalaires $\alpha, \beta \in \mathbb{R}$ tels que $\alpha v_1 + \beta v_2 = 0_E$.
$$\alpha \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \\ -\alpha - \beta \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$
Ceci implique $\alpha = 0$, $\beta = 0$ et $-\alpha - \beta = 0$. Les deux premières équations suffisent à montrer que $\alpha = 0$ et $\beta = 0$. Les vecteurs $v_1$ et $v_2$ sont donc linéairement indépendants.

Ainsi, une base du noyau de $f_1$ est $\mathcal{B}_{\ker(f_1)} = \{(1, 0, -1), (0, 1, -1)\}$.
La dimension du noyau est $\dim(\ker(f_1)) = 2$.

#### Détermination d'une base de l'image $\text{Im}(f_1)$

L'image $\text{Im}(f_1)$ est l'espace vectoriel engendré par les colonnes de la matrice $M_1$.
Les colonnes de $M_1$ sont :
$$C_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad C_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad C_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$$
Ces trois vecteurs colonnes sont identiques. Par conséquent, l'image est engendrée par n'importe lequel de ces vecteurs, puisque tous les autres sont des multiples de celui-ci.
$\text{Im}(f_1) = \text{Vect}\left(\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\right)$.
Le vecteur $w_1 = (1, 1, 1)^T$ est non nul, il forme donc à lui seul une base de l'image.

Ainsi, une base de l'image de $f_1$ est $\mathcal{B}_{\text{Im}(f_1)} = \{(1, 1, 1)\}$.
La dimension de l'image est $\dim(\text{Im}(f_1)) = 1$.

### Question 3 : Vérification du théorème du rang dans tous les cas

Le théorème du rang stipule que pour toute application linéaire $f: E \to F$, on a la relation :
$\dim(E) = \dim(\ker(f)) + \text{rang}(f)$, où $\text{rang}(f) = \dim(\text{Im}(f))$.
Dans notre cas, l'espace de départ $E = \mathbb{R}^3$, donc $\dim(E) = 3$.

#### Cas 1 : $a=1$ (où $f_1$ n'est pas un automorphisme)

D'après les calculs de la question 2 :
Nous avons trouvé $\dim(\ker(f_1)) = 2$.
Nous avons trouvé $\dim(\text{Im}(f_1)) = 1$.

Vérifions le théorème du rang pour $f_1$:
$\dim(E) = \dim(\ker(f_1)) + \dim(\text{Im}(f_1))$
$3 = 2 + 1$
$3 = 3$
Le théorème du rang est bien vérifié pour $a=1$.

#### Cas 2 : $a \neq 1$ (où $f_a$ est un automorphisme)

D'après la question 1, si $a \neq 1$, l'application $f_a$ est un automorphisme de $E$.
Par définition, un automorphisme est une application linéaire bijective.
- Puisque $f_a$ est injective, son noyau est réduit au seul vecteur nul de $E$: $\ker(f_a) = \{0_E\}$.
  Par conséquent, la dimension du noyau est $\dim(\ker(f_a)) = 0$.
- Puisque $f_a$ est surjective (et qu'elle va de $E$ vers $E$), son image est égale à l'espace d'arrivée $E$: $\text{Im}(f_a) = E$.
  Par conséquent, la dimension de l'image est $\dim(\text{Im}(f_a)) = \dim(E) = 3$.

Vérifions le théorème du rang pour $f_a$ lorsque $a \neq 1$:
$\dim(E) = \dim(\ker(f_a)) + \dim(\text{Im}(f_a))$
$3 = 0 + 3$
$3 = 3$
Le théorème du rang est bien vérifié pour $a \neq 1$.

Le théorème du rang est donc vérifié pour toutes les valeurs de $a \in \mathbb{R}$.
