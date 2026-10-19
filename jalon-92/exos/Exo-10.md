# Exercice 10 : Échec de la LFGN pour la loi de Cauchy

$\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $(X_n)_{n \geq 1}$ une suite de variables I.I.D. suivant une loi de Cauchy de densité $f(x) = \frac{1}{\pi(1+x^2)}$.
Soit $\overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.
On admet que la somme de $n$ variables de Cauchy indépendantes de paramètre 1 donne une loi de Cauchy de paramètre $n$.
1. Déterminer la loi exacte de la moyenne empirique $\overline{X}_n$.
2. En déduire que la LFGN ne s'applique pas. Expliquer mathématiquement pourquoi.

**Correction détaillée :**

1. Notons $S_n = \sum_{i=1}^n X_i$. Par la propriété admise de stabilité de la loi de Cauchy, $S_n$ suit une loi de Cauchy de paramètre $n$. La densité de $S_n$ est $f_{S_n}(x) = \frac{n}{\pi(n^2 + x^2)}$.
   La moyenne empirique est $\overline{X}_n = \frac{S_n}{n}$.
   Cherchons la densité de $\overline{X}_n$. Soit une fonction de test bornée continue $g$ :
   $$ \mathbb{E}[g(\overline{X}_n)] = \mathbb{E}[g(S_n / n)] = \int_{-\infty}^{+\infty} g\left(\frac{x}{n}\right) \frac{n}{\pi(n^2 + x^2)} dx $$
   Procédons au changement de variable $y = x/n$, $dx = n dy$ :
   $$ \mathbb{E}[g(\overline{X}_n)] = \int_{-\infty}^{+\infty} g(y) \frac{n}{\pi(n^2 + (ny)^2)} n dy = \int_{-\infty}^{+\infty} g(y) \frac{n^2}{\pi n^2(1 + y^2)} dy = \int_{-\infty}^{+\infty} g(y) \frac{1}{\pi(1+y^2)} dy $$
   Cela prouve que $\overline{X}_n$ possède la même densité $f(y) = \frac{1}{\pi(1+y^2)}$.
   Autrement dit, $\overline{X}_n$ suit exactement la même loi de Cauchy que $X_1$, pour tout $n$.
2. Puisque la loi de $\overline{X}_n$ est statique et identique à celle de $X_1$, elle ne se "concentre" jamais autour d'une valeur (sa variance reste infinie, elle "zigzague" perpétuellement de la même façon). La suite $(\overline{X}_n)$ ne converge donc pas presque sûrement vers une constante.
   L'explication fondamentale provient du non-respect de l'hypothèse cruciale de la LFGN : la loi de Cauchy n'admet pas d'espérance finie.
   En effet, $\int_{-\infty}^{+\infty} |x| \frac{1}{\pi(1+x^2)} dx = \frac{2}{\pi} \int_0^{+\infty} \frac{x}{1+x^2} dx = \frac{1}{\pi} [\ln(1+x^2)]_0^{+\infty} = +\infty$.
   Comme $\mathbb{E}[|X_1|] = +\infty$, le théorème de Kolmogorov ne s'applique pas.
