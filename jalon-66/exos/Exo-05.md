## Exercice 5 : Égalité presque partout \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :** Soient $f, g \in \mathcal{M}_+$ deux fonctions mesurables positives. Montrer que si $f = g$ presque partout, alors $\int f d\mu = \int g d\mu$.

**Correction Détaillée :**
1. Notons $N = \{x \in X \mid f(x) \neq g(x)\}$. Par hypothèse, $\mu(N) = 0$.
2. Posons $h(x) = |f(x) - g(x)|$. La fonction $h$ est mesurable positive.
   Pour tout $x \in X$, $h(x) = h(x) \cdot \mathbf{1}_N(x) + h(x) \cdot \mathbf{1}_{X \setminus N}(x)$.
   Puisque $h(x) = 0$ pour $x \in X \setminus N$, on a $h = h \cdot \mathbf{1}_N$.
3. Soit $s$ une fonction simple positive telle que $s \le h$. Alors $s$ est nulle hors de $N$, donc $s = s \cdot \mathbf{1}_N$.
   $s$ s'écrit $\sum_{i=1}^n a_i \mathbf{1}_{A_i}$. On peut remplacer chaque $A_i$ par $A_i \cap N$.
   L'intégrale de $s$ est $\sum a_i \mu(A_i \cap N) = 0$ car $\mu(A_i \cap N) \le \mu(N) = 0$.
4. Ainsi, $\int h d\mu = \sup \int s d\mu = 0$.
5. On a $f(x) \le g(x) + h(x)$. Par monotonie et sous-additivité (admise pour le moment ou prouvée via fonctions simples) de l'intégrale pour des fonctions positives :
   $$\int f d\mu \le \int g d\mu + \int h d\mu = \int g d\mu + 0 = \int g d\mu$$
6. Par symétrie, $g(x) \le f(x) + h(x)$, d'où $\int g d\mu \le \int f d\mu$.
7. On conclut que $\int f d\mu = \int g d\mu$.
