# Exercice 6 : Produit de convolution de fonctions L2
**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soient $f, g \in L^2(\mathbb{R})$. On pose $h(x) = (f * g)(x) = \int_{-\infty}^\infty f(x-t)g(t) dt$.
Montrer que $h$ est continue, bornée, et que sa transformée de Fourier, si on la définit au sens de l'analyse fonctionnelle, correspond au produit des transformées.

**Correction :**
1. Cauchy-Schwarz : $|h(x)| \leq \int |f(x-t)||g(t)| dt \leq \|f(x-\cdot)\|_2 \|g\|_2 = \|f\|_2 \|g\|_2$. Donc $h$ est bien définie et bornée par $\|f\|_2 \|g\|_2$.
2. Continuité : $h(x+a) - h(x) = \int (f(x+a-t) - f(x-t))g(t) dt$. Par Cauchy-Schwarz, $|h(x+a)-h(x)| \leq \|\tau_{-a}f - f\|_2 \|g\|_2$. La continuité des translations dans $L^2$ implique que ceci tend vers 0 quand $a \to 0$, donc $h$ est uniformément continue.
3. Théorème de Fubini étendu : Par l'identité de Parseval, $h(x) = \langle \tau_x \tilde{f}, \overline{g} \rangle = \frac{1}{2\pi} \langle \mathcal{F}(\tau_x \tilde{f}), \mathcal{F}(\overline{g}) \rangle$, ce qui permet de relier $\hat{h}$ au produit ponctuel $\hat{f} \cdot \hat{g}$.
