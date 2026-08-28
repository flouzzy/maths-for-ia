# Exercice 2 : Série entière et intégration ★★★☆☆

**Énoncé :**
On considère l'intégrale $I = \int_0^1 \frac{\ln(x)}{x-1} dx$. Montrer que $I = \sum_{n=1}^\infty \frac{1}{n^2}$ en utilisant un développement en série et le théorème de convergence monotone.

**Correction :**
1. Sur $]0, 1[$, on a $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
2. Donc $\frac{\ln(x)}{x-1} = \frac{-\ln(x)}{1-x} = \sum_{n=0}^\infty (-x^n \ln(x))$.
3. Les fonctions $u_n(x) = -x^n \ln(x)$ sont strictement positives sur $]0, 1[$ et mesurables.
4. Par le corollaire du théorème de convergence monotone pour les séries (Beppo Levi), on peut intervertir la somme et l'intégrale : $\int_0^1 \sum u_n(x) dx = \sum \int_0^1 u_n(x) dx$.
5. Calculons $\int_0^1 -x^n \ln(x) dx$. Par intégration par parties : on pose $u = \ln(x), dv = -x^n dx$, d'où $du = dx/x, v = -x^{n+1}/(n+1)$.
L'intégrale vaut $[-\ln(x) x^{n+1}/(n+1)]_0^1 - \int_0^1 \frac{-x^n}{n+1} dx = 0 + [\frac{x^{n+1}}{(n+1)^2}]_0^1 = \frac{1}{(n+1)^2}$.
6. On obtient donc $\int_0^1 \frac{\ln(x)}{x-1} dx = \sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$.
