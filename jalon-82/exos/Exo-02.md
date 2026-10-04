\subsection*{Exercice 2 : La fonction de Heaviside \quad $\bigstar\star\star\star\star$}

Soit la fonction de Heaviside $H(x) = 1$ si $x \ge 0$ et $H(x) = 0$ si $x < 0$.
1. Justifier que $H$ définit une distribution régulière $T_H$.
2. Évaluer $\langle T_H, \phi \rangle$ pour une fonction test générale $\phi \in \mathcal{D}(\mathbb{R})$.

**Correction Détaillée :**
1. Pour qu'une fonction $f$ définisse une distribution régulière, il faut et il suffit qu'elle soit localement intégrable, c'est-à-dire $f \in L^1_{loc}(\mathbb{R})$.
Pour tout compact $K = [a, b]$ de $\mathbb{R}$, on a :
$\int_K |H(x)| dx = \int_a^b |H(x)| dx$.
Puisque $0 \le H(x) \le 1$, l'intégrale est majorée par $b-a$, qui est fini. Donc $H \in L^1_{loc}(\mathbb{R})$ et $H$ définit bien une distribution régulière $T_H$.
2. L'action de $T_H$ sur une fonction test $\phi \in \mathcal{D}(\mathbb{R})$ est donnée par :
$\langle T_H, \phi \rangle = \int_{-\infty}^{+\infty} H(x) \phi(x) dx$
Comme $H(x) = 0$ sur $]-\infty, 0[$ et $H(x) = 1$ sur $[0, +\infty[$, on obtient :
$\langle T_H, \phi \rangle = \int_0^{+\infty} 1 \cdot \phi(x) dx = \int_0^{+\infty} \phi(x) dx$.
Puisque $\phi$ est à support compact, l'intégrale converge (elle se réduit en fait à une intégrale sur un segment fermé et borné). $\blacksquare$
