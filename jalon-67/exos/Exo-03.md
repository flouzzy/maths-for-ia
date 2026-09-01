# Exercice 3 : Intégrale sur un intervalle infini

**Difficulté :** $\bigstar\bigstar\star$

**Énoncé :**
Calculer $\lim_{n \to \infty} \int_0^n (1-\frac{x}{n})^n e^{x/2} \mathbb{I}_{[0,n]}(x) dx$.

**Correction :**
Soit $f_n(x) = (1-\frac{x}{n})^n e^{x/2} \mathbb{I}_{[0,n]}(x)$. Pour $0 \leq x \leq n$, $f_n(x) \geq 0$. On sait que $(1-\frac{x}{n})^n \uparrow e^{-x}$. La suite $f_n$ est donc croissante et converge vers $f(x) = e^{-x} e^{x/2} = e^{-x/2}$. Par le théorème de Beppo Levi, la limite des intégrales est $\int_0^\infty e^{-x/2} dx = [-2e^{-x/2}]_0^\infty = 2$. $\blacksquare$
