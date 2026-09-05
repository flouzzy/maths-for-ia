# Exercice 1 : Application directe : Intégrale d'une série géométrique
**Difficulté :** $\bigstar\star\star\star\star$

### Énoncé

Soit l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. En justifiant soigneusement toutes les étapes, calculer $\int_0^1 \left( \sum_{n=1}^{+\infty} x^n \right) d\lambda(x)$.

---
### Correction détaillée

1. Posons pour $n \ge 1$ les fonctions $u_n(x) = x^n$ sur $[0, 1]$.
2. Pour tout $x \in [0, 1]$, $u_n(x)$ est mesurable (car continue) et $u_n(x) \ge 0$.
3. Le corollaire du Théorème de Convergence Monotone de Beppo Levi pour les séries de fonctions positives s'applique.
4. Nous pouvons donc intervertir le signe somme et le signe intégrale :
   $$\int_0^1 \left( \sum_{n=1}^{+\infty} x^n \right) d\lambda(x) = \sum_{n=1}^{+\infty} \int_0^1 x^n \, d\lambda(x)$$
5. Or l'intégrale de Riemann coïncide avec l'intégrale de Lebesgue pour les fonctions continues sur un segment :
   $$\int_0^1 x^n \, d\lambda(x) = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}$$
6. La somme devient donc :
   $$\sum_{n=1}^{+\infty} \frac{1}{n+1} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \ldots$$
7. Il s'agit de la série harmonique (privée de son premier terme), dont la divergence vers $+\infty$ est bien connue.
8. Par conséquent, $\int_0^1 \left( \sum_{n=1}^{+\infty} x^n \right) d\lambda(x) = +\infty$.
