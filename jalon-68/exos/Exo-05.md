## Exercice 5 : Lemme de Fatou inverse pour des fonctions majorées \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $(f_n)$ une suite de fonctions mesurables telles que $f_n \le g$ pour tout $n$, où $g$ est une fonction intégrable ($g \in \mathcal{L}^1(\mu)$).
Montrer que $\limsup_{n \to \infty} \int f_n d\mu \le \int \limsup_{n \to \infty} f_n d\mu$.

**Correction :**
1. On pose $h_n = g - f_n$. Comme $f_n \le g$, $h_n \ge 0$. Les $h_n$ sont mesurables et positives.
2. On applique le lemme de Fatou classique à la suite $(h_n)$ :
   $\int \liminf_{n \to \infty} (g - f_n) d\mu \le \liminf_{n \to \infty} \int (g - f_n) d\mu$.
3. On utilise les propriétés des limites inférieures et supérieures :
   $\liminf (-f_n) = - \limsup f_n$ et $\liminf \int (-f_n) d\mu = - \limsup \int f_n d\mu$.
4. En remplaçant :
   $\int (g - \limsup f_n) d\mu \le \int g d\mu - \limsup \int f_n d\mu$.
5. Comme $g$ est intégrable, on peut soustraire $\int g d\mu$ (qui est fini) des deux côtés :
   $-\int \limsup f_n d\mu \le - \limsup \int f_n d\mu$.
6. En multipliant par -1 (et en changeant le sens de l'inégalité) :
   $\limsup \int f_n d\mu \le \int \limsup f_n d\mu$.
