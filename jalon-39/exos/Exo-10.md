# Intégrale de Dirichlet (Semi-convergence)

**Difficulté :** $\star\star\star\star\star$

**Énoncé :**
Montrer que l'intégrale de Dirichlet $S = \int_0^{+\infty} \frac{\sin(t)}{t} dt$ est convergente, mais n'est pas absolument convergente. On dit qu'elle est "semi-convergente".

**Correction Zéro Ellipse :**
**Étape 1 : Convergence simple**
1. L'intégrande $f(t) = \frac{\sin(t)}{t}$ est prolongée par continuité en 0 par $f(0)=1$. Le seul vrai problème est en $+\infty$.
2. Considérons l'intégrale partielle sur $[1, X]$ avec $X > 1$. Nous allons procéder à une intégration par parties pour forcer l'apparition d'un terme absolument convergent (principe similaire au critère d'Abel).
   Posons $u'(t) = \sin(t) \implies u(t) = -\cos(t)$ et $v(t) = 1/t \implies v'(t) = -1/t^2$.
   $$ \int_1^X \frac{\sin(t)}{t} dt = \left[ \frac{-\cos(t)}{t} \right]_1^X - \int_1^X (-\cos(t)) \left( \frac{-1}{t^2} \right) dt = \frac{-\cos(X)}{X} + \cos(1) - \int_1^X \frac{\cos(t)}{t^2} dt $$
3. Analysons les limites quand $X \to +\infty$ :
   - Le terme de bord : $\left| \frac{-\cos(X)}{X} \right| \le \frac{1}{X} \to 0$. Donc $\lim_{X \to +\infty} \frac{-\cos(X)}{X} = 0$.
   - L'intégrale résiduelle : nous avons vu dans l'Exo 7 que $\int_1^{+\infty} \frac{\cos(t)}{t^2} dt$ est absolument convergente (donc convergente) car majorée par $1/t^2$.
4. La somme de limites finies est finie. Donc $\lim_{X \to +\infty} \int_1^X \frac{\sin(t)}{t} dt$ existe, ce qui prouve la convergence de $S$.

**Étape 2 : Non absolue convergence**
5. Nous devons montrer que $\int_0^{+\infty} \frac{|\sin(t)|}{t} dt = +\infty$.
   Minifions l'intégrale en la découpant sur des intervalles de longueur $\pi$ : $[k\pi, (k+1)\pi]$.
   $$ I_n = \int_0^{n\pi} \frac{|\sin(t)|}{t} dt = \sum_{k=0}^{n-1} \int_{k\pi}^{(k+1)\pi} \frac{|\sin(t)|}{t} dt $$
6. Sur l'intervalle $[k\pi, (k+1)\pi]$, la variable $t$ vérifie $t \le (k+1)\pi$, donc $\frac{1}{t} \ge \frac{1}{(k+1)\pi}$.
   Par croissance de l'intégrale :
   $$ \int_{k\pi}^{(k+1)\pi} \frac{|\sin(t)|}{t} dt \ge \frac{1}{(k+1)\pi} \int_{k\pi}^{(k+1)\pi} |\sin(t)| dt $$
7. Or, $\int_{k\pi}^{(k+1)\pi} |\sin(t)| dt = \int_0^{\pi} \sin(x) dx = [-\cos(x)]_0^\pi = 2$.
   Donc, chaque terme de la somme est minoré par $\frac{2}{(k+1)\pi}$.
8. En sommant :
   $$ I_n \ge \frac{2}{\pi} \sum_{k=0}^{n-1} \frac{1}{k+1} = \frac{2}{\pi} \sum_{j=1}^n \frac{1}{j} $$
9. On reconnaît la somme partielle de la série harmonique $\sum \frac{1}{j}$, dont on sait qu'elle diverge vers $+\infty$ quand $n \to +\infty$.
   Par le théorème de comparaison, $\lim_{n \to +\infty} I_n = +\infty$. L'intégrale n'est donc pas absolument convergente.
