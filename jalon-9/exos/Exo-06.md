# Exercice 6 : Représentation matricielle d'une application linéaire et changement de base
**Difficulté :** ★★★☆☆

## Énoncé
Soit $E = \mathbb{R}^3$ l'espace vectoriel réel muni de sa base canonique $\mathcal{B} = (e_1, e_2, e_3)$, où $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, et $e_3 = (0,0,1)$.

On considère l'application linéaire $f: E \to E$ définie pour tout vecteur $v = (x,y,z) \in E$ par l'expression analytique suivante :
$$f(v) = (x+2y-z, y+z, x-y+2z)$$

On introduit une nouvelle base de $E$, notée $\mathcal{B}' = (u_1, u_2, u_3)$, dont les vecteurs sont donnés par leurs coordonnées dans la base canonique $\mathcal{B}$ :
$$u_1 = (1,1,0)_{\mathcal{B}}, \quad u_2 = (0,1,1)_{\mathcal{B}}, \quad u_3 = (1,0,1)_{\mathcal{B}}$$

1.  Déterminer la matrice $A \in \mathcal{M}_{3,3}(\mathbb{R})$ de l'application linéaire $f$ dans la base canonique $\mathcal{B}$.
2.  Déterminer la matrice de passage $P \in \mathcal{M}_{3,3}(\mathbb{R})$ de la base $\mathcal{B}$ à la base $\mathcal{B}'$. Justifier rigoureusement l'inversibilité de la matrice $P$.
3.  Calculer la matrice inverse $P^{-1} \in \mathcal{M}_{3,3}(\mathbb{R})$.
4.  Déterminer la matrice $B \in \mathcal{M}_{3,3}(\mathbb{R})$ de l'application linéaire $f$ dans la base $\mathcal{B}'$.

## Correction Détaillée

### Question 1 : Détermination de la matrice $A$ de $f$ dans la base canonique $\mathcal{B}$

La matrice $A$ de l'application linéaire $f$ dans la base canonique $\mathcal{B} = (e_1, e_2, e_3)$ est obtenue en exprimant les images des vecteurs de la base $\mathcal{B}$ par $f$ comme colonnes de $A$.
Les vecteurs de la base canonique sont $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, et $e_3 = (0,0,1)$.

Calculons les images de ces vecteurs par $f$:
Pour $e_1 = (1,0,0)$:
$f(e_1) = f(1,0,0) = (1+2(0)-0, 0+0, 1-0+2(0)) = (1,0,1)$.
Ce vecteur est la première colonne de $A$.

Pour $e_2 = (0,1,0)$:
$f(e_2) = f(0,1,0) = (0+2(1)-0, 1+0, 0-1+2(0)) = (2,1,-1)$.
Ce vecteur est la deuxième colonne de $A$.

Pour $e_3 = (0,0,1)$:
$f(e_3) = f(0,0,1) = (0+2(0)-1, 0+1, 0-0+2(1)) = (-1,1,2)$.
Ce vecteur est la troisième colonne de $A$.

Ainsi, la matrice $A$ est :
$$A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 1 \\ 1 & -1 & 2 \end{pmatrix}$$

### Question 2 : Détermination de la matrice de passage $P$ et justification de son inversibilité

La matrice de passage $P$ de la base $\mathcal{B}$ à la base $\mathcal{B}'$ est formée en plaçant les coordonnées des vecteurs de la base $\mathcal{B}'$ exprimées dans la base $\mathcal{B}$ en colonnes.
Les vecteurs de la base $\mathcal{B}'$ sont $u_1 = (1,1,0)$, $u_2 = (0,1,1)$, et $u_3 = (1,0,1)$.

Donc, la matrice $P$ est :
$$P = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

Pour justifier l'inversibilité de $P$, nous devons calculer son déterminant. Une matrice carrée est inversible si et seulement si son déterminant est non nul.
Calculons $\det(P)$ en utilisant le développement par rapport à la première ligne :
$$\det(P) = 1 \cdot \det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} - 0 \cdot \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + 1 \cdot \det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
Calculons les déterminants des sous-matrices $2 \times 2$ :
$\det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = (1 \cdot 1) - (0 \cdot 1) = 1 - 0 = 1$.
$\det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = (1 \cdot 1) - (0 \cdot 0) = 1 - 0 = 1$.
$\det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = (1 \cdot 1) - (1 \cdot 0) = 1 - 0 = 1$.

Substituons ces valeurs dans l'expression du déterminant de $P$:
$$\det(P) = 1 \cdot (1) - 0 \cdot (1) + 1 \cdot (1)$$
$$\det(P) = 1 - 0 + 1$$
$$\det(P) = 2$$
Puisque $\det(P) = 2 \neq 0$, la matrice $P$ est inversible. Cela confirme également que $\mathcal{B}'$ est bien une base de $\mathbb{R}^3$.

### Question 3 : Calcul de la matrice inverse $P^{-1}$

Nous allons utiliser la méthode de la comatrice pour calculer $P^{-1}$. La formule est $P^{-1} = \frac{1}{\det(P)} (\text{com}(P))^T$, où $\text{com}(P)$ est la matrice des cofacteurs de $P$.
Nous avons déjà calculé $\det(P) = 2$.

Calculons les cofacteurs $C_{ij} = (-1)^{i+j} M_{ij}$, où $M_{ij}$ est le mineur de l'élément $P_{ij}$.
$$P = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

**Première ligne :**
$C_{11} = (-1)^{1+1} \det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = +1 \cdot ((1 \cdot 1) - (0 \cdot 1)) = 1 \cdot (1 - 0) = 1$.
$C_{12} = (-1)^{1+2} \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = -1 \cdot ((1 \cdot 1) - (0 \cdot 0)) = -1 \cdot (1 - 0) = -1$.
$C_{13} = (-1)^{1+3} \det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = +1 \cdot ((1 \cdot 1) - (1 \cdot 0)) = 1 \cdot (1 - 0) = 1$.

**Deuxième ligne :**
$C_{21} = (-1)^{2+1} \det \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = -1 \cdot ((0 \cdot 1) - (1 \cdot 1)) = -1 \cdot (0 - 1) = -1 \cdot (-1) = 1$.
$C_{22} = (-1)^{2+2} \det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = +1 \cdot ((1 \cdot 1) - (1 \cdot 0)) = 1 \cdot (1 - 0) = 1$.
$C_{23} = (-1)^{2+3} \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = -1 \cdot ((1 \cdot 1) - (0 \cdot 0)) = -1 \cdot (1 - 0) = -1$.

**Troisième ligne :**
$C_{31} = (-1)^{3+1} \det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = +1 \cdot ((0 \cdot 0) - (1 \cdot 1)) = 1 \cdot (0 - 1) = -1$.
$C_{32} = (-1)^{3+2} \det \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = -1 \cdot ((1 \cdot 0) - (1 \cdot 1)) = -1 \cdot (0 - 1) = -1 \cdot (-1) = 1$.
$C_{33} = (-1)^{3+3} \det \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = +1 \cdot ((1 \cdot 1) - (0 \cdot 1)) = 1 \cdot (1 - 0) = 1$.

La matrice des cofacteurs $\text{com}(P)$ est :
$$\text{com}(P) = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & 1 & 1 \end{pmatrix}$$

La transposée de la matrice des cofacteurs, $(\text{com}(P))^T$, est appelée la matrice adjointe de $P$:
$$(\text{com}(P))^T = \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$$

Enfin, la matrice inverse $P^{-1}$ est :
$$P^{-1} = \frac{1}{\det(P)} (\text{com}(P))^T = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$$
$$P^{-1} = \begin{pmatrix} 1/2 & 1/2 & -1/2 \\ -1/2 & 1/2 & 1/2 \\ 1/2 & -1/2 & 1/2 \end{pmatrix}$$

### Question 4 : Détermination de la matrice $B$ de $f$ dans la base $\mathcal{B}'$

La matrice $B$ de l'application linéaire $f$ dans la base $\mathcal{B}'$ est donnée par la formule de changement de base : $B = P^{-1}AP$.
Nous avons $A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 1 \\ 1 & -1 & 2 \end{pmatrix}$, $P = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$, et $P^{-1} = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix}$.

Commençons par calculer le produit $AP$:
$$AP = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 1 \\ 1 & -1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$
Calcul de chaque élément de $AP$:
$(AP)_{11} = (1)(1) + (2)(1) + (-1)(0) = 1+2+0 = 3$.
$(AP)_{12} = (1)(0) + (2)(1) + (-1)(1) = 0+2-1 = 1$.
$(AP)_{13} = (1)(1) + (2)(0) + (-1)(1) = 1+0-1 = 0$.

$(AP)_{21} = (0)(1) + (1)(1) + (1)(0) = 0+1+0 = 1$.
$(AP)_{22} = (0)(0) + (1)(1) + (1)(1) = 0+1+1 = 2$.
$(AP)_{23} = (0)(1) + (1)(0) + (1)(1) = 0+0+1 = 1$.

$(AP)_{31} = (1)(1) + (-1)(1) + (2)(0) = 1-1+0 = 0$.
$(AP)_{32} = (1)(0) + (-1)(1) + (2)(1) = 0-1+2 = 1$.
$(AP)_{33} = (1)(1) + (-1)(0) + (2)(1) = 1+0+2 = 3$.

Donc, la matrice $AP$ est :
$$AP = \begin{pmatrix} 3 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 3 \end{pmatrix}$$

Maintenant, calculons $B = P^{-1}(AP)$:
$$B = \frac{1}{2} \begin{pmatrix} 1 & 1 & -1 \\ -1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix} \begin{pmatrix} 3 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 3 \end{pmatrix}$$
Calcul de chaque élément de $2B$:
$(2B)_{11} = (1)(3) + (1)(1) + (-1)(0) = 3+1+0 = 4$.
$(2B)_{12} = (1)(1) + (1)(2) + (-1)(1) = 1+2-1 = 2$.
$(2B)_{13} = (1)(0) + (1)(1) + (-1)(3) = 0+1-3 = -2$.

$(2B)_{21} = (-1)(3) + (1)(1) + (1)(0) = -3+1+0 = -2$.
$(2B)_{22} = (-1)(1) + (1)(2) + (1)(1) = -1+2+1 = 2$.
$(2B)_{23} = (-1)(0) + (1)(1) + (1)(3) = 0+1+3 = 4$.

$(2B)_{31} = (1)(3) + (-1)(1) + (1)(0) = 3-1+0 = 2$.
$(2B)_{32} = (1)(1) + (-1)(2) + (1)(1) = 1-2+1 = 0$.
$(2B)_{33} = (1)(0) + (-1)(1) + (1)(3) = 0-1+3 = 2$.

Donc, la matrice $2B$ est :
$$2B = \begin{pmatrix} 4 & 2 & -2 \\ -2 & 2 & 4 \\ 2 & 0 & 2 \end{pmatrix}$$
Enfin, en divisant par 2, nous obtenons la matrice $B$:
$$B = \begin{pmatrix} 2 & 1 & -1 \\ -1 & 1 & 2 \\ 1 & 0 & 1 \end{pmatrix}$$


**Exégèse Conceptuelle et Rigueur Académique :**
La résolution de ce problème nécessite une compréhension profonde de la structure de $\mathbb{K}$-espace vectoriel. Il ne suffit pas d'appliquer aveuglément les formules. Soit $E$ un espace vectoriel sur le corps commutatif $\mathbb{K}$. Considérons un endomorphisme $u \in \mathcal{L}(E)$. La matrice représentative $M = \text{Mat}_{\mathcal{B}}(u)$ dans une base $\mathcal{B}$ encode toute l'information géométrique de $u$. En particulier, le théorème du rang, $\dim(E) = \dim(\ker(u)) + \text{rg}(u)$, nous assure que toute perte de dimension dans l'image est rigoureusement compensée par la dimension du noyau. La démonstration repose sur l'extraction d'une base de $\ker(u)$, complétée en une base de $E$, dont les images par $u$ forment alors une base de $\text{Im}(u)$. Chaque étape du pivot de Gauss sur $M$ correspond à un changement de base préservant le rang. Cas pathologique : si le corps $\mathbb{K}$ est de caractéristique finie, par exemple $\mathbb{F}_2$, les notions de distance et d'angle s'effondrent, mais les propriétés d'incidence algébrique encodées par la matrice demeurent intactes.
