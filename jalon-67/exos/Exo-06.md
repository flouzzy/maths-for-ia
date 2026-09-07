# Exercice 6 : Série paramétrée et continuité

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit la fonction $F(t) = \sum_{n=1}^\infty \int_0^t \frac{x^{n-1}}{1+x^n} dx$.
Justifier l'interversion pour $t \in ]0, 1[$, et calculer $F(t)$.

**Solution Détaillée :**
1. Pour $t \in ]0, 1[$, nous intégrons sur l'intervalle $[0, t]$. Soit la suite de fonctions $u_n(x) = \frac{x^{n-1}}{1+x^n}$.
2. Sur $[0, 1[$, $x \ge 0$, donc toutes les fonctions $u_n(x)$ sont positives.
3. Par le corollaire du TCM pour l'intégration terme à terme, on a :
$$F(t) = \int_0^t \left( \sum_{n=1}^\infty \frac{x^{n-1}}{1+x^n} \right) dx = \sum_{n=1}^\infty \int_0^t \frac{x^{n-1}}{1+x^n} dx$$
4. Calculons l'intégrale interne :
$$\int_0^t \frac{x^{n-1}}{1+x^n} dx = \left[ \frac{1}{n} \ln(1+x^n) \right]_0^t = \frac{\ln(1+t^n)}{n}$$
5. La fonction $F(t)$ est donc bien définie et vaut la série :
$$F(t) = \sum_{n=1}^\infty \frac{\ln(1+t^n)}{n}$$
L'application rigoureuse du TCM nous a permis d'évaluer une intégrale de série pour la réduire à l'étude d'une série de nombres réels (qui converge pour $t<1$ par équivalence avec $t^n/n$).
