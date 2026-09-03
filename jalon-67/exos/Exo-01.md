# Exercice 1 : Application directe du Corollaire (Série harmonique alternée modifiée)
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Calculer l'intégrale $\int_0^1 \sum_{n=1}^{+\infty} (x^{2n} - x^{2n+1}) dx$. Discuter de l'application de Beppo-Levi.

## Correction Détaillée

Posons $u_n(x) = x^{2n} - x^{2n+1} = x^{2n}(1 - x)$.
Sur l'intervalle $[0, 1]$, on a $x \in [0,1]$, donc $1-x \geq 0$ et $x^{2n} \geq 0$. Ainsi, pour tout $n$, $u_n$ est une fonction mesurable et positive.
Le corollaire du théorème de Beppo-Levi pour les séries positives s'applique directement :
$$\int_0^1 \sum_{n=1}^{+\infty} u_n(x) dx = \sum_{n=1}^{+\infty} \int_0^1 (x^{2n} - x^{2n+1}) dx$$
Calculons l'intégrale :
$$\int_0^1 (x^{2n} - x^{2n+1}) dx = \left[ \frac{x^{2n+1}}{2n+1} - \frac{x^{2n+2}}{2n+2} \right]_0^1 = \frac{1}{2n+1} - \frac{1}{2n+2} = \frac{1}{(2n+1)(2n+2)}$$
Donc,
$$\int_0^1 \sum_{n=1}^{+\infty} u_n(x) dx = \sum_{n=1}^{+\infty} \left( \frac{1}{2n+1} - \frac{1}{2n+2} \right)$$
La somme des termes se télescope ou peut être reconnue via la série de Taylor de $\ln(1+x)$ en $x=1$ :
$\sum_{k=1}^{+\infty} \frac{(-1)^{k+1}}{k} = \ln(2)$.
Ici on a la somme pour $k \geq 3$ (en groupant termes impairs et pairs). La valeur exacte est $\ln(2) - (1 - 1/2) = \ln(2) - 1/2$.
