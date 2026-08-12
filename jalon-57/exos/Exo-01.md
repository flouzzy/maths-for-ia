# Exercice 1 : Application directe : Extraction de racine carrée par la méthode de Héron
**Niveau :** $\bigstar\star\star\star\star$

**Énoncé :**
Soit $a > 0$ un réel fixé. On considère l'application $f : [ \sqrt{a}, +\infty[ \to \mathbb{R}$ définie par $f(x) = \frac{1}{2} \left( x + \frac{a}{x} \right)$.
1. Montrer que l'intervalle $I = [ \sqrt{a}, +\infty[$ est stable par $f$, c'est-à-dire que $f(I) \subset I$.
2. Montrer que $f$ est contractante sur l'intervalle fermé $I_M = [\sqrt{a}, M]$ pour tout $M > \sqrt{a}$. Quel est le rapport de contraction sur cet intervalle ?
3. En déduire la convergence de la suite définie par $x_0 > \sqrt{a}$ et $x_{n+1} = f(x_n)$ vers $\sqrt{a}$.

**Démonstration pas à pas :**
1. La fonction $f$ est dérivable sur $]0, +\infty[$ et $f'(x) = \frac{1}{2} \left( 1 - \frac{a}{x^2} \right)$.
   Pour $x \geq \sqrt{a}$, $x^2 \geq a$, donc $\frac{a}{x^2} \leq 1$. Par conséquent, $f'(x) \geq 0$ pour tout $x \geq \sqrt{a}$.
   La fonction $f$ est donc croissante sur $I$.
   Puisque $f(\sqrt{a}) = \frac{1}{2} \left( \sqrt{a} + \frac{a}{\sqrt{a}} \right) = \frac{1}{2} (\sqrt{a} + \sqrt{a}) = \sqrt{a}$, et que $f$ est croissante, pour tout $x \in I$, $f(x) \geq f(\sqrt{a}) = \sqrt{a}$.
   Ainsi, $f(I) \subset [\sqrt{a}, +\infty[ = I$. L'intervalle est bien stable.

2. Restreignons $f$ à un sous-intervalle fermé borné $I_M = [\sqrt{a}, M]$.
   On a vu que $f'(x) = \frac{1}{2} \left( 1 - \frac{a}{x^2} \right)$.
   Sur $I_M$, $f'$ est croissante (car la dérivée seconde $f''(x) = \frac{a}{x^3} > 0$), et prend ses valeurs entre $f'(\sqrt{a}) = 0$ et $f'(M) = \frac{1}{2} \left( 1 - \frac{a}{M^2} \right)$.
   Ainsi, pour tout $x \in I_M$, $0 \leq f'(x) \leq k_M$ où $k_M = \frac{1}{2} \left( 1 - \frac{a}{M^2} \right) < \frac{1}{2} < 1$.
   Par l'inégalité des accroissements finis, pour tous $x, y \in I_M$, $|f(x) - f(y)| \leq k_M |x - y|$.
   La fonction $f$ est strictement contractante sur $I_M$.

3. L'intervalle $I_M$ est un fermé de $\mathbb{R}$ (donc complet). L'application $f : I_M \to I$ n'est pas tout à fait à image dans $I_M$, mais il est aisé de voir que si $x_0 \in I$, alors $x_{n+1} \le x_n$, donc la suite reste dans $[\sqrt{a}, x_0]$. Sur cet intervalle fermé et complet, $f$ est une contraction stricte de rapport $k_{x_0} < 1/2$. Par le théorème du point fixe de Banach, $f$ admet un unique point fixe dans cet intervalle, qui est $\sqrt{a}$, et la suite $(x_n)$ converge vers cette valeur géométriquement.
