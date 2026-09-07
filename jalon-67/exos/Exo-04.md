# Exercice 4 : Série de fonctions positives intégrables \quad $\bigstar\bigstar\star\star\star$

Calculer $\int_0^\infty \sum_{n=1}^\infty e^{-nx} dx$.

**Correction :**
Posons $u_n(x) = e^{-nx} \ge 0$. Par TCM, $\int_0^\infty \sum e^{-nx} dx = \sum \int_0^\infty e^{-nx} dx = \sum \frac{1}{n}$, qui diverge. Alternativement, $\sum e^{-nx} = \frac{e^{-x}}{1 - e^{-x}}$. L'intégrale de cette limite diverge en $0$ car $\sim \frac{1}{x}$ en 0.
