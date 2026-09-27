# Exo 09 : Analyse de convergence

**Difficulté :** \bigstar\bigstar\bigstar\bigstar\bigstar


Soit $f \in C^1_{per}$. On rappelle que $c_n(f') = in c_n(f)$.
En appliquant l'inégalité de Cauchy-Schwarz, montrer que la série de Fourier de $f$ est normalement convergente sur $\mathbb{R}$.

## Correction

Puisque $f \in C^1_{per}$, sa dérivée $f'$ est dans $L^2_{per}(0, 2\pi)$ (elle est continue donc intégrable en carré sur une période compacte).
Par l'inégalité de Bessel (ou l'identité de Parseval), la série des modules au carré des coefficients de Fourier de $f'$ converge :
$$ \sum_{n=-\infty}^{+\infty} |c_n(f')|^2 \le \frac{1}{2\pi} \int_0^{2\pi} |f'(t)|^2 dt < +\infty $$

On utilise la relation prouvée précédemment : $c_n(f') = in c_n(f)$.
Pour $n \neq 0$, on peut écrire $|c_n(f)| = \frac{|c_n(f')|}{|n|}$.

Pour démontrer la convergence normale de la série de Fourier, on doit prouver que la série numérique $\sum |c_n(f)|$ converge.
Nous allons utiliser l'inégalité de Cauchy-Schwarz pour les sommes finies :
$$ \sum_{n=1}^N a_n b_n \le \left( \sum_{n=1}^N a_n^2 \right)^{1/2} \left( \sum_{n=1}^N b_n^2 \right)^{1/2} $$

Appliquons-la en posant $a_n = |c_n(f')|$ et $b_n = \frac{1}{n}$ pour $n \ge 1$ :
$$ \sum_{n=1}^N |c_n(f)| = \sum_{n=1}^N |c_n(f')| \frac{1}{n} \le \left( \sum_{n=1}^N |c_n(f')|^2 \right)^{1/2} \left( \sum_{n=1}^N \frac{1}{n^2} \right)^{1/2} $$

Lorsque $N \to +\infty$ :
- $\sum_{n=1}^{+\infty} |c_n(f')|^2$ converge d'après Bessel pour la fonction $f'$.
- $\sum_{n=1}^{+\infty} \frac{1}{n^2}$ est la série de Riemann (convergente, valant $\pi^2/6$).

Les deux termes du membre de droite sont finis, donc la somme partielle $\sum_{n=1}^N |c_n(f)|$ est majorée par une constante indépendante de $N$. Puisque ses termes sont positifs, la série $\sum_{n=1}^{+\infty} |c_n(f)|$ converge.
Par symétrie, la série $\sum_{n=-\infty}^{-1} |c_n(f)|$ converge aussi.

Le terme général de la série de Fourier en valeur absolue s'écrit :
$$ |c_n(f) e^{int}| = |c_n(f)| |e^{int}| = |c_n(f)| $$
Puisque la série des normes infinies $\sum \|c_n(f) e^{int}\|_{\infty} = \sum |c_n(f)|$ converge, la série de Fourier converge normalement sur $\mathbb{R}$. La convergence normale impliquant la convergence uniforme, cela garantit une excellente régularité de l'approximation.
