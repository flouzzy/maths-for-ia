# Exercice 1 : $\bigstar\star\star\star\star$

## Énoncé

Soit $E = \mathbb{R}^2$ muni de sa structure d'espace vectoriel usuelle.
Considérons les ensembles :
$A = \{ (x,y) \in \mathbb{R}^2 \mid x \le 0 \}$
$B = \{ (x,y) \in \mathbb{R}^2 \mid (x-3)^2 + y^2 < 1 \}$

Démontrer rigoureusement que $A$ et $B$ peuvent être séparés strictement par un hyperplan affine fermé. Préciser explicitement l'équation d'un tel hyperplan ainsi que la forme linéaire $f$ et la constante $\alpha$ associées.

## Correction

**Étape 1 : Vérification des hypothèses du théorème de séparation stricte**
L'espace $E = \mathbb{R}^2$ est de dimension finie, et muni de la norme euclidienne usuelle, il est normé.
- $A$ est un demi-plan, c'est un ensemble **convexe**. L'inégalité $x \le 0$ est large, donc $A$ est **fermé**.
- $B$ est un disque ouvert de centre $(3,0)$ et de rayon $1$. Il est clairement **convexe**. Cependant, il n'est pas compact (puisqu'il n'est pas fermé).

Le théorème de Hahn-Banach (2ème forme, stricte) exige que l'un soit fermé et l'autre compact. Ici $B$ n'est pas compact. Nous pouvons néanmoins utiliser la fermeture de $B$.
Soit $\overline{B} = \{ (x,y) \in \mathbb{R}^2 \mid (x-3)^2 + y^2 \le 1 \}$ le disque fermé.
$\overline{B}$ est fermé et borné dans $\mathbb{R}^2$ (dimension finie), donc par le théorème de Borel-Lebesgue, $\overline{B}$ est **compact**.
De plus, la distance entre $A$ (demi-plan $x \le 0$) et $\overline{B}$ (qui commence à $x=2$) est $2 > 0$. Donc $A \cap \overline{B} = \emptyset$.
Les ensembles $A$ et $\overline{B}$ sont convexes, disjoints, $A$ est fermé et $\overline{B}$ est compact. Les hypothèses de la deuxième forme géométrique de Hahn-Banach sont donc strictement vérifiées pour $A$ et $\overline{B}$.
Ainsi, ils peuvent être séparés strictement, ce qui implique que $A$ et $B \subset \overline{B}$ le sont également.

**Étape 2 : Construction de l'hyperplan**
Intuitivement, l'axe $x = 1$ sépare largement les deux ensembles avec une marge.
Posons la forme linéaire $f(x,y) = x$. $f$ est une projection, donc continue sur $\mathbb{R}^2$.
Pour $a = (x_a, y_a) \in A$, on a par définition $x_a \le 0$, donc $f(a) \le 0$.
Pour $b = (x_b, y_b) \in B$, par définition $(x_b - 3)^2 + y_b^2 < 1$.
Puisque $(x_b - 3)^2 \le (x_b - 3)^2 + y_b^2 < 1$, on a $-1 < x_b - 3 < 1 \implies 2 < x_b < 4$.
Donc $f(b) = x_b > 2$.

Choisissons la constante $\alpha = 1$.
Nous avons, pour tout $a \in A$, $f(a) \le 0 < 1 = \alpha$.
Et pour tout $b \in B$, $f(b) > 2 > 1 = \alpha$.
Prenons $\epsilon = 1/2$.
On a $\forall a \in A, \ f(a) \le 0 \le 1 - 1/2 = \alpha - \epsilon$.
On a $\forall b \in B, \ f(b) > 2 \ge 1 + 1/2 = \alpha + \epsilon$.
L'hyperplan affine d'équation $f(x,y) = 1$, soit $x = 1$, sépare donc $A$ et $B$ au sens strict. La démonstration est complète. $\blacksquare$
