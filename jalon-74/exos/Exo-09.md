### Exercice 9 : Continuité du produit scalaire via Cauchy-Schwarz \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit un espace de Hilbert $H$. En utilisant l'inégalité de Cauchy-Schwarz, montrer que le produit scalaire $\langle \cdot, \cdot \rangle : H \times H \to \mathbb{R}$ est continu conjointement.

**Correction Détaillée :**
1. Pour montrer la continuité, on doit borner la différence $|\langle x_n, y_n \rangle - \langle x, y \rangle|$ lorsque $x_n \to x$ et $y_n \to y$ dans $H$.
2. On utilise l'astuce classique d'ajout/soustraction d'un terme croisé :
$$\langle x_n, y_n \rangle - \langle x, y \rangle = \langle x_n, y_n \rangle - \langle x_n, y \rangle + \langle x_n, y \rangle - \langle x, y \rangle$$
3. Par bilinéarité du produit scalaire :
$$= \langle x_n, y_n - y \rangle + \langle x_n - x, y \rangle$$
4. En prenant la valeur absolue et en appliquant l'inégalité triangulaire :
$$|\langle x_n, y_n \rangle - \langle x, y \rangle| \le |\langle x_n, y_n - y \rangle| + |\langle x_n - x, y \rangle|$$
5. On applique l'inégalité de Cauchy-Schwarz (cas $p=2$ de Hölder) à chaque terme :
$$\le \|x_n\| \|y_n - y\| + \|x_n - x\| \|y\|$$
6. Puisque $x_n \to x$, la suite $(x_n)$ est convergente donc bornée : il existe $M > 0$ tel que $\|x_n\| \le M$ pour tout $n$.
7. Ainsi, $|\langle x_n, y_n \rangle - \langle x, y \rangle| \le M \|y_n - y\| + \|y\| \|x_n - x\|$.
8. Comme $\|y_n - y\| \to 0$ et $\|x_n - x\| \to 0$, le membre de droite tend vers 0. Ceci prouve la continuité conjointe.
