# Exercice 9 : Opérateur intégral de Volterra
$\bigstar$\bigstar$\bigstar$\bigstar$\bigstar$

**Énoncé :**
Soit $E = \mathcal{C}([0,1])$ et $V(f)(x) = \int_0^x f(t)dt$. Montrer que $\|V^n\| \le \frac{1}{n!}$ et en déduire que $I-V$ est inversible.

**Correction Détaillée :**
1. Par récurrence, on montre que $|V^n(f)(x)| \le \|f\|_\infty \frac{x^n}{n!}$.
2. Pour $n=1$, c'est l'exercice classique. Si c'est vrai pour $n$, $|V^{n+1}(f)(x)| \le \int_0^x \|f\|_\infty \frac{t^n}{n!} dt = \|f\|_\infty \frac{x^{n+1}}{(n+1)!}$.
3. Donc $\|V^n\| \le \frac{1}{n!}$.
4. La série $\sum \|V^n\| \le \sum \frac{1}{n!} = e < \infty$. Elle converge dans $\mathcal{L}(E)$. Son inverse est $(I-V)^{-1} = \sum_{n=0}^\infty V^n$.
