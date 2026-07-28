---
uuid: "jalon-26-exo-01"
title: "Produit scalaire usuel et Cauchy-Schwarz"
difficulty: 1
---

# Exercice 1 : Produit scalaire usuel et Cauchy-Schwarz (Difficulté ★☆☆☆☆)

L'espace vectoriel euclidien canonique par excellence est $E = \mathbb{R}^n$, muni de son produit scalaire usuel défini par $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$ pour tous vecteurs $x = (x_1, \ldots, x_n)$ et $y = (y_1, \ldots, y_n)$. Cet exercice se propose de redémontrer de manière purement algébrique l'inégalité fondamentale de Cauchy-Schwarz, pilier de l'analyse fonctionnelle et de la géométrie, puis d'en déduire une inégalité entre la norme $L^1$ et la norme $L^2$ en dimension finie.

1. Redémontrer rigoureusement l'inégalité de Cauchy-Schwarz dans ce cas particulier en étudiant le trinôme du second degré $P(t) = \sum_{i=1}^n (x_i + t y_i)^2$.
2. En déduire que pour tout $x \in \mathbb{R}^n$, $\sum_{i=1}^n |x_i| \le \sqrt{n} \sqrt{\sum_{i=1}^n x_i^2}$.
3. Discuter et caractériser géométriquement les vecteurs $x$ pour lesquels cette inégalité devient une égalité stricte.

## Démonstration Rigoureuse à Blanc

1. Fixons deux vecteurs quelconques $x, y \in \mathbb{R}^n$. Si $y = (0, \ldots, 0)$, l'inégalité de Cauchy-Schwarz s'écrit $0 \le 0$, ce qui est trivialement vérifié, et la famille $(x, y)$ est liée. Supposons à présent que $y \neq 0_{\mathbb{R}^n}$. Considérons l'expression de la norme au carré d'une combinaison linéaire de $x$ et $y$, ce qui définit naturellement un polynôme $P$ de la variable réelle $t$ :
   $$ P(t) = \sum_{i=1}^n (x_i + t y_i)^2 $$
   Par essence, cette somme de carrés de réels est toujours positive ou nulle. Ainsi, pour tout $t \in \mathbb{R}$, $P(t) \ge 0$. Développons algébriquement cette somme :
   $$ P(t) = \sum_{i=1}^n (x_i^2 + 2t x_i y_i + t^2 y_i^2) $$
   Par linéarité de la somme finie, nous pouvons regrouper les termes selon les puissances de $t$ :
   $$ P(t) = \left( \sum_{i=1}^n y_i^2 \right) t^2 + 2 \left( \sum_{i=1}^n x_i y_i \right) t + \left( \sum_{i=1}^n x_i^2 \right) $$
   Nous reconnaissons ici l'expression du produit scalaire canonique et de la norme euclidienne au carré. Posons $A = \sum_{i=1}^n y_i^2 = \|y\|^2 > 0$, $B = \sum_{i=1}^n x_i y_i = \langle x, y \rangle$ et $C = \sum_{i=1}^n x_i^2 = \|x\|^2$. Le polynôme s'écrit alors $P(t) = A t^2 + 2B t + C$.
   Puisque $A > 0$ et $P(t) \ge 0$ pour tout $t \in \mathbb{R}$, le trinôme ne change jamais de signe (il reste dans le demi-plan supérieur). Cela implique géométriquement que la parabole représentative de $P$ ne coupe l'axe des abscisses qu'en au plus un point, ou jamais. Algébriquement, le discriminant réduit de ce trinôme doit être négatif ou nul :
   $$ \Delta' = B^2 - AC \le 0 $$
   Substituons les expressions initiales :
   $$ \left( \sum_{i=1}^n x_i y_i \right)^2 - \left( \sum_{i=1}^n y_i^2 \right) \left( \sum_{i=1}^n x_i^2 \right) \le 0 $$
   $$ \langle x, y \rangle^2 \le \|x\|^2 \|y\|^2 $$
   En appliquant la fonction racine carrée, qui est strictement croissante sur $\mathbb{R}_+$, nous obtenons l'inégalité de Cauchy-Schwarz :
   $$ |\langle x, y \rangle| \le \|x\| \|y\| $$

2. Soit $x \in \mathbb{R}^n$. L'inégalité demandée fait intervenir la somme des valeurs absolues des coordonnées, ce qui évoque un produit scalaire particulier. Construisons un vecteur $y = (y_1, \ldots, y_n)$ qui fera apparaître cette somme. Définissons $y_i = 1$ si $x_i \ge 0$, et $y_i = -1$ si $x_i < 0$. Ainsi, pour tout $i$, le produit $x_i y_i$ correspond exactement à $|x_i|$. Le vecteur $y$ ainsi construit possède la propriété remarquable que $y_i^2 = 1$ pour tout $i \in \{1, \ldots, n\}$.
   Le produit scalaire de $x$ et $y$ donne donc :
   $$ \langle x, y \rangle = \sum_{i=1}^n x_i y_i = \sum_{i=1}^n |x_i| $$
   La norme euclidienne au carré de $y$ est simplement :
   $$ \|y\|^2 = \sum_{i=1}^n y_i^2 = \sum_{i=1}^n 1 = n \implies \|y\| = \sqrt{n} $$
   Appliquons maintenant l'inégalité de Cauchy-Schwarz démontrée à la question précédente à ces deux vecteurs $x$ et $y$ :
   $$ |\langle x, y \rangle| \le \|x\| \|y\| $$
   $$ \sum_{i=1}^n |x_i| \le \sqrt{\sum_{i=1}^n x_i^2} \sqrt{n} $$
   Ce qui démontre parfaitement l'inégalité recherchée.

3. L'égalité dans l'inégalité de Cauchy-Schwarz est atteinte si et seulement si les vecteurs impliqués sont liés (colinéaires). Dans le cadre de la question 2, cela signifie qu'il doit exister un scalaire $\lambda \in \mathbb{R}$ tel que $x = \lambda y$, c'est-à-dire que pour tout indice $i$, $x_i = \lambda y_i$.
   Puisque $y_i \in \{-1, 1\}$, en prenant la valeur absolue, nous obtenons :
   $$ |x_i| = |\lambda| |y_i| = |\lambda| $$
   Cela signifie que toutes les coordonnées du vecteur $x$ doivent avoir la même valeur absolue $|\lambda|$. Géométriquement, les vecteurs $x$ vérifiant l'égalité sont exactement ceux qui se situent sur les diagonales des "hypercubes" centrés à l'origine, où chaque composante $x_i$ vaut soit $c$, soit $-c$ pour une constante $c$ donnée.
   $\blacksquare$
