# Exercice 2 : Inversion de l'ordre d'intégration sur un triangle $\bigstar\bigstar\star\star\star$

## Énoncé

Considérons l'intégrale itérée suivante :
$$ I = \int_0^1 \left( \int_0^x e^{x^2} \, dy \right) dx $$
1. Esquisser le domaine d'intégration $D$.
2. Inverser l'ordre d'intégration et calculer la valeur de $I$.

## Correction

1. **Le domaine d'intégration :**
D'après les bornes, $x$ varie de $0$ à $1$. Pour un $x$ fixé, $y$ varie de $0$ à $x$.
Ainsi, le domaine $D$ est défini par : $D = \{ (x, y) \in \mathbb{R}^2 \mid 0 \le x \le 1, \, 0 \le y \le x \}$.
C'est le triangle de sommets $(0,0)$, $(1,0)$ et $(1,1)$.
La fonction $f(x,y) = e^{x^2}$ est positive et continue sur $D$, donc Tonelli s'applique.

2. **Inversion de l'ordre :**
Pour intégrer d'abord par rapport à $x$, on doit fixer $y$. En regardant le triangle, $y$ varie globalement de $0$ à $1$.
Pour un $y$ fixé dans $[0, 1]$, la variable $x$ va de la droite $x = y$ jusqu'à la droite verticale $x = 1$.
Donc, le domaine s'écrit aussi : $D = \{ (x, y) \in \mathbb{R}^2 \mid 0 \le y \le 1, \, y \le x \le 1 \}$.
L'intégrale devient :
$$ I = \int_0^1 \left( \int_y^1 e^{x^2} \, dx \right) dy $$
L'intégrale intérieure $\int_y^1 e^{x^2} dx$ n'a pas de primitive usuelle. Cependant, le premier ordre d'intégration (celui de l'énoncé) était calculable facilement :
$$ I = \int_0^1 \left[ y e^{x^2} \right]_{y=0}^{y=x} dx = \int_0^1 x e^{x^2} dx $$
Posons $u = x^2$, $du = 2x dx$. Alors $x dx = \frac{1}{2} du$. Les bornes restent 0 et 1.
$$ I = \int_0^1 \frac{1}{2} e^u du = \frac{1}{2} \left[ e^u \right]_0^1 = \frac{1}{2} (e - 1) $$
Remarque : L'énoncé demande "Inverser l'ordre d'intégration et calculer la valeur". Parfois, inverser rend le calcul impossible, ici l'ordre initial était le bon. Si l'énoncé de départ était dans le mauvais sens, Fubini nous sauve.
