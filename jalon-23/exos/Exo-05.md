# Exercice 5 : Équation différentielle et résolution par séries entières

**Énoncé :**
On cherche les solutions développables en série entière au voisinage de $0$ de l'équation différentielle linéaire $(E) : y' - 2xy = 0$. Déterminer l'expression de la fonction somme.

**Correction détaillée :**
Supposons, par analyse, qu'il existe une solution de l'équation $(E)$ développable en série entière.
Soit $y(x) = \sum_{n=0}^{+\infty} a_n x^n$ une telle fonction, de rayon de convergence strictement positif $R > 0$.
Par les théorèmes de régularité analytique, $y$ est dérivable sur $]-R, R[$ et sa dérivée s'obtient par dérivation terme à terme :
$$ y'(x) = \sum_{n=1}^{+\infty} n a_n x^{n-1} $$
L'équation différentielle $(E)$ impose formellement l'égalité : $y'(x) = 2x \cdot y(x)$.
Substituons les développements en séries :
$$ \sum_{n=1}^{+\infty} n a_n x^{n-1} = 2x \sum_{n=0}^{+\infty} a_n x^n = \sum_{n=0}^{+\infty} 2 a_n x^{n+1} $$
Il convient maintenant d'unifier les puissances de $x$ par réindexation, pour procéder à l'identification des coefficients.
Dans le membre de gauche, posons $k = n-1$, soit $n = k+1$. L'indice démarre à $k = 1-1=0$.
$$ \text{Gauche} = \sum_{k=0}^{+\infty} (k+1) a_{k+1} x^k $$
Dans le membre de droite, posons $k = n+1$, soit $n = k-1$. L'indice démarre à $k = 0+1=1$.
$$ \text{Droite} = \sum_{k=1}^{+\infty} 2 a_{k-1} x^k $$
L'égalité s'écrit donc formellement pour tout $x \in ]-R, R[$ :
$$ a_1 x^0 + \sum_{k=1}^{+\infty} (k+1) a_{k+1} x^k = \sum_{k=1}^{+\infty} 2 a_{k-1} x^k $$
Par unicité du développement en série entière d'une fonction analytique nulle, l'identification des coefficients donne les relations de récurrence suivantes :
- Pour $k = 0$ : $a_1 = 0$.
- Pour $k \geq 1$ : $(k+1)a_{k+1} = 2 a_{k-1}$, ce qui conduit à $a_{k+1} = \frac{2}{k+1} a_{k-1}$.
Cette relation lie les termes d'un indice à celui le précédant de deux pas. Il y a découplage total entre les termes d'indices pairs et impairs.
- Termes de rang impair : puisque $a_1 = 0$, la récurrence injecte un facteur multiplicatif nul à toutes les étapes impaires : $a_3 = a_5 = a_{2p+1} = 0$ pour tout entier $p$.
- Termes de rang pair : posons $a_{2p}$. La récurrence pour l'indice $2p$ (donc $k+1=2p$, soit $k=2p-1$) s'écrit :
$$ a_{2p} = \frac{2}{2p} a_{2p-2} = \frac{1}{p} a_{2p-2} $$
Par itération évidente de type télescopique :
$$ a_{2p} = \frac{1}{p} \cdot \frac{1}{p-1} \cdot ... \cdot \frac{1}{1} a_0 = \frac{a_0}{p!} $$
Ainsi, l'unique paramètre libre est $a_0$, qui n'est autre que la condition initiale $y(0)$.
L'expression de la série est alors reconstruite, tous les termes impairs étant annihilés :
$$ y(x) = \sum_{p=0}^{+\infty} a_{2p} x^{2p} = \sum_{p=0}^{+\infty} \frac{a_0}{p!} x^{2p} = a_0 \sum_{p=0}^{+\infty} \frac{(x^2)^p}{p!} $$
Nous reconnaissons le développement canonique de la fonction exponentielle évaluée au point $x^2$.
La série converge sur tout $\mathbb{R}$ (rayon infini).
L'unique famille de solutions analytiques est formellement $y(x) = a_0 e^{x^2}$.
