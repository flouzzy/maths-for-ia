##{Exercice 7 : Série de fonctions et interversion \quad $\bigstar\bigstar\bigstar\star\star$}

\textbf{Énoncé :}
Montrer que $\int_0^1 \frac{x \ln(x)}{1-x} dx = -\sum_{n=1}^{\infty} \frac{1}{(n+1)^2}$.

\textbf{Correction :}
1. Pour $x \in ]0, 1[$, on peut développer $\frac{1}{1-x}$ en série géométrique : $\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n$.
2. L'intégrande devient $\sum_{n=0}^{\infty} x^{n+1} \ln(x)$. Les termes sont tous du même signe (négatif). On peut appliquer le Théorème de Convergence Monotone ou intégrer $-x^{n+1}\ln(x)$ qui est positif.
On peut aussi utiliser le TCD sur les sommes partielles. Les fonctions sont de signe constant, donc le théorème d'intégration terme à terme s'applique (équivalent au TCM).
3. Calculons $\int_0^1 x^{n+1} \ln(x) dx$ par intégration par parties :
   $u(x) = \ln(x)$, $v'(x) = x^{n+1} \implies u'(x) = 1/x$, $v(x) = \frac{x^{n+2}}{n+2}$.
   $\int_0^1 x^{n+1} \ln(x) dx = \left[ \frac{x^{n+2}}{n+2} \ln(x) \right]_0^1 - \int_0^1 \frac{x^{n+1}}{n+2} dx = 0 - \frac{1}{(n+2)^2}$.
4. On a donc $\int_0^1 \frac{x \ln(x)}{1-x} dx = \sum_{n=0}^{\infty} \frac{-1}{(n+2)^2} = -\sum_{k=2}^{\infty} \frac{1}{k^2}$.
Si l'énoncé demande à partir de $n=1$, c'est avec $k=n+1$ donc $-\sum_{n=1}^{\infty} \frac{1}{(n+1)^2}$.
