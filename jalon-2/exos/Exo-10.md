# Exercice 10 - Difficulté: Niveau 5.5

## 1. Énoncé
Déterminer toutes les fonctions continues $f: \mathbb{R} \to \mathbb{R}$ telles que pour tout $x,y \in \mathbb{R}, f(x+f(y)) = f(x) + y$.

## 2. Démonstration (Zéro Ellipse)
**Analyse :** Soit $f$ une telle fonction. 1. Montrons que $f$ est bijective. Soient $y_1, y_2 \in \mathbb{R}$ tels que $f(y_1) = f(y_2)$. Alors $f(x+f(y_1)) = f(x+f(y_2))$ pour tout $x$. En utilisant l'équation fonctionnelle, on a $f(x) + y_1 = f(x) + y_2$. En soustrayant $f(x)$, on obtient $y_1 = y_2$. $f$ est donc injective. Pour la surjectivité, soit $z \in \mathbb{R}$. Fixons $x = 0$. On cherche $y$ tel que $f(f(y)) = f(0) + y$. Mais cela ne donne pas directement $f(w)=z$. Prenons plutôt $x=0$, alors $f(f(y)) = f(0) + y$. Pour atteindre n'importe quel $z \in \mathbb{R}$, il suffit de poser $y = z - f(0)$. Alors $f(f(z-f(0))) = f(0) + z - f(0) = z$. Donc l'élément $w = f(z-f(0))$ est un antécédent de $z$. $f$ est surjective. $f$ est donc bijective.
2. Il existe donc un unique élément $a \in \mathbb{R}$ tel que $f(a) = 0$. Posons $y = a$ dans l'équation de départ : $f(x+f(a)) = f(x) + a$. Comme $f(a) = 0$, $f(x+0) = f(x) + a$. Soit $f(x) = f(x) + a$. En soustrayant $f(x)$, on obtient $a = 0$. Donc $f(0) = 0$.
3. Posons $x = 0$ dans l'équation de départ : $f(0+f(y)) = f(0) + y$. Soit $f(f(y)) = y$. $f$ est donc une involution.
4. Posons $x = f(x')$ et $y = f(y')$. L'équation $f(x+f(y)) = f(x) + y$ devient : $f(f(x') + f(f(y'))) = f(f(x')) + f(y')$. Comme $f(f(u)) = u$ pour tout $u$, on a : $f(f(x') + y') = x' + f(y')$. En appliquant $f$ des deux côtés, on trouve : $f(f(f(x') + y')) = f(x' + f(y'))$. Soit $f(x') + y' = f(x') + y'$ (ce qui ne donne rien de nouveau). En fait, reprenons : $f(x + f(y)) = f(x) + y$. Appliquons cela pour $x$ quelconque et $y = f(z)$ : $f(x + f(f(z))) = f(x) + f(z)$. Soit $f(x+z) = f(x) + f(z)$. $f$ vérifie l'équation de Cauchy.
5. $f$ vérifie l'équation de Cauchy $f(x+z) = f(x) + f(z)$. Comme on a supposé $f$ continue, la seule famille de solutions est celle des fonctions linéaires $f(x) = cx$ avec $c \in \mathbb{R}$.
En injectant $f(x) = cx$ dans $f(f(x)) = x$, on obtient $c(cx) = x \implies c^2 x = x$ pour tout $x$, d'où $c^2 = 1$, et donc $c = 1$ ou $c = -1$. Les seules solutions continues sont $f(x) = x$ et $f(x) = -x$.
**Synthèse :** Si $f(x) = x$, alors $f(x+f(y)) = (x+y) = x+y$ et $f(x)+y = x+y$. (Valide) Si $f(x) = -x$, alors $f(x+f(y)) = -(x-y) = -x+y$ et $f(x)+y = -x+y$. (Valide) Les deux fonctions continues solutions sont $f(x)=x$ et $f(x)=-x$.
