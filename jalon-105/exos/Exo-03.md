# Exercice 3 : Opérateur de multiplication dans $L^2$ $\bigstar\bigstar\star\star\star$
## Énoncé
Soit $H = L^2([0,1], \mathbb{C})$ muni du produit scalaire classique $\langle f, g \rangle = \int_0^1 f(t)\overline{g(t)} dt$.
Soit $m : [0,1] \to \mathbb{C}$ une fonction mesurable et bornée, c'est-à-dire qu'il existe $M > 0$ tel que $|m(t)| \le M$ presque partout.
On définit l'opérateur de multiplication $T_m : H \to H$ par $(T_m f)(t) = m(t)f(t)$.
1. Montrer que $T_m$ est bien un opérateur linéaire continu sur $H$.
2. Déterminer l'adjoint $T_m^*$ de $T_m$.
3. À quelle condition nécessaire et suffisante sur la fonction $m$ l'opérateur $T_m$ est-il auto-adjoint ?

## Correction
1. Linéarité : pour tous $f, g \in H$ et $\lambda, \mu \in \mathbb{C}$, on a pour presque tout $t \in [0, 1]$ :
$$ (T_m(\lambda f + \mu g))(t) = m(t)(\lambda f(t) + \mu g(t)) = \lambda m(t)f(t) + \mu m(t)g(t) = \lambda (T_m f)(t) + \mu (T_m g)(t) $$
Donc $T_m(\lambda f + \mu g) = \lambda T_m f + \mu T_m g$. L'opérateur est linéaire.
Continuité (caractérisée par le fait d'être borné) : Soit $f \in H$. Évaluons la norme au carré de $T_m f$ :
$$ \|T_m f\|_{L^2}^2 = \int_0^1 |m(t)f(t)|^2 dt = \int_0^1 |m(t)|^2 |f(t)|^2 dt $$
Puisque $m$ est bornée par $M$, on a $|m(t)|^2 \le M^2$ presque partout :
$$ \|T_m f\|_{L^2}^2 \le \int_0^1 M^2 |f(t)|^2 dt = M^2 \|f\|_{L^2}^2 $$
Donc $\|T_m f\|_{L^2} \le M \|f\|_{L^2}$. L'opérateur $T_m$ est continu (borné) et sa norme d'opérateur vérifie $\|T_m\| \le M$.

2. Calculons l'adjoint. Soient $f, g \in H$. Écrivons le produit scalaire $\langle T_m f, g \rangle$ :
$$ \langle T_m f, g \rangle = \int_0^1 (T_m f)(t) \overline{g(t)} dt = \int_0^1 m(t)f(t) \overline{g(t)} dt $$
Pour faire apparaître $f(t)$ isolément à gauche du produit pour identifier l'adjoint, nous modifions le groupement à l'intérieur de l'intégrale :
$$ = \int_0^1 f(t) (m(t)\overline{g(t)}) dt $$
Or, nous devons l'écrire sous la forme $\int_0^1 f(t) \overline{(T_m^* g)(t)} dt$. Sachant que $m(t)\overline{g(t)} = \overline{(\overline{m(t)}g(t))}$, on réécrit l'expression :
$$ = \int_0^1 f(t) \overline{(\overline{m(t)}g(t))} dt $$
Par identification dans le produit scalaire, nous avons $(T_m^* g)(t) = \overline{m(t)}g(t)$.
Ainsi, l'adjoint est l'opérateur de multiplication par la fonction conjuguée : $T_m^* = T_{\overline{m}}$.

3. Un opérateur est auto-adjoint si et seulement si $T_m = T_m^*$.
Cela signifie que pour toute fonction $f \in H$, $(T_m f)(t) = (T_m^* f)(t)$ presque partout.
Soit $m(t)f(t) = \overline{m(t)}f(t)$ pour tout $f$ et presque tout $t$.
En choisissant $f(t) = 1$ (qui est bien dans $L^2([0,1])$), on obtient $m(t) = \overline{m(t)}$ presque partout.
Ceci est la définition d'un nombre réel.
Conclusion : $T_m$ est auto-adjoint si et seulement si la fonction $m$ est à valeurs réelles presque partout.
