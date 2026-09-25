# Exercice 10 : Lemme de Riemann-Lebesgue par densité $\star\star\star\star\star$

**Énoncé :**
Montrer que pour toute fonction $f \in L^1(\mathbb{R})$, la transformée de Fourier $\widehat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-ix\xi} \, dx$ tend vers $0$ lorsque $|\xi| \to +\infty$.

**Correction détaillée :**
1. **Étape 1 : Cas des fonctions indicatrices de segments.**
Soit $f = \mathbf{1}_{[a, b]}$. Calculons directement sa transformée :
$\widehat{f}(\xi) = \int_a^b e^{-ix\xi} \, dx = \left[ \frac{e^{-ix\xi}}{-i\xi} \right]_a^b = \frac{e^{-ib\xi} - e^{-ia\xi}}{-i\xi}$.
On a $|\widehat{f}(\xi)| \le \frac{|e^{-ib\xi}| + |e^{-ia\xi}|}{|\xi|} = \frac{2}{|\xi|}$.
Il est immédiat que $\lim_{|\xi| \to \infty} \widehat{f}(\xi) = 0$.
2. **Étape 2 : Linéarité sur les fonctions étagées.**
Si $s$ est une fonction étagée intégrable, elle s'écrit comme somme finie $s = \sum_{j=1}^n c_j \mathbf{1}_{I_j}$ où les $I_j$ sont des intervalles.
Par linéarité de la transformée de Fourier, $\widehat{s}(\xi) = \sum c_j \widehat{\mathbf{1}_{I_j}}(\xi)$.
Comme une somme finie de limites nulles est nulle, $\lim_{|\xi| \to \infty} \widehat{s}(\xi) = 0$.
3. **Étape 3 : Conclusion par densité.**
Soit $f \in L^1(\mathbb{R})$ quelconque et soit $\varepsilon > 0$. Par la densité des fonctions étagées dans $L^1(\mathbb{R})$, il existe une fonction étagée intégrable $s$ telle que $\|f - s\|_1 < \frac{\varepsilon}{2}$.
Observons que pour toute fonction $g \in L^1(\mathbb{R})$, $|\widehat{g}(\xi)| \le \int_{\mathbb{R}} |g(x)| |e^{-ix\xi}| \, dx = \int_{\mathbb{R}} |g(x)| \times 1 \, dx = \|g\|_1$.
Ainsi, $|\widehat{f}(\xi) - \widehat{s}(\xi)| = |\widehat{f-s}(\xi)| \le \|f - s\|_1 < \frac{\varepsilon}{2}$.
De plus, d'après l'étape 2, il existe un réel $M > 0$ tel que pour tout $|\xi| > M$, $|\widehat{s}(\xi)| < \frac{\varepsilon}{2}$.
Par l'inégalité triangulaire :
$$ |\widehat{f}(\xi)| \le |\widehat{f}(\xi) - \widehat{s}(\xi)| + |\widehat{s}(\xi)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon \quad \text{pour } |\xi| > M $$
Ceci prouve formellement la limite $\lim_{|\xi| \to \infty} \widehat{f}(\xi) = 0$ pour toute fonction intégrable, bouclant ainsi la preuve du Lemme de Riemann-Lebesgue. $\blacksquare$
