# Exercice 5 : Inégalité de Bessel $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $H$ un espace de Hilbert et $(e_n)_{n \in \mathbb{N}}$ une famille orthonormée (pas nécessairement une base hilbertienne).
Soit $x \in H$. On pose $s_N = \sum_{n=0}^N \langle x, e_n \rangle e_n$ la projection orthogonale de $x$ sur $F_N = \text{vect}(e_0, \dots, e_N)$.
1. Montrer que $\|s_N\|^2 = \sum_{n=0}^N |\langle x, e_n \rangle|^2$.
2. Montrer que $x - s_N$ est orthogonal à $s_N$.
3. En déduire l'inégalité de Bessel : $\sum_{n=0}^\infty |\langle x, e_n \rangle|^2 \leq \|x\|^2$.

**Correction détaillée :**
1. Calculons la norme au carré de $s_N$ :
   $\|s_N\|^2 = \langle s_N, s_N \rangle = \langle \sum_{n=0}^N \langle x, e_n \rangle e_n, \sum_{m=0}^N \langle x, e_m \rangle e_m \rangle$
   Par bilinéarité du produit scalaire :
   $\|s_N\|^2 = \sum_{n=0}^N \sum_{m=0}^N \langle x, e_n \rangle \overline{\langle x, e_m \rangle} \langle e_n, e_m \rangle$
   Puisque la famille est orthonormée, $\langle e_n, e_m \rangle = \delta_{nm}$. La double somme se réduit à une somme simple :
   $\|s_N\|^2 = \sum_{n=0}^N \langle x, e_n \rangle \overline{\langle x, e_n \rangle} = \sum_{n=0}^N |\langle x, e_n \rangle|^2$.

2. Calculons le produit scalaire entre $x - s_N$ et un vecteur de base $e_k$ (pour $0 \leq k \leq N$) :
   $\langle x - s_N, e_k \rangle = \langle x, e_k \rangle - \langle \sum_{n=0}^N \langle x, e_n \rangle e_n, e_k \rangle$
   $\langle x - s_N, e_k \rangle = \langle x, e_k \rangle - \sum_{n=0}^N \langle x, e_n \rangle \langle e_n, e_k \rangle$
   $\langle x - s_N, e_k \rangle = \langle x, e_k \rangle - \langle x, e_k \rangle \cdot 1 = 0$
   Le vecteur $x - s_N$ est orthogonal à chaque $e_k$ de $F_N$.
   Par combinaison linéaire, $x - s_N$ est orthogonal à tout élément de $F_N$.
   Puisque $s_N \in F_N$, on a $\langle x - s_N, s_N \rangle = 0$.

3. Appliquons le théorème de Pythagore à la décomposition $x = (x - s_N) + s_N$ :
   Puisque $x - s_N \perp s_N$, on a $\|x\|^2 = \|x - s_N\|^2 + \|s_N\|^2$.
   Donc $\|s_N\|^2 = \|x\|^2 - \|x - s_N\|^2$.
   Puisque $\|x - s_N\|^2 \geq 0$, on obtient $\|s_N\|^2 \leq \|x\|^2$.
   En remplaçant $\|s_N\|^2$ par l'expression trouvée à la question 1 :
   $\sum_{n=0}^N |\langle x, e_n \rangle|^2 \leq \|x\|^2$.
   Cette inégalité étant vraie pour tout entier $N \geq 0$, et la suite des sommes partielles étant croissante (termes positifs) et majorée par $\|x\|^2$, la série converge et sa limite vérifie l'inégalité de Bessel :
   $\sum_{n=0}^\infty |\langle x, e_n \rangle|^2 \leq \|x\|^2$.
