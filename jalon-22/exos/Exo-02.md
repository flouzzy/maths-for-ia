# Exercice 2 : Étude sur des segments

**Difficulté :** $\star\star$

**Énoncé :**
Soit $f_n(x) = x^n(1-x)$. Étudier la convergence de $\sum f_n$ sur $[0, a]$ avec $0 < a < 1$, puis sur $[0, 1]$.

**Démonstration :**
1. **Convergence simple sur $[0, 1]$ :**
   - Si $x=1$, $f_n(1) = 0$, donc la série converge vers 0.
   - Si $x \in [0, 1[$, $f_n(x) = x^n(1-x)$. Comme $x \in [0, 1[$, la série géométrique $\sum x^n$ converge, donc $\sum x^n(1-x)$ converge. En fait, la somme des $N$ premiers termes est une série télescopique :
     $$ S_N(x) = \sum_{n=0}^N (x^n - x^{n+1}) = 1 - x^{N+1} $$
     Si $x \in [0, 1[$, $\lim_{N \to \infty} S_N(x) = 1$.
   La série converge simplement sur $[0, 1]$ vers la fonction $S$ telle que $S(x)=1$ sur $[0, 1[$ et $S(1)=0$.

2. **Convergence sur $[0, a]$ ($0 < a < 1$) :**
   Calculons la norme infinie de $f_n$ sur $[0, a]$.
   La fonction $f_n(x) = x^n - x^{n+1}$ a pour dérivée $f'_n(x) = nx^{n-1} - (n+1)x^n = x^{n-1}(n - (n+1)x)$.
   Le maximum est atteint en $x_n = \frac{n}{n+1}$.
   Pour $n$ assez grand, $x_n > a$. Donc sur $[0, a]$, $f_n$ est strictement croissante, et son supremum est $f_n(a) = a^n(1-a)$.
   $$ \|f_n\|_{\infty, [0,a]} = a^n(1-a) $$
   La série géométrique $\sum a^n$ converge puisque $0 < a < 1$.
   Donc $\sum \|f_n\|_{\infty, [0,a]}$ converge. La série converge normalement (et donc uniformément) sur $[0, a]$.

3. **Convergence uniforme sur $[0, 1]$ :**
   La fonction limite $S$ est discontinue en 1. Or, les fonctions $f_n$ sont des polynômes, donc continues sur $[0, 1]$.
   Si la série convergeait uniformément sur $[0, 1]$, le théorème de continuité de la limite garantirait que $S$ soit continue.
   Comme $S$ n'est pas continue, la série **ne converge pas uniformément** sur $[0, 1]$.
$\blacksquare$
