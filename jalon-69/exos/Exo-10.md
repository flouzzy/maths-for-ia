##{Exercice 10 : Lemme de Scheffé (Corollaire du TCD) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

\textbf{Énoncé :}
Soit $(f_n)$ une suite de fonctions de $\mathcal{L}^1(\mu)$ et $f \in \mathcal{L}^1(\mu)$.
Supposons que :
1. $f_n \to f$ presque partout.
2. $\int |f_n| d\mu \to \int |f| d\mu$.
Montrer que $f_n$ converge vers $f$ dans $L^1$, c'est-à-dire $\lim_{n \to \infty} \int |f_n - f| d\mu = 0$.

\textbf{Correction :}
On ne peut pas appliquer le TCD directement car on n'a pas de fonction dominatrice explicite.
1. Considérons la fonction $h_n = |f_n| + |f| - |f_n - f|$.
   Par l'inégalité triangulaire, $|f_n - f| \le |f_n| + |f|$, donc $h_n \ge 0$.
2. Convergence simple : Puisque $f_n \to f$ p.p., $|f_n| \to |f|$ et $|f_n - f| \to 0$ p.p.
   Ainsi, $h_n \to |f| + |f| - 0 = 2|f|$ p.p.
3. On applique le lemme de Fatou à la suite de fonctions positives $h_n$ :
   $\int \liminf h_n d\mu \le \liminf \int h_n d\mu$.
   $\int 2|f| d\mu \le \liminf \int (|f_n| + |f| - |f_n - f|) d\mu$.
4. Par linéarité, le côté droit vaut :
   $\liminf \left( \int |f_n| d\mu + \int |f| d\mu - \int |f_n - f| d\mu \right)$.
   Puisque $\int |f_n| d\mu \to \int |f| d\mu$ par hypothèse, on a :
   $\liminf (\dots) = 2\int |f| d\mu + \liminf \left( - \int |f_n - f| d\mu \right)$.
   $2\int |f| d\mu \le 2\int |f| d\mu - \limsup \int |f_n - f| d\mu$.
5. En soustrayant la quantité finie $2\int |f| d\mu$, on obtient :
   $0 \le - \limsup \int |f_n - f| d\mu$, ce qui implique $\limsup \int |f_n - f| d\mu \le 0$.
   Comme l'intégrale est positive, la limite existe et vaut $0$.
