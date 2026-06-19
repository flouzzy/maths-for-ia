Cher étudiante, cher étudiant,

Nous poursuivons notre exploration des structures fondamentales de l'algèbre linéaire avec ce quatrième exercice, qui nous permettra de consolider notre compréhension des sous-espaces vectoriels engendrés, des familles libres et des bases en dimension finie. Je vous invite à aborder cet exercice avec la rigueur et la précision qui s'imposent.

---

# Exercice 4 : Caractérisation d'un sous-espace polynomial

## Énoncé

Soit $\mathbb{R}$ le corps des nombres réels.
Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes à coefficients réels de degré inférieur ou égal à 2.
Considérons la famille de polynômes $\mathcal{F} = (P_1, P_2, P_3)$ définie par :
$P_1(X) = 1 + X$
$P_2(X) = X + X^2$
$P_3(X) = 1 - X^2$

1.  Soit $F$ le sous-espace vectoriel de $E$ engendré par la famille $\mathcal{F}$, c'est-à-dire $F = \text{Vect}(P_1, P_2, P_3)$. Déterminer une base de $F$.
2.  Quelle est la dimension de $F$?
3.  Le polynôme $Q(X) = 3 + 2X - X^2$ appartient-il à $F$? Justifier votre réponse.

## Correction Détaillée

**1. Détermination d'une base de $F$**

Soit $\mathbb{R}$ le corps des nombres réels.
Soit $E = \mathbb{R}_2[X]$ l'espace vectoriel des polynômes à coefficients réels de degré inférieur ou égal à 2.
La famille $\mathcal{F} = (P_1, P_2, P_3)$ est une famille de vecteurs de $E$.
Le sous-espace vectoriel $F$ est défini comme $F = \text{Vect}(P_1, P_2, P_3)$.
Pour déterminer une base de $F$, nous devons extraire de $\mathcal{F}$ une sous-famille qui soit à la fois libre et génératrice de $F$. Nous commençons par tester la liberté de la famille $\mathcal{F}$.

Considérons une combinaison linéaire nulle des polynômes $P_1, P_2, P_3$. Soient $\alpha, \beta, \gamma \in \mathbb{R}$ des scalaires tels que :
$\alpha P_1(X) + \beta P_2(X) + \gamma P_3(X) = 0_{\mathbb{R}_2[X]}$

Substituons les expressions des polynômes :
$\alpha(1 + X) + \beta(X + X^2) + \gamma(1 - X^2) = 0 + 0X + 0X^2$

Développons et regroupons les termes selon les puissances de $X$ :
$\alpha + \alpha X + \beta X + \beta X^2 + \gamma - \gamma X^2 = 0 + 0X + 0X^2$
$(\alpha + \gamma) \cdot 1 + (\alpha + \beta) \cdot X + (\beta - \gamma) \cdot X^2 = 0 + 0X + 0X^2$

Par identification des coefficients des polynômes, nous obtenons le système d'équations linéaires suivant :
(1) $\alpha + \gamma = 0$ (coefficient constant)
(2) $\alpha + \beta = 0$ (coefficient de $X$)
(3) $\beta - \gamma = 0$ (coefficient de $X^2$)

Résolvons ce système :
De l'équation (1), nous tirons $\gamma = -\alpha$.
De l'équation (2), nous tirons $\beta = -\alpha$.

Substituons ces expressions de $\beta$ et $\gamma$ dans l'équation (3) :
$(-\alpha) - (-\alpha) = 0$
$-\alpha + \alpha = 0$
$0 = 0$

Cette dernière équation est toujours vraie, ce qui signifie que le système admet des solutions non triviales. Par exemple, si nous choisissons $\alpha = 1$, alors $\beta = -1$ et $\gamma = -1$.
Ainsi, nous avons trouvé une combinaison linéaire non triviale qui donne le polynôme nul :
$1 \cdot P_1(X) - 1 \cdot P_2(X) - 1 \cdot P_3(X) = 0_{\mathbb{R}_2[X]}$

Ceci démontre que la famille $\mathcal{F}$ est liée.
Nous pouvons exprimer un des polynômes en fonction des autres. Par exemple, isolons $P_1(X)$ :
$P_1(X) = P_2(X) + P_3(X)$

Puisque $P_1$ est une combinaison linéaire de $P_2$ et $P_3$, il peut être retiré de la famille génératrice sans modifier l'espace engendré.
Donc, $F = \text{Vect}(P_1, P_2, P_3) = \text{Vect}(P_2, P_3)$.

Maintenant, nous devons vérifier si la famille réduite $\mathcal{F}' = (P_2, P_3)$ est libre.
Considérons une combinaison linéaire nulle de $P_2$ et $P_3$. Soient $a, b \in \mathbb{R}$ des scalaires tels que :
$a P_2(X) + b P_3(X) = 0_{\mathbb{R}_2[X]}$

Substituons les expressions des polynômes :
$a(X + X^2) + b(1 - X^2) = 0 + 0X + 0X^2$

Développons et regroupons les termes :
$aX + aX^2 + b - bX^2 = 0 + 0X + 0X^2$
$b \cdot 1 + a \cdot X + (a - b) \cdot X^2 = 0 + 0X + 0X^2$

Par identification des coefficients :
(4) $b = 0$ (coefficient constant)
(5) $a = 0$ (coefficient de $X$)
(6) $a - b = 0$ (coefficient de $X^2$)

En substituant $a=0$ et $b=0$ dans l'équation (6) :
$0 - 0 = 0$
$0 = 0$
Le système n'admet que la solution triviale $a=0$ et $b=0$.
Par conséquent, la famille $\mathcal{F}' = (P_2, P_3)$ est une famille libre.

Puisque $\mathcal{F}' = (P_2, P_3)$ est une famille libre et qu'elle engendre $F$, elle constitue une base de $F$.
Une base de $F$ est donc $(P_2(X), P_3(X)) = (X + X^2, 1 - X^2)$.

**2. Dimension de $F$**

La dimension d'un espace vectoriel est le nombre de vecteurs dans n'importe quelle de ses bases.
Nous avons trouvé que $(P_2, P_3)$ est une base de $F$. Cette base contient 2 vecteurs.
Par conséquent, la dimension de $F$ est $\text{dim}(F) = 2$.

**3. Appartenance du polynôme $Q(X)$ à $F$**

Le polynôme $Q(X) = 3 + 2X - X^2$ appartient à $F$ si et seulement s'il peut être exprimé comme une combinaison linéaire des vecteurs de la base de $F$, c'est-à-dire $P_2$ et $P_3$.
Nous cherchons donc des scalaires $a, b \in \mathbb{R}$ tels que :
$Q(X) = a P_2(X) + b P_3(X)$

Substituons les expressions des polynômes :
$3 + 2X - X^2 = a(X + X^2) + b(1 - X^2)$

Développons et regroupons les termes :
$3 + 2X - X^2 = aX + aX^2 + b - bX^2$
$3 + 2X - X^2 = b \cdot 1 + a \cdot X + (a - b) \cdot X^2$

Par identification des coefficients des polynômes :
(7) $b = 3$ (coefficient constant)
(8) $a = 2$ (coefficient de $X$)
(9) $a - b = -1$ (coefficient de $X^2$)

Nous avons directement les valeurs de $a$ et $b$ à partir des équations (7) et (8) : $a=2$ et $b=3$.
Vérifions si ces valeurs sont cohérentes avec l'équation (9) :
$a - b = 2 - 3 = -1$
L'équation (9) est $-1 = -1$, ce qui est vrai.
Le système est donc compatible et admet une solution unique.

Nous avons trouvé que $Q(X) = 2 P_2(X) + 3 P_3(X)$.
Puisque $Q(X)$ peut être écrit comme une combinaison linéaire des vecteurs de la base de $F$, nous pouvons conclure que $Q(X)$ appartient à $F$.
