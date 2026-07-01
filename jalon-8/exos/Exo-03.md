---
---
# Exercice 3 : Noyau, Image, Théorème du Rang avec Paramètre (Difficulté : **)

Soit $\mathbb{K} = \mathbb{R}$ le corps des nombres réels.
Soit $E = \mathbb{R}^3$ l'espace vectoriel des triplets de nombres réels, muni de sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$, où $e_1 = (1, 0, 0)$, $e_2 = (0, 1, 0)$ et $e_3 = (0, 0, 1)$.

On considère l'application linéaire $f_a: E \to E$ définie, pour tout paramètre $a \in \mathbb{R}$, par sa matrice $M_a \in \mathcal{M}_3(\mathbb{R})$ dans la base canonique $\mathcal{B}$ :
$$M_a = \begin{pmatrix} 1 & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{pmatrix}$$

1.  Déterminer les valeurs du paramètre $a \in \mathbb{R}$ pour lesquelles l'application $f_a$ est un automorphisme de $E$.
2.  Pour les valeurs de $a$ pour lesquelles $f_a$ n'est pas un automorphisme, déterminer une base du noyau $\ker(f_a)$ et une base de l'image $\text{Im}(f_a)$.
3.  Dans tous les cas (que $f_a$ soit un automorphisme ou non), vérifier le théorème du rang pour l'application $f_a$.

## Correction détaillée

### Question 1 : Détermination des valeurs de $a$ pour lesquelles $f_a$ est un automorphisme

Soit $f_a: E \to E$ une application linéaire. Par définition, $f_a$ est un automorphisme de l'espace vectoriel $E$ si et seulement si $f_a$ est une application linéaire bijective de $E$ vers $E$.
Une application linéaire $f_a$ est un automorphisme si et seulement si sa matrice représentative $M_a$ dans une base donnée (ici, la base canonique $\mathcal{B}$) est une matrice inversible.
Pour une matrice carrée $M_a \in \mathcal{M}_3(\mathbb{R})$, la condition d'inversibilité est équivalente à la condition que son déterminant soit non nul, c'est-à-dire $\det(M_a) \neq 0$.

Calculons le déterminant de la matrice $M_a$:
$$M_a = \begin{pmatrix} 1 & 1 & 1 \\ 1 & a & 1 \\ 1 & 1 & a \end{pmatrix}$$

Pour simplifier le calcul du déterminant, nous allons effectuer des opérations élémentaires sur les lignes de la matrice. Ces opérations ne modifient pas la valeur du déterminant. L'objectif est de transformer la matrice en une matrice triangulaire supérieure.
Appliquons les opérations suivantes :
1.  $L_2 \leftarrow L_2 - L_1$ (soustraction de la première ligne à la deuxième ligne)
2.  $L_3 \leftarrow L_3 - L_1$ (soustraction de la première ligne à la troisième ligne)

Le déterminant de $M_a$ est alors :
$$ \det(M_a) = \det \begin{pmatrix} 1 & 1 & 1 \\ 1-1 & a-1 & 1-1 \\ 1-1 & 1-1 & a-1 \end{pmatrix} $$
En effectuant les soustractions, nous obtenons la matrice suivante :
$$ \det(M_a) = \det \begin{pmatrix} 1 & 1 & 1 \\ 0 & a-1 & 0 \\ 0 & 0 & a-1 \end{pmatrix} $$

La matrice obtenue est une matrice triangulaire supérieure. Le déterminant d'une matrice triangulaire (qu'elle soit supérieure ou inférieure) est égal au produit de ses éléments diagonaux.
Par conséquent :
$$ \det(M_a) = 1 \cdot (a-1) \cdot (a-1) $$
$$ \det(M_a) = (a-1)^2 $$

L'application $f_a$ est un automorphisme de $E$ si et seulement si $\det(M_a) \neq 0$.
Nous devons donc résoudre l'inéquation :
$$ (a-1)^2 \neq 0 $$
Cette inéquation est vérifiée si et seulement si la base de la puissance n'est pas nulle :
$$ a-1 \neq 0 $$
En ajoutant $1$ aux deux membres de l'inéquation, nous obtenons :
$$ a \neq 1 $$

Par conséquent, l'application linéaire $f_a$ est un automorphisme de $E$ si et seulement si le paramètre $a \in \mathbb{R}$ est différent de $1$.

### Question 2 : Bases du noyau et de l'image pour $f_a$ lorsque $f_a$ n'est pas un automorphisme

D'après les résultats de la Question 1, l'application $f_a$ n'est pas un automorphisme de $E$ si et seulement si $a=1$. Nous allons donc étudier ce cas spécifique.

Pour $a=1$, la matrice de l'application $f_1$ est obtenue en substituant la valeur $a=1$ dans l'expression de $M_a$:
$$M_1 = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$$

#### Détermination d'une base du noyau $\ker(f_1)$

Le noyau de l'application linéaire $f_1$, noté $\ker(f_1)$, est l'ensemble de tous les vecteurs $X \in E = \mathbb{R}^3$ tels que $f_1(X) = 0_E$, où $0_E$ est le vecteur nul de $E$.
En termes matriciels, si $X = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ est un vecteur de $\mathbb{R}^3$, alors $X \in \ker(f_1)$ si et seulement si $M_1 X = 0_E$.
Ceci conduit au système d'équations linéaires homogènes :
$$ \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} $$
En effectuant le produit matriciel, nous obtenons le système suivant :
$$ \begin{cases} 1x + 1y + 1z = 0 \\ 1x + 1y + 1z = 0 \\ 1x + 1y + 1z = 0 \end{cases} $$
Les trois équations de ce système sont identiques. Par conséquent, le système se réduit à une seule équation linéaire :
$$ x + y + z = 0 $$
Cette équation définit un plan passant par l'origine dans l'espace vectoriel $\mathbb{R}^3$. Pour trouver une base du noyau, nous exprimons une variable en fonction des autres. Choisissons d'exprimer $z$ en fonction de $x$ et $y$:
$$ z = -x - y $$
Un vecteur $X \in \ker(f_1)$ peut donc s'écrire sous la forme :
$$ X = \begin{pmatrix} x \\ y \\ -x-y \end{pmatrix} $$
Nous pouvons décomposer ce vecteur en une combinaison linéaire de vecteurs où $x$ et $y$ sont les coefficients (scalaires) :
$$ X = \begin{pmatrix} x \\ 0 \\ -x \end{pmatrix} + \begin{pmatrix} 0 \\ y \\ -y \end{pmatrix} $$
$$ X = x \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + y \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} $$
Soient les vecteurs $v_1 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}$ et $v_2 = \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$.
Ces vecteurs $v_1$ et $v_2$ engendrent le noyau $\ker(f_1)$, c'est-à-dire $\ker(f_1) = \text{Vect}(v_1, v_2)$.
Pour qu'ils forment une base du noyau, il faut également qu'ils soient linéairement indépendants.
Considérons une combinaison linéaire nulle de $v_1$ et $v_2$ avec des scalaires $\alpha, \beta \in \mathbb{R}$:
$$ \alpha v_1 + \beta v_2 = 0_E $$
$$ \alpha \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} $$
En effectuant l'addition vectorielle, nous obtenons :
$$ \begin{pmatrix} \alpha \cdot 1 + \beta \cdot 0 \\ \alpha \cdot 0 + \beta \cdot 1 \\ \alpha \cdot (-1) + \beta \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} $$
Ce qui conduit au système d'équations :
$$ \begin{cases} \alpha = 0 \\ \beta = 0 \\ -\alpha - \beta = 0 \end{cases} $$
Les deux premières équations impliquent directement $\alpha = 0$ et $\beta = 0$. La troisième équation est alors satisfaite : $-(0) - (0) = 0$.
Puisque la seule combinaison linéaire de $v_1$ et $v_2$ qui donne le vecteur nul est celle où tous les scalaires sont nuls, les vecteurs $v_1$ et $v_2$ sont linéairement indépendants.

Par conséquent, une base du noyau de $f_1$ est $\mathcal{B}_{\ker(f_1)} = \left\{ \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix} \right\}$.
La dimension du noyau de $f_1$ est $\dim(\ker(f_1)) = 2$.

#### Détermination d'une base de l'image $\text{Im}(f_1)$

L'image de l'application linéaire $f_1$, notée $\text{Im}(f_1)$, est l'espace vectoriel engendré par les vecteurs colonnes de la matrice $M_1$.
Les vecteurs colonnes de $M_1$ sont :
$$ C_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad C_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \quad C_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} $$
L'image est l'ensemble des combinaisons linéaires de ces vecteurs colonnes :
$$ \text{Im}(f_1) = \text{Vect}(C_1, C_2, C_3) $$
Nous observons que les trois vecteurs colonnes sont identiques : $C_1 = C_2 = C_3$.
Par conséquent, l'espace engendré par ces trois vecteurs est le même que l'espace engendré par un seul d'entre eux.
$$ \text{Im}(f_1) = \text{Vect}\left(\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}\right) $$
Soit le vecteur $w_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$. Ce vecteur est non nul. Un ensemble constitué d'un unique vecteur non nul est toujours linéairement indépendant.
Ainsi, le vecteur $w_1$ forme à lui seul une base de l'image de $f_1$.

Par conséquent, une base de l'image de $f_1$ est $\mathcal{B}_{\text{Im}(f_1)} = \left\{ \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right\}$.
La dimension de l'image de $f_1$ est $\dim(\text{Im}(f_1)) = 1$.

### Question 3 : Vérification du théorème du rang dans tous les cas

Le théorème du rang est un résultat fondamental en algèbre linéaire qui relie la dimension de l'espace de départ, la dimension du noyau et la dimension de l'image d'une application linéaire.
Pour toute application linéaire $f: E \to F$, où $E$ et $F$ sont des espaces vectoriels de dimension finie, le théorème du rang stipule que :
$$ \dim(E) = \dim(\ker(f)) + \dim(\text{Im}(f)) $$
où $\dim(\text{Im}(f))$ est également appelé le rang de $f$, noté $\text{rang}(f)$.

Dans notre exercice, l'espace de départ est $E = \mathbb{R}^3$. Sa dimension est $\dim(E) = 3$.
Nous allons vérifier le théorème du rang pour les deux cas distincts du paramètre $a \in \mathbb{R}$.

#### Cas 1 : $a=1$ (où $f_1$ n'est pas un automorphisme)

D'après les calculs effectués dans la Question 2 pour le cas $a=1$:
*   La dimension du noyau de $f_1$ est $\dim(\ker(f_1)) = 2$.
*   La dimension de l'image de $f_1$ est $\dim(\text{Im}(f_1)) = 1$.

Appliquons le théorème du rang avec ces valeurs :
$$ \dim(E) = \dim(\ker(f_1)) + \dim(\text{Im}(f_1)) $$
$$ 3 = 2 + 1 $$
$$ 3 = 3 $$
L'égalité est vérifiée. Le théorème du rang est donc confirmé pour l'application $f_1$ lorsque $a=1$.

#### Cas 2 : $a \neq 1$ (où $f_a$ est un automorphisme)

D'après les résultats de la Question 1, si $a \neq 1$, l'application $f_a: E \to E$ est un automorphisme de $E$.
Par définition, un automorphisme est une application linéaire bijective.
1.  **Injectivité de $f_a$**: Puisque $f_a$ est injective, son noyau est réduit au seul vecteur nul de l'espace de départ $E$.
    $$ \ker(f_a) = \{0_E\} $$
    Par conséquent, la dimension du noyau de $f_a$ est :
    $$ \dim(\ker(f_a)) = 0 $$
2.  **Surjectivité de $f_a$**: Puisque $f_a$ est surjective et que l'espace d'arrivée est $E$, son image est égale à l'espace d'arrivée $E$.
    $$ \text{Im}(f_a) = E $$
    Par conséquent, la dimension de l'image de $f_a$ est :
    $$ \dim(\text{Im}(f_a)) = \dim(E) = 3 $$

Appliquons le théorème du rang avec ces valeurs pour $a \neq 1$:
$$ \dim(E) = \dim(\ker(f_a)) + \dim(\text{Im}(f_a)) $$
$$ 3 = 0 + 3 $$
$$ 3 = 3 $$
L'égalité est vérifiée. Le théorème du rang est donc confirmé pour l'application $f_a$ lorsque $a \neq 1$.

En conclusion, le théorème du rang est vérifié pour toutes les valeurs du paramètre $a \in \mathbb{R}$.
