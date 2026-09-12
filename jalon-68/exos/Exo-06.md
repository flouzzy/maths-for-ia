## Exercice 6 : Stabilité par produit avec une fonction bornée \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f \in \mathcal{L}^1(\mu)$ et $g$ une fonction mesurable et bornée sur $X$, i.e., il existe $M > 0$ tel que $|g(x)| \le M$ pour presque tout $x \in X$.
Montrer que le produit $fg \in \mathcal{L}^1(\mu)$.

**Correction :**
1. Pour prouver que $fg \in \mathcal{L}^1(\mu)$, on doit montrer que $\int |fg| d\mu < \infty$.
2. On sait que $|g(x)| \le M$ presque partout. Donc, $|f(x)g(x)| = |f(x)||g(x)| \le M|f(x)|$ presque partout.
3. Par croissance de l'intégrale (les deux fonctions étant positives ou nulles), on a :
   $\int |fg| d\mu \le \int M|f| d\mu = M \int |f| d\mu$.
4. Comme $f \in \mathcal{L}^1(\mu)$, $\int |f| d\mu$ est fini. Et comme $M$ est fini, $M \int |f| d\mu$ est fini.
5. Donc $\int |fg| d\mu < \infty$, ce qui prouve que $fg \in \mathcal{L}^1(\mu)$.
