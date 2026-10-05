# Exercice 1 : La fonction de Heaviside

\subsection*{Exercice 1 : La fonction de Heaviside \quad $\bigstar\star\star\star\star$}

**Énoncé :**
Soit $H$ la fonction de Heaviside définie par $H(x) = 1$ si $x > 0$ et $H(x) = 0$ sinon. Montrer que $H$ définit une distribution régulière et expliciter son action sur une fonction test $\phi \in \mathcal{D}(\mathbb{R})$.

**Démonstration pas à pas :**
1. **Intégrabilité locale :** $H$ est mesurable et bornée, donc sur tout compact $K$, $\int_K |H(x)| dx \le \int_K 1 dx < +\infty$. Ainsi, $H \in L^1_{loc}(\mathbb{R})$.
2. **Action sur $\phi$ :** Par définition d'une distribution régulière, on a pour toute $\phi \in \mathcal{D}(\mathbb{R})$ :
   $$ \langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x) \phi(x) dx = \int_0^{+\infty} 1 \cdot \phi(x) dx = \int_0^{+\infty} \phi(x) dx $$
3. **Continuité :** Si $\phi_n \to 0$ dans $\mathcal{D}(\mathbb{R})$, il existe $K$ contenant les supports. L'intégrale devient $\int_{K \cap [0, +\infty[} \phi_n(x) dx$, qui tend vers 0 par convergence uniforme.
**Conclusion :** $T_H$ est bien une distribution régulière, son action est l'intégrale de la fonction test sur $[0, +\infty[$. $\blacksquare$
