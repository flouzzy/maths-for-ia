## Exercice 6 : Contre-exemple sans positivité \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $f_n(x) = - \frac{1}{n} \mathbf{1}_{[0, n]}(x)$ sur $[0, +\infty[$.
**Question :** Montrer que la suite $(f_n)$ est croissante vers $0$. Le théorème de Beppo Levi s'applique-t-il ? Que vaut l'intégrale ?

**Solution :**
1. Pour tout $x \ge 0$, soit $f_n(x) = -1/n$, et $f_{n+1}(x) = -1/(n+1)$ ou $0$. Dans tous les cas, $f_{n+1}(x) \ge f_n(x)$. La suite est croissante.
2. Sa limite ponctuelle est $f \equiv 0$.
3. Cependant, les fonctions ne sont pas positives, $f_n \le 0$.
4. $\int_0^\infty f_n dx = - \frac{1}{n} \times n = -1$.
5. La limite des intégrales est $-1$, mais l'intégrale de la limite est $0$.
6. Beppo Levi tombe en défaut si on omet l'hypothèse de positivité ou si les fonctions ne sont pas minorées par une fonction intégrable. $\blacksquare$
