# Exercice 4 : Métrique induite sur une sphère
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé formel
Sur la sphère unité de $\mathbb{R}^3$, $S^2 = \left\lbrace  x \in \mathbb{R}^3 \mid \|x\|_2 = 1 \right\rbrace$, la distance géodésique entre deux points $x$ et $y$ est définie par $d_S(x,y) = \arccos(\langle x, y \rangle)$. Montrer que $d_S$ est bien une distance.

## Résolution pas à pas
**Étape 1 : L'angle comme métrique**

Le produit scalaire usuel donne $\langle x, y \rangle = \|x\| \|y\| \cos(\theta) = \cos(\theta)$ sur la sphère unité. L'arc cosinus renvoie la valeur principale $\theta \in [0, \pi]$, qui représente la longueur de l'arc de grand cercle géodésique.

**Étape 2 : Séparation et Symétrie**

- **Séparation :** $d_S(x,y) = 0 \iff \arccos(\langle x, y \rangle) = 0 \iff \langle x, y \rangle = 1$. Puisque $\|x\|=\|y\|=1$, le cas d'égalité de Cauchy-Schwarz indique que $x$ et $y$ sont positivement colinéaires, donc $x=y$.
- **Symétrie :** $d_S(x,y) = \arccos(\langle x, y \rangle) = \arccos(\langle y, x \rangle) = d_S(y,x)$ par symétrie du produit scalaire réel.

**Étape 3 : Inégalité triangulaire**

Soit $x, y, z \in S^2$. Considérons la trigonométrie sphérique. Le théorème fondamental sur les triangles sphériques énonce que la somme de deux côtés d'un triangle sphérique est toujours supérieure ou égale au troisième côté. La démonstration analytique repose sur l'algèbre des quaternions ou la géométrie différentielle (les géodésiques minimisent la longueur de l'arc). Plus élémentairement, en calculant $\|x \times z\|^2$, l'identité de Lagrange permet d'établir $\theta_{xz} \le \theta_{xy} + \theta_{yz}$. La géodésique reste le chemin le plus court sur la variété. $\blacksquare$
