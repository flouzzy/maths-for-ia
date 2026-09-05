# Exercice 1 : Intégration terme à terme d'une série positive \quad $\bigstar\star\star\star\star$

Soit $I = \int_{0}^{1} \sum_{n=1}^{\infty} x^n dx$.

**Question :** Montrer que cette intégrale vaut $+\infty$ en utilisant le théorème de convergence monotone.

**Solution Détaillée :**
1. Pour tout $n \in \mathbb{N}^*$, posons $u_n(x) = x^n$. Les fonctions $u_n$ sont mesurables et positives sur l'intervalle $[0, 1]$ muni de la tribu borélienne.
2. Le corollaire du théorème de Beppo Levi (ou convergence monotone pour les séries) stipule que pour une suite de fonctions mesurables positives, on peut intervertir le signe somme et l'intégrale de Lebesgue :
   $$ \int_{0}^{1} \left( \sum_{n=1}^{\infty} u_n(x) \right) dx = \sum_{n=1}^{\infty} \int_{0}^{1} u_n(x) dx $$
3. Calculons l'intégrale de chaque terme. Comme $x \mapsto x^n$ est continue, son intégrale de Lebesgue coïncide avec son intégrale de Riemann :
   $$ \int_{0}^{1} x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_{0}^{1} = \frac{1}{n+1} $$
4. La somme devient donc :
   $$ \sum_{n=1}^{\infty} \frac{1}{n+1} = \sum_{k=2}^{\infty} \frac{1}{k} $$
5. Il s'agit du reste de la série harmonique. Or, la série de terme général $\frac{1}{k}$ est divergente. Sa somme est donc $+\infty$.
6. Conclusion : $I = +\infty$.
