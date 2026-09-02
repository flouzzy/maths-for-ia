# Exo 08 : Un calcul difficile avec Beppo Levi ($\bigstar$\bigstar$\bigstar$\bigstar\star$)

## Énoncé
Montrer que :
$$ \int_0^1 \frac{\ln(x)}{x-1} \, dx = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} $$

## Correction Détaillée
**Étape 1 : Développement en série de la fonction**
Soit $f(x) = \frac{\ln(x)}{x-1}$ sur $]0, 1[$. Remarquons que pour $x \in ]0, 1[$, $x-1 < 0$ et $\ln(x) < 0$. Donc $f(x) > 0$.
On a $\frac{1}{1-x} = \sum_{n=0}^\infty x^n$.
Ainsi, $\frac{1}{x-1} = -\sum_{n=0}^\infty x^n$.
D'où : $f(x) = \ln(x) \times \left( -\sum_{n=0}^\infty x^n \right) = \sum_{n=0}^\infty (-\ln(x)) x^n$.

**Étape 2 : Positivité et Théorème de sommation**
Posons $u_n(x) = -x^n \ln(x)$. Pour $x \in ]0, 1[$, $u_n(x) > 0$.
Par le théorème d'intégration terme à terme des séries positives (corollaire direct du Théorème de Convergence Monotone) :
$$ \int_0^1 \left( \sum_{n=0}^\infty -x^n \ln(x) \right) dx = \sum_{n=0}^\infty \int_0^1 -x^n \ln(x) \, dx $$

**Étape 3 : Calcul de l'intégrale du terme général**
Nous devons calculer $I_n = -\int_0^1 x^n \ln(x) \, dx$.
On effectue une intégration par parties. Soit $u = \ln(x)$ d'où $du = \frac{1}{x} dx$, et $dv = x^n dx$ d'où $v = \frac{x^{n+1}}{n+1}$.
$$ \int x^n \ln(x) \, dx = \left[ \frac{x^{n+1}}{n+1} \ln(x) \right]_0^1 - \int \frac{x^{n+1}}{n+1} \frac{1}{x} \, dx $$
Le terme de bord en 1 vaut $0$ (car $\ln(1)=0$). Le terme de bord en 0 donne $\lim_{x \to 0} x^{n+1} \ln(x) = 0$ par croissance comparée.
Il reste :
$$ -\int_0^1 x^n \ln(x) \, dx = \int_0^1 \frac{x^n}{n+1} \, dx = \left[ \frac{x^{n+1}}{(n+1)^2} \right]_0^1 = \frac{1}{(n+1)^2} $$

**Étape 4 : Conclusion**
En sommant ces résultats :
$$ \int_0^1 \frac{\ln(x)}{x-1} \, dx = \sum_{n=0}^\infty \frac{1}{(n+1)^2} = \sum_{k=1}^\infty \frac{1}{k^2} $$
On reconnaît le problème de Bâle, dont la somme vaut $\frac{\pi^2}{6}$.
