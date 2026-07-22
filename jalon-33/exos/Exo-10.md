# Exercice 10 : Optimisation quadratique sous contrainte

## Énoncé
Soit $A \in \mathcal{S}_n(\mathbb{R})$ une matrice symétrique réelle de valeurs propres $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$.
On considère la forme quadratique $q(x) = x^T A x$.
Démontrer rigoureusement (Théorème de Rayleigh-Ritz) que :
$$ \max_{\|x\|=1} q(x) = \lambda_n $$
Où $\|x\|$ est la norme euclidienne standard induite par le produit scalaire standard sur $\mathbb{R}^n$.

## Correction Détaillée (Zéro Ellipse)

Le théorème spectral nous assure que toute matrice symétrique réelle est diagonalisable dans une base orthonormale.
Il existe donc une matrice orthogonale $P \in O(n)$ (telle que $P^{-1} = P^T$) et une matrice diagonale $D = \text{diag}(\lambda_1, \dots, \lambda_n)$ telles que :
$$ A = P D P^T $$
Remplaçons $A$ dans l'expression de la forme quadratique :
$$ q(x) = x^T (P D P^T) x = (x^T P) D (P^T x) $$
Posons le changement de variable $y = P^T x$. Comme $P^T$ est la transposée d'une matrice orthogonale, c'est aussi une matrice orthogonale.
Puisque $(P^T x)^T = x^T (P^T)^T = x^T P$, nous obtenons l'expression découplée :
$$ q(x) = y^T D y $$
En développant le produit vectoriel, puisque $D$ est diagonale, on obtient une somme simple :
$$ q(x) = \sum_{i=1}^n \lambda_i y_i^2 $$
Étudions la contrainte $\|x\| = 1$. L'invariance de la norme euclidienne sous transformation orthogonale donne :
$$ \|y\|^2 = \|P^T x\|^2 = (P^T x)^T (P^T x) = x^T P P^T x = x^T I_n x = x^T x = \|x\|^2 $$
Donc la condition $\|x\| = 1$ est strictement équivalente à $\|y\| = 1$, soit $\sum_{i=1}^n y_i^2 = 1$.
Le problème revient donc à maximiser $\sum_{i=1}^n \lambda_i y_i^2$ sous la contrainte $\sum_{i=1}^n y_i^2 = 1$.

**Majoration :**
Puisque $\lambda_1 \le \dots \le \lambda_n$, pour tout $i \in \{1, \dots, n\}$, on a $\lambda_i \le \lambda_n$.
Comme $y_i^2 \ge 0$, on peut multiplier l'inégalité sans en changer le sens :
$$ \lambda_i y_i^2 \le \lambda_n y_i^2 $$
En sommant ces inégalités pour $i$ allant de 1 à $n$ :
$$ \sum_{i=1}^n \lambda_i y_i^2 \le \sum_{i=1}^n \lambda_n y_i^2 = \lambda_n \sum_{i=1}^n y_i^2 $$
En appliquant la contrainte $\sum_{i=1}^n y_i^2 = 1$ :
$$ q(x) \le \lambda_n \cdot 1 = \lambda_n $$
Nous avons prouvé que pour tout $x$ sur la sphère unité, $q(x) \le \lambda_n$.

**Atteinte du maximum :**
Il faut montrer que cette borne supérieure est bien un maximum (elle est atteinte).
Considérons le vecteur $x_0 = P e_n$, où $e_n = (0, \dots, 0, 1)^T$ est le dernier vecteur de la base canonique.
Vérifions sa norme : $\|x_0\|^2 = (P e_n)^T (P e_n) = e_n^T P^T P e_n = e_n^T I_n e_n = 1$. Donc $x_0$ satisfait la contrainte.
Calculons le vecteur dans la base propre : $y_0 = P^T x_0 = P^T P e_n = e_n$.
Ainsi, $y_0$ a pour coordonnées $y_{0,1} = 0, \dots, y_{0,n} = 1$.
Évaluons $q(x_0)$ avec l'expression diagonale :
$$ q(x_0) = \sum_{i=1}^n \lambda_i y_{0,i}^2 = \lambda_1 \cdot 0^2 + \dots + \lambda_{n-1} \cdot 0^2 + \lambda_n \cdot 1^2 = \lambda_n $$
La borne est atteinte au vecteur propre unitaire associé à la plus grande valeur propre $\lambda_n$.
On a donc bien prouvé formellement que $\max_{\|x\|=1} q(x) = \lambda_n$. $\blacksquare$
