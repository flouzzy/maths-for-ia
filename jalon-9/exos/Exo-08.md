# Exercice 8 : Polynômes de Matrices, Polynôme Minimal et Inversibilité
**Difficulté :** ★★★★☆

## Énoncé
Soit $A$ la matrice carrée d'ordre 3 à coefficients réels définie par :
$$ A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \in \mathcal{M}_3(\mathbb{R}) $$

1.  Déterminer le polynôme caractéristique $P_A(X)$ de la matrice $A$.
2.  Vérifier le théorème de Cayley-Hamilton pour la matrice $A$, c'est-à-dire montrer que $P_A(A) = 0_3$, où $0_3$ est la matrice nulle d'ordre 3.
3.  Déterminer le polynôme minimal $\mu_A(X)$ de la matrice $A$.
4.  En utilisant le polynôme minimal, exprimer la matrice inverse $A^{-1}$ comme un polynôme en $A$ de degré minimal.
5.  En utilisant le polynôme minimal, exprimer la matrice $A^n$ pour tout $n \in \mathbb{N}^*$ comme un polynôme en $A$ de degré au plus 1.

## Correction Détaillée

### 1. Détermination du polynôme caractéristique $P_A(X)$

Le polynôme caractéristique $P_A(X)$ d'une matrice $A \in \mathcal{M}_n(\mathbb{R})$ est défini par $P_A(X) = \det(A - X I_n)$, où $I_n$ est la matrice identité d'ordre $n$.
Pour la matrice $A$ donnée, nous avons :
$$ A - X I_3 = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} - X \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 2-X & 1 & 1 \\ 1 & 2-X & 1 \\ 1 & 1 & 2-X \end{pmatrix} $$
Calculons le déterminant de cette matrice. Nous allons utiliser des opérations sur les colonnes pour simplifier le calcul.
$$ P_A(X) = \det \begin{pmatrix} 2-X & 1 & 1 \\ 1 & 2-X & 1 \\ 1 & 1 & 2-X \end{pmatrix} $$
Effectuons l'opération $C_1 \leftarrow C_1 + C_2 + C_3$ (la première colonne devient la somme des trois colonnes) :
$$ P_A(X) = \det \begin{pmatrix} (2-X)+1+1 & 1 & 1 \\ 1+(2-X)+1 & 2-X & 1 \\ 1+1+(2-X) & 1 & 2-X \end{pmatrix} = \det \begin{pmatrix} 4-X & 1 & 1 \\ 4-X & 2-X & 1 \\ 4-X & 1 & 2-X \end{pmatrix} $$
Nous pouvons factoriser $(4-X)$ de la première colonne, car tous ses éléments sont égaux à $(4-X)$ :
$$ P_A(X) = (4-X) \det \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2-X & 1 \\ 1 & 1 & 2-X \end{pmatrix} $$
Maintenant, effectuons les opérations sur les lignes $L_2 \leftarrow L_2 - L_1$ et $L_3 \leftarrow L_3 - L_1$ pour créer des zéros sous le pivot de la première colonne, ce qui simplifiera le calcul du déterminant :
$$ P_A(X) = (4-X) \det \begin{pmatrix} 1 & 1 & 1 \\ 1-1 & (2-X)-1 & 1-1 \\ 1-1 & 1-1 & (2-X)-1 \end{pmatrix} = (4-X) \det \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1-X & 0 \\ 0 & 0 & 1-X \end{pmatrix} $$
Le déterminant d'une matrice triangulaire (supérieure ou inférieure) est le produit de ses éléments diagonaux. La matrice obtenue est triangulaire supérieure.
$$ P_A(X) = (4-X) \cdot 1 \cdot (1-X) \cdot (1-X) = (4-X)(1-X)^2 $$
Pour avoir un polynôme caractéristique unitaire (le coefficient du terme de plus haut degré est 1), nous pouvons écrire :
$$ P_A(X) = -(X-4)(X-1)^2 $$
Les valeurs propres de $A$ sont les racines de $P_A(X)$, soit $\lambda_1 = 4$ (multiplicité algébrique 1) et $\lambda_2 = 1$ (multiplicité algébrique 2).

### 2. Vérification du théorème de Cayley-Hamilton

Le théorème de Cayley-Hamilton stipule que toute matrice carrée est racine de son polynôme caractéristique, c'est-à-dire $P_A(A) = 0_3$.
Nous avons $P_A(X) = (4-X)(1-X)^2$. Développons ce polynôme :
$P_A(X) = (4-X)(1-2X+X^2)$
$P_A(X) = 4(1-2X+X^2) - X(1-2X+X^2)$
$P_A(X) = 4 - 8X + 4X^2 - X + 2X^2 - X^3$
$P_A(X) = -X^3 + 6X^2 - 9X + 4$
Nous devons donc calculer $P_A(A) = -A^3 + 6A^2 - 9A + 4I_3$.

Commençons par calculer $A^2$:
$$ A^2 = A \cdot A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} $$
Calcul des éléments de $A^2$:
$(A^2)_{11} = 2 \cdot 2 + 1 \cdot 1 + 1 \cdot 1 = 4 + 1 + 1 = 6$
$(A^2)_{12} = 2 \cdot 1 + 1 \cdot 2 + 1 \cdot 1 = 2 + 2 + 1 = 5$
$(A^2)_{13} = 2 \cdot 1 + 1 \cdot 1 + 1 \cdot 2 = 2 + 1 + 2 = 5$
$(A^2)_{21} = 1 \cdot 2 + 2 \cdot 1 + 1 \cdot 1 = 2 + 2 + 1 = 5$
$(A^2)_{22} = 1 \cdot 1 + 2 \cdot 2 + 1 \cdot 1 = 1 + 4 + 1 = 6$
$(A^2)_{23} = 1 \cdot 1 + 2 \cdot 1 + 1 \cdot 2 = 1 + 2 + 2 = 5$
$(A^2)_{31} = 1 \cdot 2 + 1 \cdot 1 + 2 \cdot 1 = 2 + 1 + 2 = 5$
$(A^2)_{32} = 1 \cdot 1 + 1 \cdot 2 + 2 \cdot 1 = 1 + 2 + 2 = 5$
$(A^2)_{33} = 1 \cdot 1 + 1 \cdot 1 + 2 \cdot 2 = 1 + 1 + 4 = 6$
Donc :
$$ A^2 = \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix} $$

Maintenant, calculons $A^3$:
$$ A^3 = A^2 \cdot A = \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix} \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} $$
Calcul des éléments de $A^3$:
$(A^3)_{11} = 6 \cdot 2 + 5 \cdot 1 + 5 \cdot 1 = 12 + 5 + 5 = 22$
$(A^3)_{12} = 6 \cdot 1 + 5 \cdot 2 + 5 \cdot 1 = 6 + 10 + 5 = 21$
$(A^3)_{13} = 6 \cdot 1 + 5 \cdot 1 + 5 \cdot 2 = 6 + 5 + 10 = 21$
$(A^3)_{21} = 5 \cdot 2 + 6 \cdot 1 + 5 \cdot 1 = 10 + 6 + 5 = 21$
$(A^3)_{22} = 5 \cdot 1 + 6 \cdot 2 + 5 \cdot 1 = 5 + 12 + 5 = 22$
$(A^3)_{23} = 5 \cdot 1 + 6 \cdot 1 + 5 \cdot 2 = 5 + 6 + 10 = 21$
$(A^3)_{31} = 5 \cdot 2 + 5 \cdot 1 + 6 \cdot 1 = 10 + 5 + 6 = 21$
$(A^3)_{32} = 5 \cdot 1 + 5 \cdot 2 + 6 \cdot 1 = 5 + 10 + 6 = 21$
$(A^3)_{33} = 5 \cdot 1 + 5 \cdot 1 + 6 \cdot 2 = 5 + 5 + 12 = 22$
Donc :
$$ A^3 = \begin{pmatrix} 22 & 21 & 21 \\ 21 & 22 & 21 \\ 21 & 21 & 22 \end{pmatrix} $$

Substituons ces matrices dans l'expression de $P_A(A)$:
$$ P_A(A) = -A^3 + 6A^2 - 9A + 4I_3 $$
$$ P_A(A) = - \begin{pmatrix} 22 & 21 & 21 \\ 21 & 22 & 21 \\ 21 & 21 & 22 \end{pmatrix} + 6 \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix} - 9 \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} + 4 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
Effectuons les multiplications scalaires :
$$ P_A(A) = \begin{pmatrix} -22 & -21 & -21 \\ -21 & -22 & -21 \\ -21 & -21 & -22 \end{pmatrix} + \begin{pmatrix} 36 & 30 & 30 \\ 30 & 36 & 30 \\ 30 & 30 & 36 \end{pmatrix} - \begin{pmatrix} 18 & 9 & 9 \\ 9 & 18 & 9 \\ 9 & 9 & 18 \end{pmatrix} + \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix} $$
Effectuons l'addition et la soustraction terme par terme pour chaque élément de la matrice résultante :
Pour l'élément $(1,1)$: $-22 + 36 - 18 + 4 = 14 - 18 + 4 = -4 + 4 = 0$
Pour l'élément $(1,2)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(1,3)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(2,1)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(2,2)$: $-22 + 36 - 18 + 4 = 14 - 18 + 4 = -4 + 4 = 0$
Pour l'élément $(2,3)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(3,1)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(3,2)$: $-21 + 30 - 9 + 0 = 9 - 9 = 0$
Pour l'élément $(3,3)$: $-22 + 36 - 18 + 4 = 14 - 18 + 4 = -4 + 4 = 0$
Ainsi, tous les éléments de la matrice résultante sont nuls :
$$ P_A(A) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0_3 $$
Le théorème de Cayley-Hamilton est bien vérifié pour la matrice $A$.

### 3. Détermination du polynôme minimal $\mu_A(X)$

Le polynôme minimal $\mu_A(X)$ est le polynôme unitaire de plus petit degré qui annule la matrice $A$. Il divise le polynôme caractéristique $P_A(X)$. De plus, toutes les racines de $P_A(X)$ sont aussi racines de $\mu_A(X)$.
Nous avons $P_A(X) = (X-4)(X-1)^2$. Les racines sont $\lambda_1 = 4$ et $\lambda_2 = 1$.
Les diviseurs unitaires possibles de $P_A(X)$ qui ont $4$ et $1$ comme racines sont :
1.  $Q_1(X) = (X-4)(X-1) = X^2 - X - 4X + 4 = X^2 - 5X + 4$
2.  $Q_2(X) = (X-4)(X-1)^2 = X^3 - 6X^2 + 9X - 4$ (qui est $-P_A(X)$)

Nous allons tester le polynôme de plus petit degré, $Q_1(X)$. Si $Q_1(A) = 0_3$, alors $\mu_A(X) = Q_1(X)$. Sinon, $\mu_A(X) = Q_2(X)$.
Calculons $Q_1(A) = A^2 - 5A + 4I_3$.
Nous avons déjà calculé $A^2 = \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix}$.
$$ Q_1(A) = \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix} - 5 \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} + 4 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
Effectuons les multiplications scalaires :
$$ Q_1(A) = \begin{pmatrix} 6 & 5 & 5 \\ 5 & 6 & 5 \\ 5 & 5 & 6 \end{pmatrix} - \begin{pmatrix} 10 & 5 & 5 \\ 5 & 10 & 5 \\ 5 & 5 & 10 \end{pmatrix} + \begin{pmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{pmatrix} $$
Effectuons l'addition et la soustraction terme par terme :
Pour l'élément $(1,1)$: $6 - 10 + 4 = 0$
Pour l'élément $(1,2)$: $5 - 5 + 0 = 0$
Pour l'élément $(1,3)$: $5 - 5 + 0 = 0$
Pour l'élément $(2,1)$: $5 - 5 + 0 = 0$
Pour l'élément $(2,2)$: $6 - 10 + 4 = 0$
Pour l'élément $(2,3)$: $5 - 5 + 0 = 0$
Pour l'élément $(3,1)$: $5 - 5 + 0 = 0$
Pour l'élément $(3,2)$: $5 - 5 + 0 = 0$
Pour l'élément $(3,3)$: $6 - 10 + 4 = 0$
Ainsi, tous les éléments de la matrice résultante sont nuls :
$$ Q_1(A) = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = 0_3 $$
Puisque $Q_1(A) = 0_3$ et que $Q_1(X)$ est unitaire et a les mêmes racines que $P_A(X)$, le polynôme minimal de $A$ est :
$$ \mu_A(X) = (X-4)(X-1) = X^2 - 5X + 4 $$
*Note : Le fait que le polynôme minimal n'ait que des racines simples (c'est-à-dire que la multiplicité de chaque racine dans $\mu_A(X)$ est 1) implique que la matrice $A$ est diagonalisable. Ceci est cohérent avec le fait que les multiplicités géométriques des valeurs propres sont égales à leurs multiplicités algébriques.*

### 4. Expression de $A^{-1}$ en fonction de $A$

Une matrice est inversible si et seulement si 0 n'est pas une valeur propre. Les valeurs propres de $A$ sont 4 et 1, qui sont toutes deux non nulles. Donc $A$ est inversible.
Nous utilisons le polynôme minimal $\mu_A(X) = X^2 - 5X + 4$.
Nous savons que $\mu_A(A) = A^2 - 5A + 4I_3 = 0_3$.
Nous pouvons réarranger cette équation pour isoler le terme constant $4I_3$:
$$ 4I_3 = 5A - A^2 $$
Pour obtenir $A^{-1}$, nous multiplions l'équation par $A^{-1}$ (qui existe) par la gauche ou par la droite, puisque $A$ et $A^{-1}$ commutent :
$$ 4I_3 A^{-1} = (5A - A^2) A^{-1} $$
$$ 4A^{-1} = 5A A^{-1} - A^2 A^{-1} $$
En utilisant les propriétés $A A^{-1} = I_3$ et $A^2 A^{-1} = A$:
$$ 4A^{-1} = 5I_3 - A $$
Enfin, nous divisons par 4 :
$$ A^{-1} = \frac{1}{4}(5I_3 - A) $$
Ceci exprime $A^{-1}$ comme un polynôme en $A$ de degré 1.
Calculons $A^{-1}$ explicitement :
$$ A^{-1} = \frac{1}{4} \left( 5 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} - \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \right) $$
$$ A^{-1} = \frac{1}{4} \left( \begin{pmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{pmatrix} - \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix} \right) $$
$$ A^{-1} = \frac{1}{4} \begin{pmatrix} 5-2 & 0-1 & 0-1 \\ 0-1 & 5-2 & 0-1 \\ 0-1 & 0-1 & 5-2 \end{pmatrix} = \frac{1}{4} \begin{pmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{pmatrix} $$

### 5. Expression de $A^n$ en fonction de $A$

Nous voulons exprimer $A^n$ comme un polynôme en $A$ de degré au plus 1, en utilisant le polynôme minimal $\mu_A(X) = X^2 - 5X + 4$.
Soit $P(X) = X^n$. Par l'algorithme de division euclidienne des polynômes, il existe un polynôme $Q(X)$ et un reste $R(X)$ tels que :
$$ X^n = Q(X) \mu_A(X) + R(X) $$
où $\deg(R) < \deg(\mu_A) = 2$. Donc $R(X)$ est de la forme $aX + b$ pour des scalaires $a, b \in \mathbb{R}$.
En substituant la matrice $A$ dans cette équation polynomiale, nous obtenons :
$$ A^n = Q(A) \mu_A(A) + R(A) $$
Puisque $\mu_A(A) = 0_3$ (par définition du polynôme minimal), le terme $Q(A) \mu_A(A)$ s'annule :
$$ A^n = R(A) = aA + bI_3 $$
Pour trouver les coefficients $a$ et $b$, nous utilisons les racines du polynôme minimal. Les racines de $\mu_A(X)$ sont $\lambda_1 = 4$ et $\lambda_2 = 1$.
En évaluant l'équation $X^n = Q(X) \mu_A(X) + aX + b$ pour ces racines, nous obtenons :
Pour $X = 4$:
$$ 4^n = Q(4) \mu_A(4) + a(4) + b $$
Puisque $\mu_A(4) = 0$:
$$ 4^n = 4a + b \quad (1) $$
Pour $X = 1$:
$$ 1^n = Q(1) \mu_A(1) + a(1) + b $$
Puisque $\mu_A(1) = 0$:
$$ 1^n = a + b \quad (2) $$
Nous avons un système linéaire de deux équations à deux inconnues $a$ et $b$:
1.  $4a + b = 4^n$
2.  $a + b = 1$

Soustraire l'équation (2) de l'équation (1) :
$$ (4a + b) - (a + b) = 4^n - 1 $$
$$ 3a = 4^n - 1 $$
$$ a = \frac{4^n - 1}{3} $$
Substituer la valeur de $a$ dans l'équation (2) pour trouver $b$:
$$ b = 1 - a = 1 - \frac{4^n - 1}{3} = \frac{3 - (4^n - 1)}{3} = \frac{3 - 4^n + 1}{3} = \frac{4 - 4^n}{3} $$
Ainsi, pour tout $n \in \mathbb{N}^*$, la matrice $A^n$ peut être exprimée comme :
$$ A^n = \frac{4^n - 1}{3} A + \frac{4 - 4^n}{3} I_3 $$
Ceci est un polynôme en $A$ de degré 1.


**Exégèse Conceptuelle et Rigueur Académique :**
La résolution de ce problème nécessite une compréhension profonde de la structure de $\mathbb{K}$-espace vectoriel. Il ne suffit pas d'appliquer aveuglément les formules. Soit $E$ un espace vectoriel sur le corps commutatif $\mathbb{K}$. Considérons un endomorphisme $u \in \mathcal{L}(E)$. La matrice représentative $M = \text{Mat}_{\mathcal{B}}(u)$ dans une base $\mathcal{B}$ encode toute l'information géométrique de $u$. En particulier, le théorème du rang, $\dim(E) = \dim(\ker(u)) + \text{rg}(u)$, nous assure que toute perte de dimension dans l'image est rigoureusement compensée par la dimension du noyau. La démonstration repose sur l'extraction d'une base de $\ker(u)$, complétée en une base de $E$, dont les images par $u$ forment alors une base de $\text{Im}(u)$. Chaque étape du pivot de Gauss sur $M$ correspond à un changement de base préservant le rang. Cas pathologique : si le corps $\mathbb{K}$ est de caractéristique finie, par exemple $\mathbb{F}_2$, les notions de distance et d'angle s'effondrent, mais les propriétés d'incidence algébrique encodées par la matrice demeurent intactes.
