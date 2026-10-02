# Exercice 4 : Évaluation d'intégrales par Plancherel
**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Calculer l'intégrale $I = \int_{-\infty}^\infty \frac{\sin^2(t)}{t^2} dt$ en utilisant le théorème de Plancherel sur une fonction bien choisie.

**Correction :**
Considérons la fonction porte $f(t) = \mathbf{1}_{[-1, 1]}(t)$.
Son énergie temporelle est $\|f\|_2^2 = \int_{-1}^1 1 dt = 2$.
Sa transformée de Fourier est $\hat{f}(\xi) = 2\frac{\sin(\xi)}{\xi} = 2\text{sinc}(\xi)$.
D'après Plancherel, $\|\hat{f}\|_2^2 = 2\pi \|f\|_2^2$.
Donc $\int_{-\infty}^\infty 4 \frac{\sin^2(\xi)}{\xi^2} d\xi = 2\pi \cdot 2 = 4\pi$.
En divisant par 4 de chaque côté et en renommant la variable muette $\xi$ en $t$, on obtient :
$\int_{-\infty}^\infty \frac{\sin^2(t)}{t^2} dt = \pi$.
