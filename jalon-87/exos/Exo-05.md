# Exercice 5 : La non-intégrabilité de la loi de Cauchy

**Difficulté :** $\bigstarigstarigstar\star\star$

Soit $X$ une variable aléatoire suivant la loi de Cauchy standard, dont la densité sur $\mathbb{R}$ est :
$$ f(x) = \frac{1}{\pi(1+x^2)} $$
Démontrer rigoureusement que $X$ n'admet pas d'espérance, c'est-à-dire que $X \notin \mathcal{L}^1$.

### Correction détaillée

Pour qu'une variable aléatoire $X$ admette une espérance, il est nécessaire et suffisant que son espérance absolue soit finie :
$$ \mathbb{E}[|X|] = \int_{-\infty}^{+\infty} |x| f(x) \, \mathrm{d}x < +\infty $$

1. Écrivons l'intégrale pour la loi de Cauchy :
   $$ \mathbb{E}[|X|] = \int_{-\infty}^{+\infty} \frac{|x|}{\pi(1+x^2)} \, \mathrm{d}x $$
2. Par parité de la fonction $x \mapsto \frac{|x|}{1+x^2}$, l'intégrale sur $\mathbb{R}$ est égale à deux fois l'intégrale sur $\mathbb{R}^+$ :
   $$ \mathbb{E}[|X|] = \frac{2}{\pi} \int_{0}^{+\infty} \frac{x}{1+x^2} \, \mathrm{d}x $$
3. Calculons cette intégrale impropre. Pour tout $A > 0$ :
   $$ \int_{0}^{A} \frac{x}{1+x^2} \, \mathrm{d}x $$
   On reconnaît une dérivée de la forme $\frac{u'}{u}$ au facteur 2 près. En posant $u = 1+x^2$, $\mathrm{d}u = 2x \, \mathrm{d}x$ :
   $$ \int_{0}^{A} \frac{1}{2} \frac{2x}{1+x^2} \, \mathrm{d}x = \frac{1}{2} \left[ \ln(1+x^2) \right]_0^A = \frac{1}{2} \ln(1+A^2) - 0 $$
4. On passe à la limite lorsque $A \to +\infty$ :
   $$ \lim_{A \to +\infty} \frac{1}{2} \ln(1+A^2) = +\infty $$
5. L'intégrale diverge vers l'infini. Par conséquent, $\mathbb{E}[|X|] = +\infty$.

La variable aléatoire $X$ n'est pas intégrable, elle n'appartient pas à $\mathcal{L}^1(\Omega, \mathcal{F}, \mathbb{P})$. Elle n'a donc pas d'espérance mathématique (la moyenne est indéfinie à cause des probabilités trop importantes accordées aux valeurs extrêmes).
