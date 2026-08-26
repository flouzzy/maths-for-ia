### Mesure de comptage et séries \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X = \mathbb{N}$ muni de la tribu discrète $\mathcal{P}(\mathbb{N})$ et de la mesure de comptage $\mu$.
Montrer que pour toute fonction $f : \mathbb{N} \to \mathbb{R}_+$, l'intégrale de Lebesgue de $f$ par rapport à $\mu$ coïncide avec la somme de la série de terme général $f(n)$ :
$$\int_{\mathbb{N}} f d\mu = \sum_{n=0}^\infty f(n)$$

**Correction Détaillée :**
**Étape 1 : Cas des fonctions simples.**
Soit $s$ une fonction simple positive sur $\mathbb{N}$ s'annulant en dehors d'un sous-ensemble fini $K \subset \mathbb{N}$.
Elle s'écrit $s = \sum_{n \in K} s(n) \mathbf{1}_{\{n\}}$.
Son intégrale par rapport à la mesure de comptage est :
$$\int_{\mathbb{N}} s d\mu = \sum_{n \in K} s(n) \mu(\{n\})$$
Puisque $\mu$ est la mesure de comptage, pour tout singleton, $\mu(\{n\}) = 1$.
Donc $\int_{\mathbb{N}} s d\mu = \sum_{n \in K} s(n)$.

**Étape 2 : Approximation de la fonction mesurable positive.**
Soit $f \in \mathcal{M}_+$. Définissons une suite croissante de fonctions simples $(s_N)_{N \in \mathbb{N}}$ par :
$$s_N(n) = f(n) \mathbf{1}_{\{0, 1, \dots, N\}}(n)$$
Il est clair que $0 \le s_N \le f$ pour tout $N$.

**Étape 3 : Utilisation de la définition par le supremum.**
Par définition, $\int_{\mathbb{N}} f d\mu = \sup \left\{ \int_{\mathbb{N}} s d\mu \mid 0 \le s \le f, s \text{ simple} \right\}$.
D'une part, comme $s_N \le f$, on a :
$$\int_{\mathbb{N}} s_N d\mu = \sum_{n=0}^N f(n) \le \int_{\mathbb{N}} f d\mu$$
En passant à la limite quand $N \to \infty$ (ou à la borne supérieure), on obtient :
$$\sum_{n=0}^\infty f(n) \le \int_{\mathbb{N}} f d\mu$$

**Étape 4 : Inégalité inverse.**
Soit $s$ une fonction simple quelconque telle que $0 \le s \le f$.
Soit $s = \sum_{i=1}^k a_i \mathbf{1}_{A_i}$.
Si un $A_i$ est infini et $a_i > 0$, alors $\int_{\mathbb{N}} s d\mu = \infty$. Comme $s \le f$, on a alors $a_i \le f(n)$ pour une infinité de $n$, d'où $\sum_{n=0}^\infty f(n) = \infty$, l'égalité est triviale.
Si tous les $A_i$ pour lesquels $a_i > 0$ sont finis, alors $s$ ne prend des valeurs non nulles que sur un ensemble fini $K$.
$$\int_{\mathbb{N}} s d\mu = \sum_{n \in K} s(n) \le \sum_{n \in K} f(n) \le \sum_{n=0}^\infty f(n)$$
Puisque ceci est vrai pour toute fonction simple $s \le f$, en prenant le supremum sur $s$, on a :
$$\int_{\mathbb{N}} f d\mu \le \sum_{n=0}^\infty f(n)$$

**Conclusion :**
Les deux inégalités démontrent l'égalité. L'intégrale de Lebesgue subsume ainsi la théorie des séries à termes positifs.
