# Exercice 3 : Série impliquant le logarithme
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

En développant la fonction sous l'intégrale en série entière, calculer $\int_0^1 \frac{-\ln(x)}{1-x} dx$.

## Correction Détaillée

On sait que pour $x \in ]0, 1[$, on a le développement géométrique :
$\frac{1}{1-x} = \sum_{n=0}^{+\infty} x^n$.
Ainsi, la fonction à intégrer est $f(x) = \sum_{n=0}^{+\infty} -x^n \ln(x)$.
Posons $u_n(x) = -x^n \ln(x)$. Sur $]0, 1[$, $\ln(x) < 0$, donc $u_n(x) \geq 0$. Les fonctions $u_n$ sont mesurables et positives.
Le corollaire du Théorème de Beppo-Levi justifie l'interversion série-intégrale :
$$\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=0}^{+\infty} \int_0^1 -x^n \ln(x) dx$$
Calculons l'intégrale par intégration par parties. Posons $u' = x^n \implies u = \frac{x^{n+1}}{n+1}$ et $v = -\ln(x) \implies v' = -\frac{1}{x}$.
$$\int_0^1 -x^n \ln(x) dx = \left[ -\frac{x^{n+1}}{n+1} \ln(x) \right]_{x \to 0}^1 - \int_0^1 \frac{x^{n+1}}{n+1} \left(-\frac{1}{x}\right) dx$$
Le terme tout intégré s'annule (car $x^{n+1} \ln(x) \to 0$ en $0$).
Il reste :
$$\int_0^1 \frac{x^n}{n+1} dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2}$$
On somme cette expression :
$$\int_0^1 \frac{-\ln(x)}{1-x} dx = \sum_{n=0}^{+\infty} \frac{1}{(n+1)^2} = \sum_{k=1}^{+\infty} \frac{1}{k^2} = \frac{\pi^2}{6}$$
