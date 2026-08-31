## Exercice 10 : Application aux espaces $L^1$ \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions de $L^1(X, \mu)$ convergeant ponctuellement vers $f$. On suppose qu'il existe une fonction $F \in L^1$ telle que $\forall n, |f_n| \le F$ p.p.
En utilisant le théorème de Beppo Levi (ou plutôt son corollaire qui donne Fatou, voir exercice précédent), démontrer que $f \in L^1$ et $\lim \int |f_n - f| d\mu = 0$ (C'est le Théorème de Convergence Dominée).

**Correction Détaillée :**
1. Comme $|f_n| \le F$, à la limite $|f| \le F$. Puisque $F \in L^1$, on a $f \in L^1$.
2. Considérons la suite de fonctions positives : $g_n = 2F - |f_n - f|$.
   Puisque $|f_n| \le F$ et $|f| \le F$, l'inégalité triangulaire donne $|f_n - f| \le 2F$, donc $g_n \ge 0$.
3. La limite simple de $g_n$ est $\lim (2F - |f_n - f|) = 2F - 0 = 2F$.
4. Appliquons le Lemme de Fatou (démontré via TCM) à la suite positive $g_n$ :
   $\int \liminf g_n \le \liminf \int g_n$.
   Ici la limite existe, donc $\liminf = \lim$.
   $\int 2F \le \liminf \int (2F - |f_n - f|) = \int 2F - \limsup \int |f_n - f|$.
5. Les quantités $\int 2F$ sont finies (car $F \in L^1$). On peut donc les soustraire de l'inégalité :
   $0 \le -\limsup \int |f_n - f|$, ce qui implique $\limsup \int |f_n - f| \le 0$.
6. Or, l'intégrale est positive, donc $\liminf \int |f_n - f| \ge 0$.
7. Finalement, $0 \le \liminf \int |f_n - f| \le \limsup \int |f_n - f| \le 0$.
   La limite existe donc et vaut 0 : $\lim \int |f_n - f| d\mu = 0$.
   La convergence dans $L^1$ implique la convergence des intégrales : $\int f_n \to \int f$.
