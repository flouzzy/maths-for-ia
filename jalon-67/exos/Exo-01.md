# Exercice 1 : Application directe : Intégrale et Série entière

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Montrer que pour tout $x \in ]-1, 1[$, on a :
$$\int_0^x \frac{1}{1-t} dt = \sum_{n=1}^\infty \frac{x^n}{n}$$
en utilisant le théorème de convergence monotone pour justifier l'inversion somme-intégrale.

**Solution Détaillée :**
1. Pour $t \in [0, x]$ avec $x \in [0, 1[$, on a $|t| < 1$. On connaît le développement en série entière :
$$\frac{1}{1-t} = \sum_{n=0}^\infty t^n$$
2. Considérons la suite de fonctions $u_n(t) = t^n$ sur $[0, x]$.
3. Sur l'intervalle d'intégration, $t \ge 0$, donc les fonctions $u_n(t)$ sont des fonctions mesurables **positives**.
4. D'après le corollaire du Théorème de Convergence Monotone pour les séries à termes positifs, on peut intervertir le signe somme et le signe intégral :
$$\int_0^x \left(\sum_{n=0}^\infty t^n\right) dt = \sum_{n=0}^\infty \int_0^x t^n dt$$
5. Calculons l'intégrale pour chaque $n$ :
$$\int_0^x t^n dt = \left[ \frac{t^{n+1}}{n+1} \right]_0^x = \frac{x^{n+1}}{n+1}$$
6. Ainsi, la somme devient :
$$\sum_{n=0}^\infty \frac{x^{n+1}}{n+1} = \sum_{k=1}^\infty \frac{x^k}{k}$$
7. Or l'intégrale directe donne $\int_0^x \frac{1}{1-t} dt = [-\ln(1-t)]_0^x = -\ln(1-x)$.
Ceci permet de retrouver le développement en série entière classique de $-\ln(1-x)$. La justification est impeccable grâce au TCM. Pour $x < 0$, la croissance simple est perdue, il faudrait utiliser la convergence dominée ou séparer la série en parties positives et négatives.
