### Exercice 3 : L'inégalité de Jensen pour la variance \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que pour toute variable aléatoire $X$ admettant un moment d'ordre 2, $\mathbb{E}[X^2] \ge (\mathbb{E}[X])^2$.

**Correction Détaillée :**
1. Soit la fonction $\phi(x) = x^2$. Cette fonction est deux fois dérivable sur $\mathbb{R}$ et $\phi''(x) = 2 > 0$, donc elle est strictement convexe.
2. L'inégalité de Jensen stipule que pour une fonction convexe $\phi$, $\phi(\mathbb{E}[X]) \le \mathbb{E}[\phi(X)]$.
3. Appliquons ceci à notre fonction carré :
$$(\mathbb{E}[X])^2 \le \mathbb{E}[X^2]$$
4. En corollaire direct, la variance $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ est nécessairement positive ou nulle.
5. De plus, le cas d'égalité dans Jensen stricte se produit si et seulement si la variable aléatoire est constante presque sûrement. Donc $\text{Var}(X) = 0 \iff X = \mathbb{E}[X]$ p.s.
