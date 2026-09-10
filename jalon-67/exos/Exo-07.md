## Exercice 7 : Intégrabilité d'une série \quad $\bigstar\bigstar\bigstar\bigstar\star$

Soit $f \in L^1([0, 1], \lambda)$. Montrer que la série $\sum_{n=1}^\infty f(x^n)$ converge presque partout sur $[0, 1[$ si $f \ge 0$.
**Question :** Montrer cela en intégrant.

**Solution :**
1. La fonction $f$ étant positive, posons $u_n(x) = f(x^n)$.
2. Par Beppo Levi, l'intégrale de la somme est la somme des intégrales : $\int_0^1 \sum f(x^n) dx = \sum \int_0^1 f(x^n) dx$.
3. Faisons le changement de variable $y = x^n$, $dy = n x^{n-1} dx = n y^{(n-1)/n} dx$, soit $dx = \frac{1}{n} y^{\frac{1}{n}-1} dy$.
4. $\int_0^1 f(x^n) dx = \frac{1}{n} \int_0^1 f(y) y^{\frac{1}{n}-1} dy \le \frac{1}{n} \int_0^1 f(y) y^{-1/2} dy$ pour $n \ge 2$.
5. Si $f$ est intégrable par rapport à la mesure de densité $y^{-1/2}$, la série des intégrales converge.
6. Si l'intégrale de la somme est finie, la somme doit être finie presque partout. $\blacksquare$
