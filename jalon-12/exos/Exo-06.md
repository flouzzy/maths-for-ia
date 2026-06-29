# Exercice 06 (3 $\star$) : Optimisation de la Représentativité Sémantique par Similarité Cosinus et Formes Quadratiques

## Énoncé
Soit $E$ un espace vectoriel euclidien de dimension $n \ge 1$, muni du produit scalaire $\langle \cdot, \cdot \rangle$ et de la norme associée $\|\cdot\|$.
On dispose d'un ensemble de $k$ vecteurs non nuls $\mathbf{u}_1, \dots, \mathbf{u}_k \in E$, représentant des "ancres sémantiques" ou des "caractéristiques de recherche". Pour chaque $i \in \{1, \dots, k\}$, on définit le vecteur normalisé $\mathbf{v}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}$.
Nous cherchons à déterminer un vecteur $\mathbf{x} \in E$, de norme unité (c'est-à-dire $\|\mathbf{x}\|=1$), qui maximise la somme des carrés des similarités cosinus avec les vecteurs $\mathbf{u}_i$. Ce vecteur $\mathbf{x}$ peut être interprété comme une "représentation sémantique optimale" ou un "document idéal" par rapport aux ancres données.

1.  Montrer que le problème revient à maximiser la fonction $f(\mathbf{x}) = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2$ sous la contrainte $\|\mathbf{x}\|=1$.
2.  Démontrer que la fonction $f(\mathbf{x})$ peut s'écrire sous la forme $f(\mathbf{x}) = \langle \mathbf{x}, M\mathbf{x} \rangle$ pour une certaine application linéaire symétrique $M: E \to E$ que l'on explicitera. Préciser la nature de $M$ (positive, définie positive, etc.).
3.  Justifier l'existence d'un maximum pour $f(\mathbf{x})$ sur la sphère unité $S^{n-1} = \{\mathbf{x} \in E \mid \|\mathbf{x}\|=1\}$.
4.  Déterminer la valeur maximale de $f(\mathbf{x})$ et caractériser l'ensemble des vecteurs $\mathbf{x}$ qui atteignent ce maximum.
5.  Dans le cas particulier où $E = \mathbb{R}^2$ muni du produit scalaire canonique, et les vecteurs normalisés sont $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$, $\mathbf{v}_3 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, calculer la matrice de $M$ dans la base canonique et trouver le vecteur $\mathbf{x}$ optimal (à un signe près).

## Correction Détaillée
### Analyse et Stratégie
Le problème nous demande de maximiser une somme de carrés de similarités cosinus. La similarité cosinus entre deux vecteurs $\mathbf{a}$ et $\mathbf{b}$ est définie par $\text{sim}(\mathbf{a}, \mathbf{b}) = \frac{\langle \mathbf{a}, \mathbf{b} \rangle}{\|\mathbf{a}\| \|\mathbf{b}\|}$. La contrainte $\|\mathbf{x}\|=1$ simplifiera considérablement l'expression de la fonction à maximiser.

La première étape consistera à reformuler la fonction objectif en utilisant la définition des vecteurs normalisés $\mathbf{v}_i$.
Ensuite, nous devrons exprimer cette fonction sous la forme d'une forme quadratique $\langle \mathbf{x}, M\mathbf{x} \rangle$. Cela implique de construire l'opérateur linéaire symétrique $M$ à partir des vecteurs $\mathbf{v}_i$. La nature de $M$ (positive, définie positive) sera étudiée en examinant le signe de la forme quadratique associée.

Pour justifier l'existence d'un maximum, nous nous appuierons sur des résultats fondamentaux de l'analyse fonctionnelle sur les espaces euclidiens, notamment le théorème de Weierstrass (ou théorème des bornes atteintes) qui s'applique aux fonctions continues sur des ensembles compacts.

La détermination du maximum et des vecteurs qui l'atteignent relève de la théorie des formes quadratiques et des opérateurs linéaires symétriques. Le problème de la maximisation d'une forme quadratique $\langle \mathbf{x}, M\mathbf{x} \rangle$ sous la contrainte $\|\mathbf{x}\|=1$ est un problème classique de valeurs propres (quotient de Rayleigh). Le maximum sera la plus grande valeur propre de $M$, et les vecteurs optimaux seront les vecteurs propres associés à cette valeur propre maximale, normalisés.

Enfin, la dernière partie est une application concrète de la théorie développée, nécessitant le calcul explicite de la matrice $M$ et de ses éléments propres dans un cas bidimensionnel.

### Résolution Pas-à-Pas

#### 1. Reformulation du problème
Le problème consiste à maximiser la fonction $g(\mathbf{x}) = \sum_{i=1}^k \left( \frac{\langle \mathbf{x}, \mathbf{u}_i \rangle}{\|\mathbf{x}\| \|\mathbf{u}_i\|} \right)^2$ sous la contrainte $\|\mathbf{x}\|=1$.
Puisque $\|\mathbf{x}\|=1$, l'expression de la similarité cosinus au carré se simplifie :
$$ \left( \frac{\langle \mathbf{x}, \mathbf{u}_i \rangle}{\|\mathbf{x}\| \|\mathbf{u}_i\|} \right)^2 = \frac{\langle \mathbf{x}, \mathbf{u}_i \rangle^2}{\|\mathbf{x}\|^2 \|\mathbf{u}_i\|^2} = \frac{\langle \mathbf{x}, \mathbf{u}_i \rangle^2}{1 \cdot \|\mathbf{u}_i\|^2} = \left\langle \mathbf{x}, \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|} \right\rangle^2 $$
En utilisant la définition $\mathbf{v}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}$, qui sont des vecteurs de norme unité, l'expression devient :
$$ \left\langle \mathbf{x}, \mathbf{v}_i \right\rangle^2 $$
Par conséquent, la fonction à maximiser sous la contrainte $\|\mathbf{x}\|=1$ est bien :
$$ f(\mathbf{x}) = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2 $$

#### 2. Expression sous forme quadratique et propriétés de $M$
Soit $(\mathbf{e}_1, \dots, \mathbf{e}_n)$ une base orthonormée de $E$. Tout vecteur $\mathbf{x} \in E$ peut s'écrire $\mathbf{x} = \sum_{j=1}^n x_j \mathbf{e}_j$, où $x_j = \langle \mathbf{x}, \mathbf{e}_j \rangle$. De même, chaque $\mathbf{v}_i$ peut s'écrire $\mathbf{v}_i = \sum_{j=1}^n v_{ij} \mathbf{e}_j$, où $v_{ij} = \langle \mathbf{v}_i, \mathbf{e}_j \rangle$.
Le produit scalaire $\langle \mathbf{x}, \mathbf{v}_i \rangle$ s'écrit alors :
$$ \langle \mathbf{x}, \mathbf{v}_i \rangle = \left\langle \sum_{j=1}^n x_j \mathbf{e}_j, \sum_{l=1}^n v_{il} \mathbf{e}_l \right\rangle = \sum_{j=1}^n \sum_{l=1}^n x_j v_{il} \langle \mathbf{e}_j, \mathbf{e}_l \rangle = \sum_{j=1}^n x_j v_{ij} $$
Le carré de ce produit scalaire est :
$$ \langle \mathbf{x}, \mathbf{v}_i \rangle^2 = \left( \sum_{j=1}^n x_j v_{ij} \right) \left( \sum_{l=1}^n x_l v_{il} \right) = \sum_{j=1}^n \sum_{l=1}^n x_j x_l v_{ij} v_{il} $$
En sommant sur $i$ de $1$ à $k$, nous obtenons :
$$ f(\mathbf{x}) = \sum_{i=1}^k \sum_{j=1}^n \sum_{l=1}^n x_j x_l v_{ij} v_{il} = \sum_{j=1}^n \sum_{l=1}^n \left( \sum_{i=1}^k v_{ij} v_{il} \right) x_j x_l $$
Cette expression est une forme quadratique. On peut l'écrire sous la forme $\langle \mathbf{x}, M\mathbf{x} \rangle$, où $M$ est une application linéaire de $E$ dans $E$. Dans la base orthonormée $(\mathbf{e}_1, \dots, \mathbf{e}_n)$, la matrice associée à $M$, notée $[M]$, a pour coefficients $M_{jl}$ :
$$ M_{jl} = \sum_{i=1}^k v_{ij} v_{il} $$
On peut également exprimer $M$ de manière plus abstraite. Pour tout $\mathbf{y} \in E$, l'opérateur $M$ est défini par :
$$ M\mathbf{y} = \sum_{i=1}^k \langle \mathbf{y}, \mathbf{v}_i \rangle \mathbf{v}_i $$
Vérifions que $f(\mathbf{x}) = \langle \mathbf{x}, M\mathbf{x} \rangle$ avec cette définition de $M$:
$$ \langle \mathbf{x}, M\mathbf{x} \rangle = \left\langle \mathbf{x}, \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle \mathbf{v}_i \right\rangle = \sum_{i=1}^k \langle \mathbf{x}, \langle \mathbf{x}, \mathbf{v}_i \rangle \mathbf{v}_i \rangle $$
Par linéarité du produit scalaire par rapport au second argument, on a $\langle \mathbf{x}, c\mathbf{y} \rangle = c \langle \mathbf{x}, \mathbf{y} \rangle$. Donc :
$$ \langle \mathbf{x}, M\mathbf{x} \rangle = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle \langle \mathbf{x}, \mathbf{v}_i \rangle = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2 = f(\mathbf{x}) $$
L'application linéaire $M$ est donc bien définie par $M\mathbf{y} = \sum_{i=1}^k \langle \mathbf{y}, \mathbf{v}_i \rangle \mathbf{v}_i$.

**Nature de $M$ :**
1.  **Symétrie :** Pour montrer que $M$ est symétrique, nous devons vérifier que $\langle M\mathbf{y}, \mathbf{z} \rangle = \langle \mathbf{y}, M\mathbf{z} \rangle$ pour tous $\mathbf{y}, \mathbf{z} \in E$.
    $$ \langle M\mathbf{y}, \mathbf{z} \rangle = \left\langle \sum_{i=1}^k \langle \mathbf{y}, \mathbf{v}_i \rangle \mathbf{v}_i, \mathbf{z} \right\rangle = \sum_{i=1}^k \langle \mathbf{y}, \mathbf{v}_i \rangle \langle \mathbf{v}_i, \mathbf{z} \rangle $$
    $$ \langle \mathbf{y}, M\mathbf{z} \rangle = \left\langle \mathbf{y}, \sum_{i=1}^k \langle \mathbf{z}, \mathbf{v}_i \rangle \mathbf{v}_i \right\rangle = \sum_{i=1}^k \langle \mathbf{z}, \mathbf{v}_i \rangle \langle \mathbf{y}, \mathbf{v}_i \rangle $$
    Puisque $\langle \mathbf{v}_i, \mathbf{z} \rangle = \langle \mathbf{z}, \mathbf{v}_i \rangle$ (symétrie du produit scalaire), on a bien $\langle M\mathbf{y}, \mathbf{z} \rangle = \langle \mathbf{y}, M\mathbf{z} \rangle$. Donc $M$ est un opérateur symétrique.

2.  **Positivité :** Un opérateur symétrique $M$ est dit positif si $\langle \mathbf{x}, M\mathbf{x} \rangle \ge 0$ pour tout $\mathbf{x} \in E$.
    Nous avons montré que $\langle \mathbf{x}, M\mathbf{x} \rangle = f(\mathbf{x}) = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2$.
    Puisque $\langle \mathbf{x}, \mathbf{v}_i \rangle^2 \ge 0$ pour chaque $i$, la somme est également non négative :
    $$ \langle \mathbf{x}, M\mathbf{x} \rangle \ge 0 \quad \text{pour tout } \mathbf{x} \in E $$
    Donc $M$ est un opérateur symétrique positif.

3.  **Définie positivité :** Un opérateur symétrique $M$ est dit défini positif si $\langle \mathbf{x}, M\mathbf{x} \rangle > 0$ pour tout $\mathbf{x} \ne \mathbf{0}$.
    Dans notre cas, $\langle \mathbf{x}, M\mathbf{x} \rangle = 0$ si et seulement si $\sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2 = 0$. Cela implique que $\langle \mathbf{x}, \mathbf{v}_i \rangle = 0$ pour tout $i \in \{1, \dots, k\}$.
    Ceci signifie que $\mathbf{x}$ est orthogonal à tous les vecteurs $\mathbf{v}_i$. Si les vecteurs $\mathbf{v}_1, \dots, \mathbf{v}_k$ engendrent tout l'espace $E$ (c'est-à-dire si $\text{span}(\mathbf{v}_1, \dots, \mathbf{v}_k) = E$), alors le seul vecteur orthogonal à tous les $\mathbf{v}_i$ est le vecteur nul $\mathbf{0}$. Dans ce cas, $M$ serait défini positif.
    Cependant, si $\text{span}(\mathbf{v}_1, \dots, \mathbf{v}_k) \ne E$, alors il existe des vecteurs non nuls $\mathbf{x}$ qui sont orthogonaux à tous les $\mathbf{v}_i$. Pour de tels vecteurs, $\langle \mathbf{x}, M\mathbf{x} \rangle = 0$. Par conséquent, $M$ n'est pas nécessairement défini positif ; il est seulement positif.

#### 3. Justification de l'existence d'un maximum
La fonction $f(\mathbf{x}) = \sum_{i=1}^k \langle \mathbf{x}, \mathbf{v}_i \rangle^2$ est une fonction polynomiale des coordonnées de $\mathbf{x}$ dans n'importe quelle base orthonormée de $E$. Les fonctions polynomiales sont continues sur $E$.
L'ensemble de contrainte est la sphère unité $S^{n-1} = \{\mathbf{x} \in E \mid \|\mathbf{x}\|=1\}$.
Dans un espace euclidien de dimension finie $E$, la sphère unité $S^{n-1}$ est un ensemble fermé et borné. Par le théorème de Heine-Borel, tout ensemble fermé et borné dans un espace euclidien de dimension finie est compact. Donc $S^{n-1}$ est un ensemble compact.
Le théorème de Weierstrass (ou théorème des bornes atteintes) stipule que toute fonction continue sur un ensemble compact atteint son maximum et son minimum sur cet ensemble.
Puisque $f(\mathbf{x})$ est continue et $S^{n-1}$ est compact, il existe au moins un vecteur $\mathbf{x}_0 \in S^{n-1}$ tel que $f(\mathbf{x}_0)$ est la valeur maximale de $f$ sur $S^{n-1}$.

#### 4. Détermination de la valeur maximale et des vecteurs optimaux
Nous cherchons à maximiser $f(\mathbf{x}) = \langle \mathbf{x}, M\mathbf{x} \rangle$ sous la contrainte $\|\mathbf{x}\|=1$.
Ceci est un problème classique de valeurs propres. Puisque $M$ est un opérateur symétrique sur un espace euclidien de dimension finie, il existe une base orthonormée de $E$ constituée de vecteurs propres de $M$. Soient $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$ les valeurs propres de $M$, ordonnées par ordre décroissant.
Pour tout $\mathbf{x} \in S^{n-1}$, on peut écrire $\mathbf{x} = \sum_{j=1}^n c_j \mathbf{e}_j$, où $(\mathbf{e}_1, \dots, \mathbf{e}_n)$ est une base orthonormée de vecteurs propres de $M$ correspondant aux valeurs propres $\lambda_1, \dots, \lambda_n$.
Puisque $\|\mathbf{x}\|=1$, nous avons $\sum_{j=1}^n c_j^2 = 1$.
Alors :
$$ \langle \mathbf{x}, M\mathbf{x} \rangle = \left\langle \sum_{j=1}^n c_j \mathbf{e}_j, M \left( \sum_{l=1}^n c_l \mathbf{e}_l \right) \right\rangle = \left\langle \sum_{j=1}^n c_j \mathbf{e}_j, \sum_{l=1}^n c_l \lambda_l \mathbf{e}_l \right\rangle $$
En utilisant l'orthonormalité de la base de vecteurs propres :
$$ \langle \mathbf{x}, M\mathbf{x} \rangle = \sum_{j=1}^n c_j^2 \lambda_j $$
Puisque $\lambda_1$ est la plus grande valeur propre, nous avons $\lambda_j \le \lambda_1$ pour tout $j$.
$$ \sum_{j=1}^n c_j^2 \lambda_j \le \sum_{j=1}^n c_j^2 \lambda_1 = \lambda_1 \sum_{j=1}^n c_j^2 = \lambda_1 \cdot 1 = \lambda_1 $$
Ainsi, la valeur maximale de $f(\mathbf{x})$ est $\lambda_1$, la plus grande valeur propre de $M$.

Les vecteurs $\mathbf{x}$ qui atteignent ce maximum sont ceux pour lesquels l'inégalité $\sum_{j=1}^n c_j^2 \lambda_j \le \lambda_1$ devient une égalité. Cela se produit si et seulement si $c_j^2 \lambda_j = c_j^2 \lambda_1$ pour tous les $j$.
Si $\lambda_j < \lambda_1$, alors il faut que $c_j=0$. Cela signifie que $\mathbf{x}$ doit être une combinaison linéaire des vecteurs propres associés à la valeur propre $\lambda_1$.
L'ensemble des vecteurs $\mathbf{x}$ qui atteignent ce maximum est l'espace propre $E_{\lambda_1}$ associé à la plus grande valeur propre $\lambda_1$, intersecté avec la sphère unité $S^{n-1}$. Autrement dit, ce sont les vecteurs propres de $M$ associés à la plus grande valeur propre $\lambda_1$, normalisés à l'unité.

#### 5. Cas particulier dans $\mathbb{R}^2$
Dans $E = \mathbb{R}^2$ muni du produit scalaire canonique, la base canonique est $(\mathbf{e}_1, \mathbf{e}_2)$ où $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ et $\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$.
Les vecteurs normalisés sont donnés par :
$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$
$\mathbf{v}_2 = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$
$\mathbf{v}_3 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$

La matrice $M$ est donnée par $M = \sum_{i=1}^3 \mathbf{v}_i \mathbf{v}_i^T$.
Calculons chaque terme $\mathbf{v}_i \mathbf{v}_i^T$:
Pour $\mathbf{v}_1$:
$$ \mathbf{v}_1 \mathbf{v}_1^T = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} $$
Pour $\mathbf{v}_2$:
$$ \mathbf{v}_2 \mathbf{v}_2^T = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} \end{pmatrix} $$
Pour $\mathbf{v}_3$:
$$ \mathbf{v}_3 \mathbf{v}_3^T = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} $$
Maintenant, nous sommons ces matrices pour obtenir $M$:
$$ M = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 + \frac{1}{2} + 0 & 0 + \frac{1}{2} + 0 \\ 0 + \frac{1}{2} + 0 & 0 + \frac{1}{2} + 1 \end{pmatrix} = \begin{pmatrix} \frac{3}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} \end{pmatrix} $$
La matrice $M$ est $\begin{pmatrix} \frac{3}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} \end{pmatrix}$.

Pour trouver le vecteur $\mathbf{x}$ optimal, nous devons trouver la plus grande valeur propre de $M$ et son vecteur propre associé.
Le polynôme caractéristique de $M$ est $\det(M - \lambda I)$:
$$ \det \begin{pmatrix} \frac{3}{2} - \lambda & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} - \lambda \end{pmatrix} = \left( \frac{3}{2} - \lambda \right)^2 - \left( \frac{1}{2} \right)^2 $$
$$ = \left( \frac{3}{2} - \lambda - \frac{1}{2} \right) \left( \frac{3}{2} - \lambda + \frac{1}{2} \right) = (1 - \lambda)(2 - \lambda) $$
Les valeurs propres sont $\lambda_1 = 2$ et $\lambda_2 = 1$.
La plus grande valeur propre est $\lambda_1 = 2$.

Cherchons le vecteur propre associé à $\lambda_1 = 2$:
$$ (M - 2I) \mathbf{x} = \mathbf{0} $$
$$ \begin{pmatrix} \frac{3}{2} - 2 & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} - 2 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
$$ \begin{pmatrix} -\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
Cela conduit au système d'équations :
$$ -\frac{1}{2} x_1 + \frac{1}{2} x_2 = 0 \implies x_1 = x_2 $$
$$ \frac{1}{2} x_1 - \frac{1}{2} x_2 = 0 \implies x_1 = x_2 $$
Les vecteurs propres associés à $\lambda_1 = 2$ sont de la forme $\begin{pmatrix} c \\ c \end{pmatrix}$ pour $c \ne 0$.
Pour que le vecteur $\mathbf{x}$ soit de norme unité, nous devons avoir $\|\mathbf{x}\|=1$:
$$ \left\| \begin{pmatrix} c \\ c \end{pmatrix} \right\|^2 = c^2 + c^2 = 2c^2 = 1 \implies c^2 = \frac{1}{2} \implies c = \pm \frac{1}{\sqrt{2}} $$
Donc, les vecteurs optimaux sont $\mathbf{x} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$ et $\mathbf{x} = \begin{pmatrix} -\frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix}$.
Le vecteur $\mathbf{x}$ optimal (à un signe près) est $\begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$.

### Conclusion
Le problème de la maximisation de la somme des carrés des similarités cosinus d'un vecteur de norme unité $\mathbf{x}$ avec un ensemble de vecteurs sémantiques normalisés $\mathbf{v}_i$ se ramène à la maximisation d'une forme quadratique $f(\mathbf{x}) = \langle \mathbf{x}, M\mathbf{x} \rangle$ sur la sphère unité. L'opérateur $M = \sum_{i=1}^k \mathbf{v}_i \mathbf{v}_i^T$ est un opérateur linéaire symétrique et positif.

L'existence d'un maximum est garantie par la continuité de $f$ sur la sphère unité compacte. La valeur maximale de $f(\mathbf{x})$ est la plus grande valeur propre de $M$, et les vecteurs $\mathbf{x}$ qui atteignent ce maximum sont les vecteurs propres de $M$ associés à cette plus grande valeur propre, normalisés à l'unité.

Dans le cas particulier de $\mathbb{R}^2$ avec les vecteurs $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$, $\mathbf{v}_3 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, la matrice $M$ est $\begin{pmatrix} \frac{3}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{3}{2} \end{pmatrix}$.
La plus grande valeur propre de $M$ est $\lambda_1 = 2$.
Le vecteur optimal (à un signe près) est le vecteur propre normalisé associé à $\lambda_1=2$, qui est $\mathbf{x} = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}$. Ce vecteur représente la direction qui maximise la "représentativité sémantique" par rapport aux ancres données.
