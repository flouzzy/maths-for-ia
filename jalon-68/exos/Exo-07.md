# Exercice 7 : L'intégrale de Dirichlet et l'intégrabilité de Lebesgue
$\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé
On s'intéresse à la fonction $f(x) = \frac{\sin x}{x}$ sur l'intervalle $[0, +\infty[$.
1. Montrer que l'intégrale généralisée de Riemann $\int_0^{+\infty} \frac{\sin x}{x} dx$ est convergente.
2. Montrer que $f$ **n'est pas** intégrable au sens de Lebesgue sur $[0, +\infty[$ muni de la mesure $\lambda$.
Conclusion sur le lien Riemann/Lebesgue sur les intervalles non bornés.

## Correction
**1. Convergence au sens de Riemann (Intégrale impropre) :**
$f$ est prolongeable par continuité en $0$ (vaut $1$), le seul problème est en $+\infty$.
On intègre par parties sur $[1, M]$ :
$\int_1^M \frac{\sin x}{x} dx = \left[ -\frac{\cos x}{x} \right]_1^M - \int_1^M \frac{\cos x}{x^2} dx = -\frac{\cos M}{M} + \cos(1) - \int_1^M \frac{\cos x}{x^2} dx$.
- Le terme de bord $-\frac{\cos M}{M}$ tend vers $0$ quand $M \to \infty$.
- L'intégrale $\int_1^\infty \frac{\cos x}{x^2} dx$ est absolument convergente car $\left| \frac{\cos x}{x^2} \right| \leq \frac{1}{x^2}$, qui est de Riemann convergente ($2 > 1$).
Ainsi, la limite quand $M \to \infty$ existe, l'intégrale impropre de Riemann converge.

**2. Non-intégrabilité de Lebesgue :**
Pour qu'une fonction soit Lebesgue-intégrable, il faut et il suffit que $\int |f| d\lambda < \infty$.
Évaluons $\int_0^\infty \left| \frac{\sin x}{x} \right| dx$.
On décompose l'intégrale sur les intervalles $I_k = [k\pi, (k+1)\pi]$ pour $k \in \mathbb{N}$.
Sur $I_k$, $| \sin x | = (-1)^k \sin x$.
Et sur $I_k$, $x \leq (k+1)\pi$, donc $\frac{1}{x} \geq \frac{1}{(k+1)\pi}$.
Ainsi :
$$\int_{k\pi}^{(k+1)\pi} \left| \frac{\sin x}{x} \right| dx \geq \int_{k\pi}^{(k+1)\pi} \frac{|\sin x|}{(k+1)\pi} dx = \frac{1}{(k+1)\pi} \int_{k\pi}^{(k+1)\pi} |\sin x| dx$$
Par périodicité de $|\sin x|$, $\int_{k\pi}^{(k+1)\pi} |\sin x| dx = \int_0^\pi \sin x dx = \left[ -\cos x \right]_0^\pi = 2$.
Donc, l'intégrale sur $I_k$ est minorée par $\frac{2}{(k+1)\pi}$.

L'intégrale sur $[0, \infty[$ est la somme des intégrales sur les $I_k$ (par le théorème de convergence monotone, car on intègre une fonction positive) :
$$\int_0^\infty \left| \frac{\sin x}{x} \right| dx = \sum_{k=0}^\infty \int_{I_k} \left| \frac{\sin x}{x} \right| dx \geq \sum_{k=0}^\infty \frac{2}{(k+1)\pi}$$
La série harmonique $\sum \frac{1}{k+1}$ diverge vers l'infini.
Par conséquent, $\int_0^\infty \left| \frac{\sin x}{x} \right| dx = +\infty$.

**Conclusion :** La fonction n'est pas Lebesgue-intégrable. Le formalisme de Lebesgue (qui impose l'intégrabilité de $|f|$ par la séparation $f = f^+ - f^-$) est plus strict que l'intégrale de Riemann généralisée qui autorise des compensations infinies entre les aires positives et négatives.
