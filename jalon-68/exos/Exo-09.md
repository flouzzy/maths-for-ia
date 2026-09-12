## Exercice 9 : Fatou et convergence en mesure \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions mesurables positives convergeant en mesure vers une fonction $f$.
Montrer que $\int f d\mu \le \liminf \int f_n d\mu$.
*(Indice : extraire une sous-suite).*

**Correction :**
1. Posons $l = \liminf \int f_n d\mu$. Si $l = +\infty$, l'inégalité est triviale. Supposons $l < \infty$.
2. Par définition de la limite inférieure, il existe une sous-suite $(f_{n_k})$ telle que $\lim_{k \to \infty} \int f_{n_k} d\mu = l$.
3. Comme $(f_{n_k})$ converge en mesure vers $f$, on peut en extraire une sous-sous-suite $(f_{n_{k_j}})$ qui converge presque partout vers $f$.
4. On applique le lemme de Fatou classique à la suite $(f_{n_{k_j}})$ :
   $\int (\liminf_{j \to \infty} f_{n_{k_j}}) d\mu \le \liminf_{j \to \infty} \int f_{n_{k_j}} d\mu$.
5. Puisque la sous-sous-suite converge p.p. vers $f$, $\liminf_{j \to \infty} f_{n_{k_j}} = f$ presque partout.
6. La suite réelle $(\int f_{n_{k_j}} d\mu)_j$ est une sous-suite de la suite convergente $(\int f_{n_k} d\mu)_k$, sa limite est donc $l$.
7. On obtient alors : $\int f d\mu \le l = \liminf \int f_n d\mu$.
