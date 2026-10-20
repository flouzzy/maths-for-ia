# Exercice 10 : Théorème de Lindeberg et variables non identiquement distribuées \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(X_n)_{n \ge 1}$ une suite de variables aléatoires indépendantes mais **non identiquement distribuées**. On note $\mu_k = \mathbb{E}[X_k]$ et $\sigma_k^2 = \text{Var}(X_k)$. On pose $s_n^2 = \sum_{k=1}^n \sigma_k^2$.
La condition de Lindeberg stipule que pour tout $\epsilon > 0$ :
$$\lim_{n \to \infty} \frac{1}{s_n^2} \sum_{k=1}^n \mathbb{E}\left[ (X_k - \mu_k)^2 \mathbf{1}_{|X_k - \mu_k| > \epsilon s_n} \right] = 0$$
Montrer que si les $X_n$ sont uniformément bornées (i.e. il existe $M > 0$ tel que $\mathbb{P}(|X_n| \le M) = 1$ pour tout $n$) et si $s_n \to \infty$, alors la condition de Lindeberg est vérifiée, ce qui entraîne la validité du TCL :
$$\frac{\sum_{k=1}^n (X_k - \mu_k)}{s_n} \xrightarrow{\mathcal{L}} \mathcal{N}(0, 1)$$

**Correction :**

Nous devons vérifier la condition de Lindeberg sous les hypothèses données.
Les variables $X_k$ sont presque sûrement bornées par $M$.
L'espérance $|\mu_k| = |\mathbb{E}[X_k]| \le \mathbb{E}[|X_k|] \le M$.
Par l'inégalité triangulaire, pour tout $k$ :
$$|X_k - \mu_k| \le |X_k| + |\mu_k| \le M + M = 2M \quad \text{presque sûrement}.$$

Fixons $\epsilon > 0$.
On observe la fonction indicatrice $\mathbf{1}_{|X_k - \mu_k| > \epsilon s_n}$.
Puisque $s_n \to \infty$ quand $n \to \infty$, il existe un entier $N$ tel que pour tout $n \ge N$, on a $\epsilon s_n > 2M$.
Ainsi, pour tout $n \ge N$ et pour tout $k \le n$, l'événement $\{|X_k - \mu_k| > \epsilon s_n\}$ devient impossible, puisque la quantité $|X_k - \mu_k|$ est bornée supérieurement par $2M$.
L'indicatrice est alors identiquement nulle presque sûrement :
$$\mathbf{1}_{|X_k - \mu_k| > \epsilon s_n} = 0 \quad p.s.$$

Par suite, l'espérance est nulle :
$$\mathbb{E}\left[ (X_k - \mu_k)^2 \mathbf{1}_{|X_k - \mu_k| > \epsilon s_n} \right] = 0$$
Et la somme de ces termes est nulle pour tout $n \ge N$.
Donc la limite de la somme divisée par $s_n^2$ est trivialement nulle :
$$\lim_{n \to \infty} \frac{1}{s_n^2} \sum_{k=1}^n 0 = 0$$

La condition de Lindeberg est donc vérifiée.
Selon le théorème de Lindeberg-Feller, cette condition est suffisante pour que la somme normalisée converge en loi vers la normale standard.

**Interprétation :**
Ce corollaire très puissant démontre que le TCL s'applique à des variables hétérogènes (non I.I.D.) pourvu qu'aucune d'entre elles ne domine la variance totale (la condition de borne globale empêche les queues de distribution lourdes de perturber la moyenne globale, tandis que $s_n \to \infty$ garantit que l'accumulation des variances individuelles est suffisante pour créer la cloche gaussienne).
