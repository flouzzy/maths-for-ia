# Exercice 10 : Densité et fonctions non-L1 dans L2
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

On pose $f(x) = \frac{x}{1+x^2}$.
1. Justifier que $f \in L^2(\mathbb{R})$ mais $f \notin L^1(\mathbb{R})$.
2. Proposer une méthode analytique basée sur la dérivation et l'inversion de Fourier pour calculer sa transformée de Fourier dans $L^2$, sachant que $\mathcal{F}(e^{-|x|}) = \frac{2}{1+\xi^2}$.

**Correction :**
1. Au voisinage de l'infini, $f(x) \sim \frac{1}{x}$. $\int_1^\infty \frac{1}{x} dx = \infty$ donc $f \notin L^1$.
Mais $f(x)^2 \sim \frac{1}{x^2}$. $\int_1^\infty \frac{1}{x^2} dx < \infty$ et $f$ est continue, donc $f \in L^2$.
2. Nous voulons trouver $\hat{f}(\xi)$.
On sait que si $g(x) = e^{-|x|}$, alors $\hat{g}(\xi) = \frac{2}{1+\xi^2}$.
Donc $\frac{x}{1+x^2} = \frac{x}{2} \hat{g}(x)$.
Par la propriété de dualité/inversion, multiplier la transformée par la variable équivaut à dériver le signal temporel.
Plus précisément, si $h(x) = x \hat{g}(x)$, par la transformée inverse, $h$ est liée à la dérivée de $g$.
On sait que $g'(t) = -\text{sgn}(t) e^{-|t|}$ (presque partout).
Par les propriétés de Fourier, $\mathcal{F}(tg(t)) = i \frac{d}{d\xi}\hat{g}(\xi)$.
La fonction cherchée est la transformée inverse de $-i \pi \text{sgn}(\xi) e^{-|\xi|}$.
En manipulant rigoureusement ces distributions tempérées au sens $L^2$, on montre que $\hat{f}(\xi) = -i \pi \text{sgn}(\xi) e^{-|\xi|}$.
L'intégrale classique oscille et diverge au sens usuel, mais au sens limite hilbertien (Plancherel), cette forme est l'unique limite $L^2$.
