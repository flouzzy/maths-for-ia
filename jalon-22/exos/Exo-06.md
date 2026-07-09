# Exercice 6 : Dérivation terme à terme

**Difficulté :** $\star\star\star\star$

**Énoncé :**
Soit $f(x) = \sum_{n=1}^\infty \frac{\sin(nx)}{n^3}$. Montrer que $f$ est de classe $\mathcal{C}^1$ sur $\mathbb{R}$, et exprimer sa dérivée.

**Démonstration :**
1. Soit $u_n(x) = \frac{\sin(nx)}{n^3}$. Les $u_n$ sont de classe $\mathcal{C}^1$ sur $\mathbb{R}$.
   Leur dérivée est $u_n'(x) = \frac{n \cos(nx)}{n^3} = \frac{\cos(nx)}{n^2}$.
2. **Convergence de la série des dérivées :**
   Étudions la série $\sum u_n'(x)$.
   $$ \|u_n'\|_{\infty, \mathbb{R}} = \sup_{x \in \mathbb{R}} \left| \frac{\cos(nx)}{n^2} \right| = \frac{1}{n^2} $$
   La série $\sum \frac{1}{n^2}$ est une série de Riemann convergente ($\alpha=2$).
   Donc la série des dérivées $\sum u_n'$ converge normalement, et donc uniformément, sur $\mathbb{R}$.
3. **Convergence de la série originelle en au moins un point :**
   Pour $x=0$, $u_n(0) = 0$, donc la série $\sum u_n(0) = 0$ converge.
4. **Application du théorème :**
   Les trois hypothèses du théorème de dérivation terme à terme étant vérifiées (les fonctions sont $\mathcal{C}^1$, la série des dérivées converge uniformément, et la série converge en un point), on déduit que :
   - La série $\sum u_n$ converge uniformément sur $\mathbb{R}$.
   - La fonction somme $f$ est de classe $\mathcal{C}^1$ sur $\mathbb{R}$.
   - Et pour tout $x \in \mathbb{R}$, $f'(x) = \sum_{n=1}^\infty u_n'(x) = \sum_{n=1}^\infty \frac{\cos(nx)}{n^2}$.
$\blacksquare$
