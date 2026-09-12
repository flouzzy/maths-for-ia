## Exercice 10 : Différence entre intégrale de Lebesgue et valeur principale de Cauchy \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Soit $f(x) = \frac{1}{x}$ pour $x \in [-1, 1] \setminus \{0\}$.
1. Calculer $\lim_{\epsilon \to 0^+} \left( \int_{-1}^{-\epsilon} \frac{1}{x} dx + \int_{\epsilon}^{1} \frac{1}{x} dx \right)$ (Valeur principale de Cauchy).
2. Montrer que $f$ n'est pas intégrable au sens de Lebesgue sur $[-1, 1]$.

**Correction :**
1. On calcule la valeur principale de Cauchy :
   $VP = \lim_{\epsilon \to 0^+} \left( [\ln |x|]_{-1}^{-\epsilon} + [\ln |x|]_{\epsilon}^{1} \right)$
   $VP = \lim_{\epsilon \to 0^+} \left( \ln(\epsilon) - \ln(1) + \ln(1) - \ln(\epsilon) \right) = \lim_{\epsilon \to 0^+} (0) = 0$.
2. Pour que $f$ soit intégrable au sens de Lebesgue, il faut que l'intégrale de la valeur absolue soit finie :
   $\int_{[-1, 1]} \left| \frac{1}{x} \right| dx = 2 \int_{0}^{1} \frac{1}{x} dx$.
   L'intégrale de Riemann généralisée $\int_{0}^{1} \frac{1}{x} dx = [\ln x]_0^1$ diverge vers l'infini.
   Donc $\int |f| dx = +\infty$. $f \notin \mathcal{L}^1([-1, 1])$.
L'intégrale de Lebesgue exige la convergence absolue, ce qui évite les compensations artificielles de l'infini avec l'infini (comme dans la valeur principale).
