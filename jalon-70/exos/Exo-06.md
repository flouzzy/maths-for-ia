## Exercice 6 : Produit d'une mesure discrète et continue \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $c$ la mesure de comptage sur $(\mathbb{R}, \mathcal{P}(\mathbb{R}))$ et $\lambda$ la mesure de Lebesgue sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. On munit $\mathbb{R}^2$ de la tribu $\mathcal{P}(\mathbb{R}) \otimes \mathcal{B}(\mathbb{R})$.
Soit la diagonale $\Delta = \{(x,x) \mid x \in [0,1]\}$. Calculer les deux intégrales itérées $\int (\int \mathbf{1}_\Delta(x,y) d\lambda(y)) dc(x)$ et $\int (\int \mathbf{1}_\Delta(x,y) dc(x)) d\lambda(y)$.
Pourquoi sont-elles différentes ?

**Correction :**
1. Première intégrale : On intègre d'abord sur $y$. Pour un $x \in [0,1]$ fixé, la section $\Delta_x$ est le singleton $\{x\}$. Sa mesure de Lebesgue est $\lambda(\{x\}) = 0$.
   Donc $\int \mathbf{1}_\Delta(x,y) d\lambda(y) = 0$. L'intégrale extérieure par rapport à $c$ donne $0$.
2. Seconde intégrale : On intègre d'abord sur $x$. Pour un $y \in [0,1]$ fixé, la section "verticale" est le singleton $\{y\}$. Sa mesure de comptage est $c(\{y\}) = 1$.
   Donc $\int \mathbf{1}_\Delta(x,y) dc(x) = 1$ pour $y \in [0,1]$, et $0$ sinon. L'intégrale extérieure est $\int_{[0,1]} 1 d\lambda(y) = 1$.
3. Les deux intégrales donnent des résultats différents ($0 \neq 1$) car le théorème de Fubini ne s'applique pas. L'espace mesuré $(\mathbb{R}, \mathcal{P}(\mathbb{R}), c)$ n'est pas $\sigma$-fini.
