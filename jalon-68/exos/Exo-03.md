## Exercice 3 : Intégrabilité et inégalité triangulaire \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $X$ un espace mesuré et $\mu$ une mesure. Soit $f \in \mathcal{L}^1(\mu)$ une fonction à valeurs réelles.
Montrer que $\left| \int_X f d\mu \right| \le \int_X |f| d\mu$.

**Correction :**
On utilise la décomposition $f = f^+ - f^-$.
1. Par définition, on a $\int f d\mu = \int f^+ d\mu - \int f^- d\mu$.
2. La valeur absolue de l'intégrale est :
   $\left| \int f d\mu \right| = \left| \int f^+ d\mu - \int f^- d\mu \right|$.
3. Par l'inégalité triangulaire usuelle pour les réels, $|a - b| \le |a| + |b|$, comme $\int f^+ d\mu \ge 0$ et $\int f^- d\mu \ge 0$, on a :
   $\left| \int f^+ d\mu - \int f^- d\mu \right| \le \int f^+ d\mu + \int f^- d\mu$.
4. De plus, $|f| = f^+ + f^-$. L'intégrale étant linéaire pour les fonctions positives :
   $\int |f| d\mu = \int (f^+ + f^-) d\mu = \int f^+ d\mu + \int f^- d\mu$.
5. On conclut donc bien que $\left| \int f d\mu \right| \le \int |f| d\mu$.
