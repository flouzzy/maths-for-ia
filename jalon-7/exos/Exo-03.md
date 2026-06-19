# Exercice 3 : Sous-espace des matrices à trace nulle et famille libre

## Énoncé

Soit $\mathbb{R}$ le corps des nombres réels.
Soit $E = \mathcal{M}_2(\mathbb{R})$ l'espace vectoriel des matrices carrées d'ordre 2 à coefficients réels, muni des lois d'addition matricielle et de multiplication par un scalaire usuelles.
Nous définissons l'application trace, notée $\text{Tr}$, qui à toute matrice $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in E$ associe le scalaire $\text{Tr}(A) = a+d \in \mathbb{R}$.

Considérons l'ensemble $F$ défini par :
$$F = \{ A \in E \mid \text{Tr}(A) = 0 \}$$

1.  Démontrer que $F$ est un sous-espace vectoriel de $E$.
2.  Considérons la famille de matrices $\mathcal{F} = (M_1, M_2, M_3)$ où :
    $$M_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad M_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad M_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$$
    Vérifier que chaque matrice de la famille $\mathcal{F}$ appartient à $F$.
    Démontrer ensuite que la famille $\mathcal{F}$ est une famille libre dans $F$.

## Correction Détaillée

### 1. Démonstration que $F$ est un sous-espace vectoriel de $E$

Pour démontrer que $F$ est un sous-espace vectoriel de $E$, nous devons vérifier trois conditions :
(a) $F$ est non vide.
(b) $F$ est stable par addition vectorielle.
(c) $F$ est stable par multiplication par un scalaire.

Soit $E = \mathcal{M}_2(\mathbb{R})$ l'espace vectoriel des matrices carrées d'ordre 2 à coefficients réels.

**(a) $F$ est non vide :**
Nous devons vérifier que le vecteur nul de $E$, qui est la matrice nulle $0_E = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$, appartient à $F$.
Calculons la trace de $0_E$ :
$\text{Tr}(0_E) = \text{Tr}\left(\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}\right) = 0 + 0 = 0$.
Puisque $\text{Tr}(0_E) = 0$, la matrice nulle $0_E$ appartient à $F$.
Par conséquent, $F$ est non vide.

**(b) $F$ est stable par addition vectorielle :**
Soient $A$ et $B$ deux matrices quelconques appartenant à $F$.
Par définition de $F$, nous avons $\text{Tr}(A) = 0$ et $\text{Tr}(B) = 0$.
Nous devons montrer que la somme $A+B$ appartient également à $F$, c'est-à-dire que $\text{Tr}(A+B) = 0$.
Soient $A = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$ et $B = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$.
Alors $\text{Tr}(A) = a_1 + d_1 = 0$ et $\text{Tr}(B) = a_2 + d_2 = 0$.
La somme $A+B$ est donnée par :
$A+B = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix} + \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} = \begin{pmatrix} a_1+a_2 & b_1+b_2 \\ c_1+c_2 & d_1+d_2 \end{pmatrix}$.
Calculons la trace de $A+B$ :
$\text{Tr}(A+B) = (a_1+a_2) + (d_1+d_2)$.
En réarrangeant les termes, nous obtenons :
$\text{Tr}(A+B) = (a_1+d_1) + (a_2+d_2)$.
Puisque $A \in F$ et $B \in F$, nous savons que $a_1+d_1 = 0$ et $a_2+d_2 = 0$.
Donc, $\text{Tr}(A+B) = 0 + 0 = 0$.
Par conséquent, $A+B \in F$. $F$ est stable par addition vectorielle.

**(c) $F$ est stable par multiplication par un scalaire :**
Soit $\lambda$ un scalaire quelconque appartenant à $\mathbb{R}$ et soit $A$ une matrice quelconque appartenant à $F$.
Par définition de $F$, nous avons $\text{Tr}(A) = 0$.
Nous devons montrer que le produit $\lambda A$ appartient également à $F$, c'est-à-dire que $\text{Tr}(\lambda A) = 0$.
Soit $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Alors $\text{Tr}(A) = a+d = 0$.
Le produit $\lambda A$ est donné par :
$\lambda A = \lambda \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} \lambda a & \lambda b \\ \lambda c & \lambda d \end{pmatrix}$.
Calculons la trace de $\lambda A$ :
$\text{Tr}(\lambda A) = \lambda a + \lambda d$.
En factorisant $\lambda$, nous obtenons :
$\text{Tr}(\lambda A) = \lambda (a+d)$.
Puisque $A \in F$, nous savons que $a+d = 0$.
Donc, $\text{Tr}(\lambda A) = \lambda \cdot 0 = 0$.
Par conséquent, $\lambda A \in F$. $F$ est stable par multiplication par un scalaire.

Les trois conditions étant vérifiées, nous pouvons conclure que $F$ est un sous-espace vectoriel de $E$.

### 2. Vérification de l'appartenance à $F$ et démonstration que $\mathcal{F}$ est une famille libre

**Vérification de l'appartenance des matrices de $\mathcal{F}$ à $F$ :**
Calculons la trace de chaque matrice de la famille $\mathcal{F} = (M_1, M_2, M_3)$ :
Pour $M_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ :
$\text{Tr}(M_1) = 1 + (-1) = 0$. Donc $M_1 \in F$.

Pour $M_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ :
$\text{Tr}(M_2) = 0 + 0 = 0$. Donc $M_2 \in F$.

Pour $M_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ :
$\text{Tr}(M_3) = 0 + 0 = 0$. Donc $M_3 \in F$.

Toutes les matrices de la famille $\mathcal{F}$ appartiennent bien à $F$.

**Démonstration que la famille $\mathcal{F}$ est une famille libre dans $F$ :**
Pour démontrer que la famille $\mathcal{F} = (M_1, M_2, M_3)$ est libre dans $F$ (et donc dans $E$), nous devons montrer que la seule combinaison linéaire de ces matrices qui est égale au vecteur nul de $E$ est celle où tous les coefficients scalaires sont nuls.
Soient $\alpha_1, \alpha_2, \alpha_3$ trois scalaires réels tels que :
$\alpha_1 M_1 + \alpha_2 M_2 + \alpha_3 M_3 = 0_E$.

Substituons les matrices $M_1, M_2, M_3$ dans l'équation :
$\alpha_1 \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + \alpha_2 \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + \alpha_3 \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.

Effectuons la multiplication par les scalaires :
$\begin{pmatrix} \alpha_1 & 0 \\ 0 & -\alpha_1 \end{pmatrix} + \begin{pmatrix} 0 & \alpha_2 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ \alpha_3 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.

Effectuons l'addition des matrices :
$\begin{pmatrix} \alpha_1 + 0 + 0 & 0 + \alpha_2 + 0 \\ 0 + 0 + \alpha_3 & -\alpha_1 + 0 + 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.

Ce qui nous donne la matrice suivante :
$\begin{pmatrix} \alpha_1 & \alpha_2 \\ \alpha_3 & -\alpha_1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$.

Pour que deux matrices soient égales, leurs coefficients correspondants doivent être égaux. Cela nous conduit au système d'équations linéaires suivant :
1.  $\alpha_1 = 0$
2.  $\alpha_2 = 0$
3.  $\alpha_3 = 0$
4.  $-\alpha_1 = 0$

À partir de l'équation (1), nous obtenons directement $\alpha_1 = 0$.
À partir de l'équation (2), nous obtenons directement $\alpha_2 = 0$.
À partir de l'équation (3), nous obtenons directement $\alpha_3 = 0$.
L'équation (4) est $-\alpha_1 = 0$, ce qui est cohérent avec $\alpha_1 = 0$.

Puisque la seule solution à ce système est $\alpha_1 = 0$, $\alpha_2 = 0$, et $\alpha_3 = 0$, nous pouvons conclure que la famille $\mathcal{F} = (M_1, M_2, M_3)$ est une famille libre dans $F$.
