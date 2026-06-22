# Exercice 7 : Étude d'une application linéaire sur l'espace des matrices carrées d'ordre 2
**Difficulté :** ★★★★☆

## Énoncé
Soit $E = \mathcal{M}_2(\mathbb{R})$ l'espace vectoriel des matrices carrées d'ordre 2 à coefficients réels.
On munit $E$ de la base canonique ordonnée $\mathcal{B} = (E_{11}, E_{12}, E_{21}, E_{22})$, où $E_{ij}$ désigne la matrice élémentaire dont le coefficient à la $i$-ème ligne et $j$-ème colonne est 1 et tous les autres sont nuls.
Soit $A \in \mathcal{M}_2(\mathbb{R})$ la matrice définie par $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
On considère l'application $\Phi_A: E \to E$ définie pour toute matrice $M \in E$ par $\Phi_A(M) = AM - MA$.

1.  Démontrer que $\Phi_A$ est une application linéaire.
2.  Déterminer la matrice $M_{\mathcal{B}}(\Phi_A)$ représentant l'application linéaire $\Phi_A$ dans la base $\mathcal{B}$.
3.  Déterminer le noyau $\text{Ker}(\Phi_A)$ et l'image $\text{Im}(\Phi_A)$ de $\Phi_A$. En déduire si $\Phi_A$ est injective, surjective, ou bijective.

## Correction Détaillée

### Question 1 : Démontrer que $\Phi_A$ est une application linéaire.

Pour démontrer que $\Phi_A$ est une application linéaire, nous devons vérifier deux propriétés :
1.  Additivité : $\forall M_1, M_2 \in E, \Phi_A(M_1 + M_2) = \Phi_A(M_1) + \Phi_A(M_2)$.
2.  Homogénéité : $\forall \lambda \in \mathbb{R}, \forall M \in E, \Phi_A(\lambda M) = \lambda \Phi_A(M)$.

Soient $M_1, M_2 \in E$ et $\lambda \in \mathbb{R}$.

**Vérification de l'additivité :**
$\Phi_A(M_1 + M_2) = A(M_1 + M_2) - (M_1 + M_2)A$
En utilisant la distributivité de la multiplication matricielle par rapport à l'addition :
$A(M_1 + M_2) = AM_1 + AM_2$
$(M_1 + M_2)A = M_1 A + M_2 A$
Donc,
$\Phi_A(M_1 + M_2) = (AM_1 + AM_2) - (M_1 A + M_2 A)$
$\Phi_A(M_1 + M_2) = AM_1 + AM_2 - M_1 A - M_2 A$
En réarrangeant les termes :
$\Phi_A(M_1 + M_2) = (AM_1 - M_1 A) + (AM_2 - M_2 A)$
Par définition de $\Phi_A$:
$\Phi_A(M_1 + M_2) = \Phi_A(M_1) + \Phi_A(M_2)$
L'additivité est vérifiée.

**Vérification de l'homogénéité :**
$\Phi_A(\lambda M) = A(\lambda M) - (\lambda M)A$
En utilisant la propriété de scalarité de la multiplication matricielle :
$A(\lambda M) = \lambda (AM)$
$(\lambda M)A = \lambda (MA)$
Donc,
$\Phi_A(\lambda M) = \lambda (AM) - \lambda (MA)$
En factorisant le scalaire $\lambda$ :
$\Phi_A(\lambda M) = \lambda (AM - MA)$
Par définition de $\Phi_A$:
$\Phi_A(\lambda M) = \lambda \Phi_A(M)$
L'homogénéité est vérifiée.

Puisque $\Phi_A$ satisfait les deux propriétés d'additivité et d'homogénéité, nous pouvons conclure que $\Phi_A$ est une application linéaire.

### Question 2 : Déterminer la matrice $M_{\mathcal{B}}(\Phi_A)$ représentant l'application linéaire $\Phi_A$ dans la base $\mathcal{B}$.

La base $\mathcal{B}$ de $E = \mathcal{M}_2(\mathbb{R})$ est donnée par :
$E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$.
La matrice $A$ est $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

Pour construire la matrice $M_{\mathcal{B}}(\Phi_A)$, nous devons calculer $\Phi_A(E_{ij})$ pour chaque matrice de base et exprimer le résultat comme une combinaison linéaire des matrices de base $E_{11}, E_{12}, E_{21}, E_{22}$. Les coefficients de ces combinaisons linéaires formeront les colonnes de $M_{\mathcal{B}}(\Phi_A)$.

**Calcul de $\Phi_A(E_{11})$ :**
$AE_{11} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 0 + 1 \cdot 0 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$
$E_{11}A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 1 \\ 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$
$\Phi_A(E_{11}) = AE_{11} - E_{11}A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} - \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1-1 & 0-1 \\ 0-0 & 0-0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}$
En termes de la base $\mathcal{B}$ : $\Phi_A(E_{11}) = 0 \cdot E_{11} - 1 \cdot E_{12} + 0 \cdot E_{21} + 0 \cdot E_{22}$.
La première colonne de $M_{\mathcal{B}}(\Phi_A)$ est $\begin{pmatrix} 0 \\ -1 \\ 0 \\ 0 \end{pmatrix}$.

**Calcul de $\Phi_A(E_{12})$ :**
$AE_{12} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot 0 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
$E_{12}A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \\ 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
$\Phi_A(E_{12}) = AE_{12} - E_{12}A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$
En termes de la base $\mathcal{B}$ : $\Phi_A(E_{12}) = 0 \cdot E_{11} + 0 \cdot E_{12} + 0 \cdot E_{21} + 0 \cdot E_{22}$.
La deuxième colonne de $M_{\mathcal{B}}(\Phi_A)$ est $\begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}$.

**Calcul de $\Phi_A(E_{21})$ :**
$AE_{21} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 \cdot 0 + 1 \cdot 1 & 1 \cdot 0 + 1 \cdot 0 \\ 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 0 + 1 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$
$E_{21}A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 1 \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 1 + 0 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix}$
$\Phi_A(E_{21}) = AE_{21} - E_{21}A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 0 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1-0 & 0-0 \\ 1-1 & 0-1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$
En termes de la base $\mathcal{B}$ : $\Phi_A(E_{21}) = 1 \cdot E_{11} + 0 \cdot E_{12} + 0 \cdot E_{21} - 1 \cdot E_{22}$.
La troisième colonne de $M_{\mathcal{B}}(\Phi_A)$ est $\begin{pmatrix} 1 \\ 0 \\ 0 \\ -1 \end{pmatrix}$.

**Calcul de $\Phi_A(E_{22})$ :**
$AE_{22} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 \cdot 0 + 1 \cdot 0 & 1 \cdot 0 + 1 \cdot 1 \\ 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$
$E_{22}A = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 \cdot 1 + 0 \cdot 0 & 0 \cdot 1 + 0 \cdot 1 \\ 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$
$\Phi_A(E_{22}) = AE_{22} - E_{22}A = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} - \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0-0 & 1-0 \\ 0-0 & 1-1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
En termes de la base $\mathcal{B}$ : $\Phi_A(E_{22}) = 0 \cdot E_{11} + 1 \cdot E_{12} + 0 \cdot E_{21} + 0 \cdot E_{22}$.
La quatrième colonne de $M_{\mathcal{B}}(\Phi_A)$ est $\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$.

En regroupant ces colonnes, la matrice $M_{\mathcal{B}}(\Phi_A)$ est :
$M_{\mathcal{B}}(\Phi_A) = \begin{pmatrix}
0 & 0 & 1 & 0 \\
-1 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & -1 & 0
\end{pmatrix}$.

### Question 3 : Déterminer le noyau $\text{Ker}(\Phi_A)$ et l'image $\text{Im}(\Phi_A)$ de $\Phi_A$. En déduire si $\Phi_A$ est injective, surjective, ou bijective.

**Détermination du noyau $\text{Ker}(\Phi_A)$ :**
Le noyau de $\Phi_A$ est l'ensemble des matrices $M \in E$ telles que $\Phi_A(M) = 0$.
C'est-à-dire, $AM - MA = 0$, ou $AM = MA$.
Soit $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ une matrice générique de $E$.
Calculons $AM$ :
$AM = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 \cdot a + 1 \cdot c & 1 \cdot b + 1 \cdot d \\ 0 \cdot a + 1 \cdot c & 0 \cdot b + 1 \cdot d \end{pmatrix} = \begin{pmatrix} a+c & b+d \\ c & d \end{pmatrix}$.
Calculons $MA$ :
$MA = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a \cdot 1 + b \cdot 0 & a \cdot 1 + b \cdot 1 \\ c \cdot 1 + d \cdot 0 & c \cdot 1 + d \cdot 1 \end{pmatrix} = \begin{pmatrix} a & a+b \\ c & c+d \end{pmatrix}$.

Pour que $AM = MA$, nous devons avoir l'égalité de leurs coefficients :
1.  $a+c = a \implies c = 0$.
2.  $b+d = a+b \implies d = a$.
3.  $c = c$ (cette équation est triviale et cohérente avec $c=0$).
4.  $d = c+d \implies c = 0$ (cette équation est également cohérente avec $c=0$).

Ainsi, une matrice $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ est dans $\text{Ker}(\Phi_A)$ si et seulement si $c=0$ et $d=a$.
Donc, les matrices du noyau sont de la forme $M = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$.
Nous pouvons écrire ces matrices comme une combinaison linéaire :
$M = a \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + b \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = a I_2 + b E_{12}$.
Le noyau $\text{Ker}(\Phi_A)$ est l'ensemble des matrices qui commutent avec $A$.
Une base de $\text{Ker}(\Phi_A)$ est $\left( \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \right)$.
La dimension du noyau est $\dim(\text{Ker}(\Phi_A)) = 2$.

**Déduction sur l'injectivité :**
Puisque $\dim(\text{Ker}(\Phi_A)) = 2 \neq 0$, l'application linéaire $\Phi_A$ n'est pas injective.

**Détermination de l'image $\text{Im}(\Phi_A)$ :**
L'image de $\Phi_A$ est l'ensemble des vecteurs (matrices) de $E$ qui peuvent être atteints par $\Phi_A$.
L'image est engendrée par les colonnes de la matrice $M_{\mathcal{B}}(\Phi_A)$.
Les colonnes de $M_{\mathcal{B}}(\Phi_A)$ sont :
$C_1 = \begin{pmatrix} 0 \\ -1 \\ 0 \\ 0 \end{pmatrix}$, $C_2 = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}$, $C_3 = \begin{pmatrix} 1 \\ 0 \\ 0 \\ -1 \end{pmatrix}$, $C_4 = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$.
En termes de matrices de base :
$\Phi_A(E_{11}) = -E_{12}$
$\Phi_A(E_{12}) = 0$
$\Phi_A(E_{21}) = E_{11} - E_{22}$
$\Phi_A(E_{22}) = E_{12}$

L'image $\text{Im}(\Phi_A)$ est l'espace vectoriel engendré par ces matrices :
$\text{Im}(\Phi_A) = \text{Vect}(-E_{12}, 0, E_{11}-E_{22}, E_{12})$.
Nous pouvons simplifier cette expression :
$\text{Im}(\Phi_A) = \text{Vect}(-E_{12}, E_{11}-E_{22}, E_{12})$.
Puisque $-E_{12}$ et $E_{12}$ sont colinéaires, nous pouvons réduire l'ensemble des générateurs à :
$\text{Im}(\Phi_A) = \text{Vect}(E_{12}, E_{11}-E_{22})$.
Ces deux matrices, $E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ et $E_{11}-E_{22} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, sont linéairement indépendantes.
En effet, si $\alpha E_{12} + \beta (E_{11}-E_{22}) = 0$, alors $\begin{pmatrix} \beta & \alpha \\ 0 & -\beta \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$, ce qui implique $\alpha=0$ et $\beta=0$.
Donc, une base de $\text{Im}(\Phi_A)$ est $\left( \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \right)$.
La dimension de l'image est $\dim(\text{Im}(\Phi_A)) = 2$.

**Vérification par le théorème du rang :**
La dimension de l'espace de départ $E$ est $\dim(E) = 4$.
Le théorème du rang stipule que $\dim(E) = \dim(\text{Ker}(\Phi_A)) + \dim(\text{Im}(\Phi_A))$.
Nous avons $4 = 2 + 2$, ce qui est cohérent avec nos calculs.

**Déduction sur la surjectivité et la bijectivité :**
Puisque $\dim(\text{Im}(\Phi_A)) = 2 \neq \dim(E) = 4$, l'application linéaire $\Phi_A$ n'est pas surjective.
Puisqu'elle n'est ni injective ni surjective, $\Phi_A$ n'est pas bijective.

**Résumé des conclusions :**
*   Le noyau de $\Phi_A$ est $\text{Ker}(\Phi_A) = \left\{ \begin{pmatrix} a & b \\ 0 & a \end{pmatrix} \mid a, b \in \mathbb{R} \right\}$, de dimension 2.
*   L'image de $\Phi_A$ est $\text{Im}(\Phi_A) = \left\{ \begin{pmatrix} x & y \\ 0 & -x \end{pmatrix} \mid x, y \in \mathbb{R} \right\}$, de dimension 2.
*   $\Phi_A$ n'est pas injective car $\text{Ker}(\Phi_A) \neq \{0\}$.
*   $\Phi_A$ n'est pas surjective car $\text{Im}(\Phi_A) \neq E$.
*   $\Phi_A$ n'est pas bijective.
