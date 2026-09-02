# Exo 06 : Limite supérieure et croissance ($\bigstar$\bigstar$\bigstar\star\star$)

## Énoncé
Soit $f \in L^1(\mathbb{R}, \lambda)$ une fonction positive intégrable.
On définit la suite $f_n(x) = \min(f(x), n)$.
1. Prouver que la suite $(f_n)$ converge en croissant vers $f$.
2. En déduire que $\lim_{n \to \infty} \int_{\mathbb{R}} \min(f(x), n) \, dx = \int_{\mathbb{R}} f(x) \, dx$.
3. Cette propriété reste-t-elle vraie si on lève l'hypothèse $f \in L^1$ ?

## Correction Détaillée
**Étape 1 : Convergence monotone de la suite $(f_n)$**
Pour tout $x \in \mathbb{R}$, $f_n(x) = \min(f(x), n) \ge 0$ car $f$ est positive.
De plus, $\min(f(x), n) \le \min(f(x), n+1)$ car $n < n+1$. La suite $(f_n)$ est donc bien croissante ponctuellement.
Si $f(x)$ est fini, il existe un rang $N$ tel que pour tout $n \ge N$, $n \ge f(x)$. À partir de ce rang $N$, $\min(f(x), n) = f(x)$.
La suite stationne vers $f(x)$, donc $\lim_{n \to \infty} f_n(x) = f(x)$. Si $f(x) = +\infty$, $\min(f(x), n) = n \to +\infty$.
La limite est donc $f$ presque partout.

**Étape 2 : Évaluation des intégrales**
Les $f_n$ sont mesurables (car composition par le minimum qui est lipschitzien), positives et croissantes vers $f$.
Le théorème de convergence monotone s'applique directement :
$$ \lim_{n \to \infty} \int_{\mathbb{R}} \min(f(x), n) \, dx = \int_{\mathbb{R}} f(x) \, dx $$

**Étape 3 : Hypothèse sur $f$**
Le théorème de Beppo Levi ne requiert absolument pas que $f$ soit intégrable ($f \in L^1$). Il fonctionne à valeurs dans $[0, +\infty]$.
Si l'intégrale de $f$ est infinie, la limite des intégrales des $f_n$ sera également $+\infty$. L'égalité reste strictement vraie dans $[0, +\infty]$. L'hypothèse $f \in L^1$ dans l'énoncé n'était qu'une restriction psychologique.
