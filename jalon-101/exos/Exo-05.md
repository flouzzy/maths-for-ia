# Exercice 05: Le Théorème d'Isomorphisme de Banach et les Projections

Cet exercice approfondit la compréhension du Théorème d'Isomorphisme de Banach en l'appliquant à l'étude des opérateurs de projection sur les espaces de Banach. Il démontre la continuité automatique d'une projection dont l'image et le noyau sont fermés, une conséquence fondamentale de la complétude des espaces sous-jacents. La rigueur et la précision seront de mise pour chaque étape de la démonstration.

Difficulté : $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $(X, \|\cdot\|)$ un espace de Banach.
Soit $P: X \to X$ une application linéaire telle que $P^2 = P$. Un tel opérateur est appelé un projecteur ou une projection.

**Partie 1: Propriétés élémentaires des projections**

1.  Démontrer que $X = \text{Ker}(P) \oplus \text{Im}(P)$, où $\text{Ker}(P) = \{x \in X : Px = 0\}$ est le noyau de $P$ et $\text{Im}(P) = \{Px : x \in X\}$ est l'image de $P$. C'est-à-dire, pour tout $x \in X$, il existe un unique $y \in \text{Ker}(P)$ et un unique $z \in \text{Im}(P)$ tels que $x = y + z$.
2.  Si $P$ est un opérateur linéaire continu (borné), démontrer que $\text{Ker}(P)$ et $\text{Im}(P)$ sont des sous-espaces vectoriels fermés de $X$.

**Partie 2: Le Théorème d'Isomorphisme de Banach et la continuité de la projection**

Dans cette partie, nous allons établir une propriété remarquable des projections sur les espaces de Banach. Nous supposerons que $\text{Ker}(P)$ et $\text{Im}(P)$ sont des sous-espaces vectoriels fermés de $X$. Soit $Y = \text{Im}(P)$ et $Z = \text{Ker}(P)$.

1.  Justifier que $Y$ et $Z$ sont des espaces de Banach munis de la norme induite par $X$.
2.  Considérer l'opérateur $T: Y \times Z \to X$ défini par $T(y, z) = y + z$ pour tout $(y,z) \in Y \times Z$. Démontrer que $T$ est un opérateur linéaire continu et bijectif. Pour l'espace produit $Y \times Z$, on utilisera la norme $\|(y,z)\|_{Y \times Z} = \|y\|_X + \|z\|_X$.
3.  En utilisant le Théorème d'Isomorphisme de Banach (aussi connu sous le nom de Théorème de l'Inverse Borné), déduire que $T$ est un isomorphisme d'espaces de Banach. C'est-à-dire que $T$ est linéaire, bijectif, et que $T$ et $T^{-1}$ sont continus.
4.  Conclure que l'opérateur de projection $P$ est continu.

---

## Correction Détaillée

Nous allons aborder chaque question avec la plus grande rigueur, en justifiant chaque assertion.

### Partie 1: Propriétés élémentaires des projections

**1. Démontrer que $X = \text{Ker}(P) \oplus \text{Im}(P)$.**

Pour montrer que $X = \text{Ker}(P) \oplus \text{Im}(P)$, nous devons établir deux points essentiels :
(a) $X = \text{Ker}(P) + \text{Im}(P)$, c'est-à-dire que tout élément de $X$ peut s'écrire comme la somme d'un élément du noyau et d'un élément de l'image.
(b) $\text{Ker}(P) \cap \text{Im}(P) = \{0\}$, c'est-à-dire que l'intersection du noyau et de l'image est réduite au vecteur nul.

Démonstration de (a) $X = \text{Ker}(P) + \text{Im}(P)$:
Soit $x \in X$ un vecteur arbitraire. Nous cherchons à décomposer $x$ en une somme de deux termes, l'un appartenant à $\text{Ker}(P)$ et l'autre à $\text{Im}(P)$.
Considérons l'identité $x = (x - Px) + Px$.
D'une part, posons $z = Px$. Par définition de l'image, $z \in \text{Im}(P)$.
D'autre part, posons $y = x - Px$. Pour vérifier que $y \in \text{Ker}(P)$, nous appliquons l'opérateur $P$ à $y$:
$P(y) = P(x - Px) = Px - P(Px)$ par linéarité de $P$.
Puisque $P$ est une projection, nous avons $P^2 = P$. Par conséquent, $P(Px) = Px$.
Substituant cela dans l'expression précédente, nous obtenons:
$P(y) = Px - Px = 0$.
Ainsi, $y \in \text{Ker}(P)$.
Nous avons donc démontré que pour tout $x \in X$, $x$ peut s'écrire comme $y + z$ avec $y \in \text{Ker}(P)$ et $z \in \text{Im}(P)$. Cela prouve que $X = \text{Ker}(P) + \text{Im}(P)$.

Démonstration de (b) $\text{Ker}(P) \cap \text{Im}(P) = \{0\}$:
Soit $v \in \text{Ker}(P) \cap \text{Im}(P)$.
Puisque $v \in \text{Ker}(P)$, par définition du noyau, nous avons $P(v) = 0$.
Puisque $v \in \text{Im}(P)$, par définition de l'image, il existe un certain $u \in X$ tel que $v = P(u)$.
En appliquant $P$ à cette dernière égalité, nous obtenons $P(v) = P(P(u)) = P^2(u)$.
Utilisant la propriété $P^2 = P$, nous avons $P^2(u) = P(u)$.
Donc, $P(v) = P(u)$.
Mais nous savions déjà que $P(v) = 0$. Par conséquent, $P(u) = 0$.
Puisque $v = P(u)$, cela implique $v = 0$.
Ainsi, le seul élément qui appartient à la fois au noyau et à l'image est le vecteur nul. Cela prouve que $\text{Ker}(P) \cap \text{Im}(P) = \{0\}$.

Ayant démontré (a) et (b), nous concluons que $X = \text{Ker}(P) \oplus \text{Im}(P)$. La décomposition est unique car si $x = y_1+z_1 = y_2+z_2$, alors $y_1-y_2 = z_2-z_1$. L'élément $y_1-y_2 \in \text{Ker}(P)$ et $z_2-z_1 \in \text{Im}(P)$. Leur égalité implique que cet élément appartient à l'intersection, donc il est nul. Ainsi $y_1=y_2$ et $z_1=z_2$.

**2. Si $P$ est un opérateur linéaire continu (borné), démontrer que $\text{Ker}(P)$ et $\text{Im}(P)$ sont des sous-espaces vectoriels fermés de $X$.**

Un opérateur linéaire continu est également appelé borné. Cela signifie qu'il existe une constante $M \ge 0$ telle que $\|Px\| \le M\|x\|$ pour tout $x \in X$.

Démonstration que $\text{Ker}(P)$ est fermé:
Le noyau $\text{Ker}(P)$ est l'ensemble des vecteurs $x \in X$ tels que $P(x) = 0$.
Formellement, $\text{Ker}(P) = P^{-1}(\{0\})$.
L'ensemble $\{0\}$ est un sous-ensemble fermé de $X$ (car $X$ est un espace métrique et $\{0\}$ est l'ensemble des points $x$ tels que $\|x\|=0$, et la fonction $x \mapsto \|x\|$ est continue).
Puisque $P$ est un opérateur continu, la préimage d'un ensemble fermé par une application continue est un ensemble fermé.
Par conséquent, $\text{Ker}(P)$ est un sous-espace vectoriel fermé de $X$.

Démonstration que $\text{Im}(P)$ est fermé:
L'image $\text{Im}(P)$ est l'ensemble des vecteurs $x \in X$ tels que $P(x) = x$.
Pour le démontrer, soit $x \in \text{Im}(P)$. Alors il existe $u \in X$ tel que $x = P(u)$.
Appliquons $P$ à $x$: $P(x) = P(P(u)) = P^2(u)$.
Puisque $P^2 = P$, nous avons $P(x) = P(u) = x$.
Donc, tout élément de $\text{Im}(P)$ est un point fixe de $P$.
Réciproquement, si $P(x) = x$, alors $x$ est l'image de $x$ par $P$, donc $x \in \text{Im}(P)$.
Par conséquent, $\text{Im}(P) = \{x \in X : Px = x\}$.
Nous pouvons réécrire cette condition comme $(P - I)x = 0$, où $I$ est l'opérateur identité sur $X$.
Donc, $\text{Im}(P) = \text{Ker}(P - I)$.
L'opérateur identité $I: X \to X$ est linéaire et continu (sa norme est 1).
La différence de deux opérateurs linéaires continus, $P - I$, est un opérateur linéaire continu.
Comme précédemment, le noyau d'un opérateur linéaire continu est fermé.
Par conséquent, $\text{Im}(P) = \text{Ker}(P - I)$ est un sous-espace vectoriel fermé de $X$.

### Partie 2: Le Théorème d'Isomorphisme de Banach et la continuité de la projection

Nous supposons dans cette partie que $\text{Ker}(P)$ et $\text{Im}(P)$ sont des sous-espaces vectoriels fermés de $X$. Soit $Y = \text{Im}(P)$ et $Z = \text{Ker}(P)$.

**1. Justifier que $Y$ et $Z$ sont des espaces de Banach munis de la norme induite par $X$.**

Un espace de Banach est un espace vectoriel normé qui est complet pour la métrique induite par sa norme.
Nous savons que $X$ est un espace de Banach, ce qui signifie que $X$ est complet.
$Y$ est un sous-espace vectoriel fermé de $X$. Un théorème fondamental de l'analyse fonctionnelle stipule que tout sous-espace vectoriel fermé d'un espace de Banach est lui-même un espace de Banach par rapport à la norme induite. La complétude de $Y$ découle directement du fait qu'il est fermé dans un espace complet. Si une suite de Cauchy dans $Y$ converge vers un point dans $X$, ce point doit également être dans $Y$ puisque $Y$ est fermé.
De même, $Z$ est un sous-espace vectoriel fermé de $X$. Par le même raisonnement, $Z$ est également un espace de Banach.

**2. Considérer l'opérateur $T: Y \times Z \to X$ défini par $T(y, z) = y + z$ pour tout $(y,z) \in Y \times Z$. Démontrer que $T$ est un opérateur linéaire continu et bijectif. Pour l'espace produit $Y \times Z$, on utilisera la norme $\|(y,z)\|_{Y \times Z} = \|y\|_X + \|z\|_X$.**

Démonstration de la linéarité de $T$:
Soient $(y_1, z_1), (y_2, z_2) \in Y \times Z$ et $\alpha \in \mathbb{R}$ (ou $\mathbb{C}$).
$T((y_1, z_1) + (y_2, z_2)) = T(y_1+y_2, z_1+z_2) = (y_1+y_2) + (z_1+z_2)$
Par associativité et commutativité de l'addition vectorielle dans $X$:
$(y_1+y_2) + (z_1+z_2) = (y_1+z_1) + (y_2+z_2) = T(y_1, z_1) + T(y_2, z_2)$.
$T(\alpha(y_1, z_1)) = T(\alpha y_1, \alpha z_1) = \alpha y_1 + \alpha z_1$
Par distributivité de la multiplication scalaire dans $X$:
$\alpha y_1 + \alpha z_1 = \alpha(y_1 + z_1) = \alpha T(y_1, z_1)$.
Ainsi, $T$ est linéaire.

Démonstration de la continuité de $T$:
Pour prouver la continuité de $T$, il suffit de montrer qu'il est borné, c'est-à-dire qu'il existe une constante $M \ge 0$ telle que $\|T(y,z)\|_X \le M\|(y,z)\|_{Y \times Z}$ pour tout $(y,z) \in Y \times Z$.
$\|T(y,z)\|_X = \|y + z\|_X$.
Par l'inégalité triangulaire pour la norme $\|\cdot\|_X$:
$\|y + z\|_X \le \|y\|_X + \|z\|_X$.
Par définition de la norme sur l'espace produit $Y \times Z$:
$\|(y,z)\|_{Y \times Z} = \|y\|_X + \|z\|_X$.
En combinant ces deux expressions, nous obtenons:
$\|T(y,z)\|_X \le \|(y,z)\|_{Y \times Z}$.
On peut choisir $M=1$. Cela démontre que $T$ est un opérateur borné, et par conséquent continu.

Démonstration de la bijectivité de $T$:
La bijectivité se décompose en injectivité et surjectivité.

Injectivité de $T$:
Nous devons montrer que si $T(y,z) = 0$, alors $(y,z) = (0,0)$.
Si $T(y,z) = 0$, alors $y + z = 0$.
Cela implique $y = -z$.
Puisque $y \in Y = \text{Im}(P)$ et $z \in Z = \text{Ker}(P)$, nous avons $y \in \text{Im}(P)$ et $y = -z \in \text{Ker}(P)$.
Ainsi, $y$ est un élément de l'intersection $\text{Im}(P) \cap \text{Ker}(P)$.
D'après la Partie 1, question 1(b), nous avons démontré que $\text{Im}(P) \cap \text{Ker}(P) = \{0\}$.
Par conséquent, $y = 0$.
Puisque $y = -z$, il s'ensuit que $z = 0$.
Donc, $(y,z) = (0,0)$. Cela prouve que $T$ est injectif.

Surjectivité de $T$:
Nous devons montrer que pour tout $x \in X$, il existe $(y,z) \in Y \times Z$ tel que $T(y,z) = x$.
D'après la Partie 1, question 1(a), nous avons démontré que $X = \text{Ker}(P) + \text{Im}(P)$.
Cela signifie que pour tout $x \in X$, il existe un $y \in \text{Im}(P)$ et un $z \in \text{Ker}(P)$ tels que $x = y + z$.
Par définition de $T$, $T(y,z) = y+z = x$.
Ainsi, pour tout $x \in X$, nous pouvons trouver un couple $(y,z) \in Y \times Z$ qui lui est associé par $T$. Cela prouve que $T$ est surjectif.

En conclusion, $T$ est un opérateur linéaire continu et bijectif.

**3. En utilisant le Théorème d'Isomorphisme de Banach, déduire que $T$ est un isomorphisme d'espaces de Banach.**

Le Théorème d'Isomorphisme de Banach (également connu sous le nom de Théorème de l'Inverse Borné) stipule que si $T: E \to F$ est un opérateur linéaire continu et bijectif entre deux espaces de Banach $E$ et $F$, alors son inverse $T^{-1}: F \to E$ est également un opérateur linéaire continu.
Dans notre cas, $E = Y \times Z$ et $F = X$.
1.  Nous avons établi dans la question 2.1 que $Y$ et $Z$ sont des espaces de Banach. L'espace produit $Y \times Z$ muni de la norme $\|(y,z)\|_{Y \times Z} = \|y\|_X + \|z\|_X$ est également un espace de Banach. En effet, si $((y_n, z_n))$ est une suite de Cauchy dans $Y \times Z$, alors $(y_n)$ est une suite de Cauchy dans $Y$ et $(z_n)$ est une suite de Cauchy dans $Z$. Comme $Y$ et $Z$ sont complets, $y_n \to y \in Y$ et $z_n \to z \in Z$. Donc $(y_n, z_n) \to (y,z)$ dans $Y \times Z$.
2.  Nous avons établi dans la question 2.2 que $X$ est un espace de Banach (donné par l'énoncé).
3.  Nous avons établi dans la question 2.2 que $T: Y \times Z \to X$ est un opérateur linéaire continu et bijectif.

Toutes les conditions du Théorème d'Isomorphisme de Banach sont remplies.
Par conséquent, le théorème garantit que l'inverse $T^{-1}: X \to Y \times Z$ est également un opérateur linéaire continu.
Un opérateur linéaire qui est bijectif et dont l'inverse est également continu est appelé un isomorphisme d'espaces de Banach (ou un homéomorphisme linéaire).

**4. Conclure que l'opérateur de projection $P$ est continu.**

Rappelons que $P: X \to X$ est la projection telle que $P^2=P$. Pour tout $x \in X$, nous avons la décomposition unique $x = y + z$ où $y \in Y = \text{Im}(P)$ et $z \in Z = \text{Ker}(P)$.
Par la définition de $P$:
Si $x = y+z$ avec $y \in \text{Im}(P)$ et $z \in \text{Ker}(P)$, alors $P(x) = P(y+z) = P(y) + P(z)$.
Puisque $y \in \text{Im}(P)$, nous avons $P(y) = y$ (démontré en 1.2).
Puisque $z \in \text{Ker}(P)$, nous avons $P(z) = 0$.
Donc, $P(x) = y + 0 = y$.

Nous avons l'opérateur $T: Y \times Z \to X$ tel que $T(y,z) = y+z$.
Son inverse $T^{-1}: X \to Y \times Z$ est donné par $T^{-1}(x) = T^{-1}(y+z) = (y,z)$.
Considérons l'opérateur de projection sur la première composante $\pi_Y: Y \times Z \to Y$ défini par $\pi_Y(y,z) = y$.
Cet opérateur est linéaire. De plus, il est continu:
$\|\pi_Y(y,z)\|_X = \|y\|_X$.
Puisque $\|(y,z)\|_{Y \times Z} = \|y\|_X + \|z\|_X \ge \|y\|_X$, nous avons $\|\pi_Y(y,z)\|_X \le \|(y,z)\|_{Y \times Z}$.
Ainsi, $\pi_Y$ est borné et donc continu.

Maintenant, nous pouvons exprimer $P$ comme une composition d'opérateurs continus:
Pour tout $x \in X$, $P(x) = y$.
Nous avons $T^{-1}(x) = (y,z)$.
Donc, $P(x) = \pi_Y(y,z) = \pi_Y(T^{-1}(x))$.
Nous pouvons écrire $P = \pi_Y \circ T^{-1}$.
Nous avons démontré que $T^{-1}: X \to Y \times Z$ est un opérateur linéaire continu (par le Théorème d'Isomorphisme de Banach).
Nous avons démontré que $\pi_Y: Y \times Z \to Y$ est un opérateur linéaire continu.
La composition de deux opérateurs linéaires continus est un opérateur linéaire continu.
Par conséquent, $P: X \to Y$ est un opérateur linéaire continu.
Puisque $Y$ est un sous-espace de $X$ et que la norme est la même, l'opérateur $P: X \to X$ est continu.

Ceci conclut la démonstration. Nous avons montré que sur un espace de Banach, une projection dont le noyau et l'image sont fermés est nécessairement continue. Ceci est un résultat fondamental illustrant la puissance du Théorème d'Isomorphisme de Banach.