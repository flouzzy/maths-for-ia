# Exercice 6 : L'intégrale comme somme de série
$\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit l'espace $\mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$.
Soit $f : \mathbb{N} \to \mathbb{R}_+$. On pose $u_n = f(n)$.
Montrer en utilisant la définition par le supremum que :
$$\int_{\mathbb{N}} f \, d\mu = \sum_{n=0}^\infty u_n$$

**Correction :**
1. **Étape 1 : Minoration par les sommes partielles (fonctions étagées).**
   Soit $N \in \mathbb{N}$. Considérons la fonction $s_N = \sum_{n=0}^N u_n \mathbf{1}_{\{n\}}$.
   La fonction $s_N$ est étagée (elle prend un nombre fini de valeurs non nulles, qui sont les $u_n$, sur les singletons $\{n\}$).
   Pour tout $k \in \mathbb{N}$, si $k \le N$, $s_N(k) = u_k = f(k)$. Si $k > N$, $s_N(k) = 0 \le f(k)$.
   Ainsi, ponctuellement, $0 \le s_N \le f$.
   L'intégrale de cette fonction étagée est :
   $$\int_{\mathbb{N}} s_N \, d\mu = \sum_{n=0}^N u_n \mu(\{n\}) = \sum_{n=0}^N u_n \cdot 1 = \sum_{n=0}^N u_n$$
   Par définition de l'intégrale de $f$ (supremum sur les étagées minorantes) :
   $$\forall N \in \mathbb{N}, \quad \int_{\mathbb{N}} f \, d\mu \ge \sum_{n=0}^N u_n$$
   En passant à la limite quand $N \to +\infty$ :
   $$\int_{\mathbb{N}} f \, d\mu \ge \sum_{n=0}^\infty u_n$$

2. **Étape 2 : Majoration par la somme totale.**
   Soit $s$ une fonction étagée positive arbitraire telle que $0 \le s \le f$.
   La fonction $s$ prend la valeur $a_i > 0$ sur des ensembles $A_i$ ($1 \le i \le k$).
   L'intégrale de $s$ est $\int s d\mu = \sum_{i=1}^k a_i \mu(A_i)$.
   - Si au moins un ensemble $A_i$ est infini, sa mesure est $+\infty$. L'intégrale de $s$ vaut $+\infty$. Mais sur cet ensemble infini, on a $f(n) \ge a_i > 0$ pour une infinité d'indices. La série $\sum u_n$ diverge donc vers $+\infty$, et l'inégalité $s \le f$ garantit que $\sum u_n = +\infty \ge \int s$.
   - Si tous les ensembles $A_i$ sont finis, alors $s$ n'est non nulle que sur un nombre fini d'entiers, disons $\{0, 1, \dots, N\}$.
     $$\int s \, d\mu = \sum_{n=0}^N s(n) \mu(\{n\}) = \sum_{n=0}^N s(n) \le \sum_{n=0}^N f(n) = \sum_{n=0}^N u_n \le \sum_{n=0}^\infty u_n$$
   Dans les deux cas, pour toute étagée $s \le f$, on a $\int s \, d\mu \le \sum_{n=0}^\infty u_n$.
   En prenant le supremum sur toutes les $s \in \mathcal{E}_+(f)$ :
   $$\int_{\mathbb{N}} f \, d\mu \le \sum_{n=0}^\infty u_n$$

3. **Conclusion :**
   Par double inégalité, l'intégrale de Lebesgue relativement à la mesure de comptage coïncide avec la somme de la série.
