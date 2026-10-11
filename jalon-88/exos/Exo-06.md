# Densités conjointes et factorisation

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

On considère un vecteur aléatoire continu $(X,Y)$ de densité conjointe donnée par :
$f(x,y) = k \cdot x y^2 e^{-x} e^{-2y}$ pour $x > 0, y > 0$, et $0$ sinon.
1. Trouver la constante $k$ pour que $f$ soit une véritable densité de probabilité.
2. Montrer que $X$ et $Y$ sont des variables aléatoires indépendantes et identifier leurs lois marginales.

### Correction

Soit la densité $f(x,y) = k \cdot x e^{-x} \cdot y^2 e^{-2y} \cdot \mathbb{1}_{\{x>0, y>0\}}$.

**1. Calcul de la constante $k$**
Pour que $f$ soit une densité, son intégrale sur $\mathbb{R}^2$ doit être égale à 1.
$1 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) dx dy$
$1 = \int_{0}^{\infty} \int_{0}^{\infty} k \cdot x e^{-x} \cdot y^2 e^{-2y} dx dy$
Par le théorème de Fubini-Tonelli, l'intégrale d'une fonction produit sur un domaine produit rectangulaire (ici $\mathbb{R}_+ \times \mathbb{R}_+$) se factorise :
$1 = k \left( \int_{0}^{\infty} x e^{-x} dx \right) \left( \int_{0}^{\infty} y^2 e^{-2y} dy \right)$
Calculons les intégrales unidimensionnelles. On reconnait la fonction Gamma : $\Gamma(n) = \int_0^\infty t^{n-1} e^{-t} dt = (n-1)!$.
- $\int_{0}^{\infty} x e^{-x} dx = \Gamma(2) = 1! = 1$.
- Pour la seconde intégrale, effectuons le changement de variable $u = 2y \implies dy = du/2$.
  $\int_{0}^{\infty} y^2 e^{-2y} dy = \int_{0}^{\infty} (u/2)^2 e^{-u} (du/2) = \frac{1}{8} \int_{0}^{\infty} u^2 e^{-u} du = \frac{1}{8} \Gamma(3) = \frac{2!}{8} = \frac{2}{8} = \frac{1}{4}$.
L'équation devient donc :
$1 = k \times 1 \times \frac{1}{4} \implies k = 4$.
La densité conjointe est $f(x,y) = 4 x y^2 e^{-x} e^{-2y} \mathbb{1}_{\{x>0, y>0\}}$.

**2. Indépendance et lois marginales**
D'après le théorème de factorisation des densités (Jalon 88), deux variables à densité sont indépendantes si et seulement si leur densité jointe peut s'écrire sous la forme du produit de deux densités unidimensionnelles (ou le produit d'une fonction de $x$ et d'une fonction de $y$).
Ici, on peut écrire $f(x,y) = (x e^{-x} \mathbb{1}_{\{x>0\}}) \times (4 y^2 e^{-2y} \mathbb{1}_{\{y>0\}})$.
Cette factorisation stricte en produit de fonctions mesurables positives $g(x)h(y)$ démontre immédiatement l'indépendance de $X$ et $Y$.
De plus, ce produit nous donne, à une constante de normalisation près, l'expression des densités marginales :
- $f_X(x) = C_1 x e^{-x} \mathbb{1}_{\{x>0\}}$. On reconnaît la densité d'une loi Gamma $\Gamma(k=2, \theta=1)$.
- $f_Y(y) = C_2 y^2 e^{-2y} \mathbb{1}_{\{y>0\}}$. On reconnaît la densité d'une loi Gamma $\Gamma(k=3, \theta=1/2)$.
L'exercice illustre de façon canonique comment lire l'indépendance directement sur la formule algébrique de la densité conjointe.
