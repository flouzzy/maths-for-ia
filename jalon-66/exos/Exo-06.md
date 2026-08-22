# Exercice 6 : Intégrale de comptage et série géométrique $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
On considère l'espace mesurable $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$ muni de la mesure de comptage $\mu(A) = \operatorname{Card}(A)$.
Soit $f : \mathbb{N} \to \mathbb{R}_+$ définie par $f(n) = \frac{1}{3^n}$.
Calculer $\int_{\mathbb{N}} f \, d\mu$ en utilisant le théorème d'approximation par des fonctions étagées.

**Correction Détaillée :**
1. Posons pour tout entier $N \ge 0$, la fonction tronquée (qui est une fonction étagée car elle ne prend qu'un nombre fini de valeurs non nulles) :
   $s_N(n) = f(n)$ si $n \le N$, et $s_N(n) = 0$ si $n > N$.
   Formellement, $s_N = \sum_{k=0}^N \frac{1}{3^k} \mathbf{1}_{\{k\}}$.
2. L'intégrale de cette fonction étagée est :
   $$\int_{\mathbb{N}} s_N \, d\mu = \sum_{k=0}^N \frac{1}{3^k} \mu(\{k\}) = \sum_{k=0}^N \frac{1}{3^k}$$
   car la mesure de comptage d'un singleton est $1$.
3. La suite $(s_N)$ est manifestement croissante ($s_{N+1}(n) \ge s_N(n)$) et converge simplement vers $f$ sur $\mathbb{N}$.
4. Or, par définition de l'intégrale pour des fonctions mesurables positives (ou via le futur théorème de Beppo-Levi), l'intégrale de $f$ est le supremum des intégrales des fonctions étagées qui la minorent, et ce supremum est atteint par la limite de $\int s_N \, d\mu$.
5. Ainsi :
   $$\int_{\mathbb{N}} f \, d\mu = \lim_{N \to \infty} \sum_{k=0}^N \left(\frac{1}{3}\right)^k$$
6. On reconnaît la série géométrique de raison $1/3$, convergente car $|1/3| < 1$ :
   $$\int_{\mathbb{N}} f \, d\mu = \frac{1}{1 - 1/3} = \frac{1}{2/3} = \frac{3}{2}$$
