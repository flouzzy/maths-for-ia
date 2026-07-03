# Exercice 5: Intersection de deux hyperplans
## Énoncé
Soit $E$ un espace vectoriel de dimension $n \ge 2$. Soient $H_1$ et $H_2$ deux hyperplans de $E$.
Montrer que si $H_1 \neq H_2$, alors $\dim(H_1 \cap H_2) = n - 2$.


## Correction détaillée
Soit $\varphi_1, \varphi_2 \in E^*$ deux formes linéaires non nulles telles que $H_1 = \ker(\varphi_1)$ et $H_2 = \ker(\varphi_2)$.
Considérons l'application linéaire définie par :
$\Phi : E \to \mathbb{K}^2$
$x \mapsto (\varphi_1(x), \varphi_2(x))$

Le noyau de $\Phi$ est constitué des vecteurs $x$ tels que $\varphi_1(x) = 0$ et $\varphi_2(x) = 0$.
Ainsi, $\ker(\Phi) = \ker(\varphi_1) \cap \ker(\varphi_2) = H_1 \cap H_2$.

D'après le théorème du rang, nous avons :
$\dim(E) = \dim(\ker(\Phi)) + \text{rg}(\Phi)$
$n = \dim(H_1 \cap H_2) + \dim(\text{Im}(\Phi))$

L'image $\text{Im}(\Phi)$ est un sous-espace vectoriel de $\mathbb{K}^2$. Sa dimension est donc au plus 2.
Supposons par l'absurde que $\text{rg}(\Phi) < 2$.
Si $\text{rg}(\Phi) = 0$, alors $\Phi$ est l'application nulle, ce qui contredit $\varphi_1 \neq 0$.
Si $\text{rg}(\Phi) = 1$, alors l'image de $\Phi$ est une droite vectorielle de $\mathbb{K}^2$. Cela signifie que les vecteurs images sont tous colinéaires.
Il existerait alors des scalaires $(a, b) \neq (0,0)$ tels que pour tout $x \in E$, $a\varphi_1(x) + b\varphi_2(x) = 0$.
Donc $a\varphi_1 + b\varphi_2 = 0$. Les formes linéaires $\varphi_1$ et $\varphi_2$ seraient proportionnelles (colinéaires).
Or, deux formes linéaires proportionnelles et non nulles définissent le même noyau (le même hyperplan). On aurait alors $H_1 = H_2$, ce qui contredit l'hypothèse $H_1 \neq H_2$.

Par conséquent, l'hypothèse $\text{rg}(\Phi) < 2$ est fausse. La seule possibilité est $\text{rg}(\Phi) = 2$, ce qui signifie que $\Phi$ est surjective sur $\mathbb{K}^2$.
En remplaçant dans l'égalité du théorème du rang, nous obtenons :
$n = \dim(H_1 \cap H_2) + 2 \implies \dim(H_1 \cap H_2) = n - 2$.
La dimension de l'intersection de deux hyperplans distincts est exactement $n - 2$.
