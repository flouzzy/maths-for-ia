# Critère de majoration

**Difficulté :** $\star\star\star$

**Énoncé :**
Montrer que l'intégrale suivante est convergente :
$$ L = \int_2^{+\infty} \frac{\sin^2(t)}{t^3} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** Soit $f(t) = \frac{\sin^2(t)}{t^3}$. La fonction $f$ est continue sur $[2, +\infty[$. De plus, comme un carré est toujours positif et $t \ge 2 > 0$, la fonction $f$ est positive sur son domaine d'intégration.
2. **Majoration :** Pour appliquer le théorème de majoration pour des fonctions positives, nous devons trouver une fonction $g(t)$ plus grande que $f(t)$ dont l'intégrale converge.
   Nous savons de manière universelle que pour tout $t \in \mathbb{R}$, $-1 \le \sin(t) \le 1$, ce qui implique que :
   $$ 0 \le \sin^2(t) \le 1 $$
   Comme $t^3 > 0$ sur $[2, +\infty[$, nous pouvons diviser l'inégalité sans en changer le sens :
   $$ 0 \le \frac{\sin^2(t)}{t^3} \le \frac{1}{t^3} $$
   Posons $g(t) = \frac{1}{t^3}$.
3. **Analyse du majorant :** L'intégrale $\int_2^{+\infty} g(t) dt = \int_2^{+\infty} \frac{1}{t^3} dt$ est une intégrale de Riemann. Ici, $\alpha = 3$.
   Comme $\alpha > 1$, cette intégrale de Riemann est convergente.
4. **Conclusion :** D'après le critère de comparaison (ou majoration) pour les intégrales de fonctions positives :
   Si $0 \le f(t) \le g(t)$ pour tout $t \ge a$ et si $\int_a^{+\infty} g(t) dt$ converge, alors $\int_a^{+\infty} f(t) dt$ converge.
   Par conséquent, l'intégrale $L$ est convergente.
