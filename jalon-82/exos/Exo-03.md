\subsection*{Exercice 3 : Distribution régulière de la fonction signe \quad $\bigstar\bigstar\star\star\star$}

**Énoncé :**
Soit la fonction $\text{sgn}(x)$ qui vaut $1$ si $x > 0$, $-1$ si $x < 0$ et $0$ si $x=0$. Montrer qu'elle définit une distribution régulière et exprimer son action sur $\phi \in \mathcal{D}(\mathbb{R})$.

**Correction :**
La fonction $\text{sgn}$ est constante par morceaux et bornée sur $\mathbb{R}$. Elle est donc localement intégrable, c'est-à-dire que sur tout intervalle compact $[a,b]$, l'intégrale $\int_a^b |\text{sgn}(x)| dx \le b - a < +\infty$.
Elle définit ainsi une distribution régulière $T_{\text{sgn}}$ :
$$\langle T_{\text{sgn}}, \phi \rangle = \int_{-\infty}^{+\infty} \text{sgn}(x) \phi(x) dx$$
Puisque le support de $\phi$ est compact, l'intégrale est bien définie. On peut découper l'intégrale en deux parties :
$$\langle T_{\text{sgn}}, \phi \rangle = \int_{-\infty}^0 (-1)\phi(x) dx + \int_0^{+\infty} (1)\phi(x) dx$$
$$\langle T_{\text{sgn}}, \phi \rangle = \int_0^{+\infty} \phi(x) dx - \int_{-\infty}^0 \phi(x) dx$$
