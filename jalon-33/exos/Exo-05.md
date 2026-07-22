# Exercice 5 : Inégalité de Cauchy-Schwarz pour les FQ

## Énoncé
Soit $q$ une forme quadratique positive (c'est-à-dire $\forall x, q(x) \ge 0$) sur un $\mathbb{R}$-espace vectoriel $E$, et $b$ sa forme polaire.
Démontrer l'inégalité de Cauchy-Schwarz généralisée :
$$ \forall (x,y) \in E^2, \quad (b(x,y))^2 \le q(x)q(y) $$
Puis démontrer que $N(q) = \{x \in E \mid q(x) = 0\} = \ker(b) = \{x \in E \mid \forall y \in E, b(x,y)=0\}$.

## Correction Détaillée (Zéro Ellipse)

**1. Preuve de l'inégalité de Cauchy-Schwarz**
Fixons $x, y \in E$.
Pour tout scalaire $t \in \mathbb{R}$, considérons le vecteur $x + ty \in E$.
Puisque $q$ est positive, on a :
$$ q(x + ty) \ge 0 $$
Développons par bilinéarité de $b$ :
$$ q(x + ty) = b(x+ty, x+ty) = b(x,x) + tb(x,y) + tb(y,x) + t^2b(y,y) $$
Puisque $b$ est symétrique ($b(x,y) = b(y,x)$) et que $b(z,z) = q(z)$ :
$$ q(x+ty) = q(x) + 2tb(x,y) + t^2q(y) \ge 0 $$
Cette expression est un trinôme du second degré en la variable réelle $t$ : $P(t) = q(y)t^2 + 2b(x,y)t + q(x)$.
Puisque $P(t) \ge 0$ pour tout $t \in \mathbb{R}$, ce trinôme garde un signe constant (positif) et ne peut pas avoir deux racines réelles distinctes.
Son discriminant (réduit) doit donc être inférieur ou égal à zéro :
$$ \Delta' = (b(x,y))^2 - q(y)q(x) \le 0 $$
Ce qui donne exactement l'inégalité recherchée :
$$ (b(x,y))^2 \le q(x)q(y) $$

**2. Étude de $N(q)$**
Il est trivial que $\ker(b) \subset N(q)$. En effet, si $x \in \ker(b)$, alors pour tout $y \in E, b(x,y) = 0$. En particulier pour $y = x$, $b(x,x) = q(x) = 0$, donc $x \in N(q)$.
Démontrons l'inclusion inverse $N(q) \subset \ker(b)$.
Soit $x \in N(q)$. Donc $q(x) = 0$.
Appliquons l'inégalité de Cauchy-Schwarz démontrée ci-dessus avec un vecteur $y \in E$ quelconque :
$$ (b(x,y))^2 \le q(x)q(y) = 0 \cdot q(y) = 0 $$
Un carré d'un nombre réel étant toujours positif ou nul, si $(b(x,y))^2 \le 0$, on a obligatoirement $(b(x,y))^2 = 0$, soit $b(x,y) = 0$.
Puisque cela est vrai pour tout $y \in E$, on en conclut que $x \in \ker(b)$.
On a donc bien $N(q) = \ker(b)$. $\blacksquare$
