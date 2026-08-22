# Exercice 10 : Mesure de comptage et passage à la limite $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Montrer que pour toute fonction positive sur $\mathbb{N}$ (i.e. $f : \mathbb{N} \to [0, +\infty]$), l'intégrale par rapport à la mesure de comptage $\mu$ est équivalente à la somme d'une série :
$\int_{\mathbb{N}} f \, d\mu = \sup_{K \subset \mathbb{N}, K \text{ fini}} \sum_{k \in K} f(k) = \sum_{k=0}^{\infty} f(k)$

**Correction Détaillée :**
1. Toute partie de $\mathbb{N}$ est mesurable, et $\mu(A) = \text{Card}(A)$.
2. Soit $\alpha = \sup_{K \subset \mathbb{N}, K \text{ fini}} \sum_{k \in K} f(k)$.
3. Montrons que $\int f \, d\mu \ge \alpha$.
   Soit $K \subset \mathbb{N}$ un ensemble fini. Posons la fonction étagée $s_K = \sum_{k \in K} f(k) \mathbf{1}_{\{k\}}$.
   Clairement $s_K \in \mathcal{E}_+$ et $s_K \le f$ sur tout $\mathbb{N}$.
   L'intégrale vaut $\int s_K \, d\mu = \sum_{k \in K} f(k) \mu(\{k\}) = \sum_{k \in K} f(k)$.
   Par définition de l'intégrale de $f$ comme supremum sur tous les minorants étagés, on a :
   $\int f \, d\mu \ge \int s_K \, d\mu = \sum_{k \in K} f(k)$.
   Ceci est vrai pour tout ensemble fini $K$, donc en passant au sup, $\int f \, d\mu \ge \alpha$.
4. Montrons l'inégalité inverse $\int f \, d\mu \le \alpha$.
   Soit $s = \sum_{i=1}^m a_i \mathbf{1}_{A_i}$ une fonction étagée telle que $0 \le s \le f$.
   Son intégrale est $I = \sum_{i=1}^m a_i \mu(A_i)$.
   Si l'intégrale $I$ est infinie, c'est qu'un $a_i > 0$ correspond à un $A_i$ de mesure infinie. Donc $A_i$ contient une infinité d'entiers sur lesquels $f(k) \ge a_i$. En prenant $K \subset A_i$ fini mais arbitrairement grand, la somme partielle $\sum_{K} f(k)$ diverge vers $+\infty$, donc $\alpha = +\infty$, et l'inégalité $I \le \alpha$ est triviale.
   Si $I$ est finie, alors les $A_i$ pour lesquels $a_i > 0$ sont finis. Leur union est un ensemble fini $K^*$.
   Sur $K^*$, $s(k) \le f(k)$. L'intégrale de $s$ s'écrit $\int s \, d\mu = \sum_{k \in K^*} s(k) \le \sum_{k \in K^*} f(k)$.
   Cette dernière somme est par définition majorée par $\alpha$.
   Donc pour toute fonction étagée $s \le f$, on a $\int s \, d\mu \le \alpha$. Le supremum sur les étagées respecte la borne, d'où $\int f \, d\mu \le \alpha$.
5. Par double inégalité, l'égalité est démontrée. La notation de série infinie $\sum_{k=0}^{\infty} f(k)$ est exactement la définition analytique de ce supremum sur les sommes finies pour des termes positifs.
