# Exercice 7 : Approximation et norme infinie
**Énoncé :**
Montrer que $f_n(x) = \frac{\arctan(nx)}{\sqrt{n}}$ converge uniformément sur $\mathbb{R}$.

**Solution Rigoureuse :**
On évalue la borne supérieure directement.
La fonction arctangente est bornée sur $\mathbb{R}$ par $\frac{\pi}{2}$.
Ainsi, pour tout $x \in \mathbb{R}$ et tout $n \ge 1$ :
$$|f_n(x)| = \frac{|\arctan(nx)|}{\sqrt{n}} \le \frac{\pi}{2\sqrt{n}}$$
La limite simple est la fonction constante $0$.
L'évaluation de la norme infinie donne :
$$\|f_n - 0\|_{\infty, \mathbb{R}} = \sup_{x \in \mathbb{R}} \frac{|\arctan(nx)|}{\sqrt{n}} \le \frac{\pi}{2\sqrt{n}}$$
Puisque $\lim_{n \to +\infty} \frac{\pi}{2\sqrt{n}} = 0$, on a $\lim_{n \to +\infty} \|f_n\|_{\infty, \mathbb{R}} = 0$.
La convergence est donc **uniforme** sur la totalité de la droite réelle $\mathbb{R}$.
L'intérêt est que bien que la fonction arctangente possède des variations asymptotiques marquées, le dénominateur uniformément écrasant $\sqrt{n}$ force la convergence globale.
