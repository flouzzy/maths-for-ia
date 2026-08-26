---
title: "Exercice 10 : Absolue continuité de l'intégrale"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Absolue continuité de l'intégrale

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

Soit $f \in \mathcal{M}_+$ telle que $\int_X f \, d\mu < +\infty$.
Prouver que pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que pour tout ensemble mesurable $A$ avec $\mu(A) < \delta$, on a $\int_A f \, d\mu < \epsilon$.
(C'est la propriété fondamentale d'absolue continuité de l'intégrale de Lebesgue).

### Correction détaillée

1. L'hypothèse indique que $f$ est intégrable. Soit $\epsilon > 0$.
2. Par définition de l'intégrale de $f$ (qui est finie), il existe une fonction simple positive $s \in \mathcal{E}_+$ telle que $0 \le s \le f$ et :
   $$ \int_X f \, d\mu - \int_X s \, d\mu < \frac{\epsilon}{2} $$
   Par linéarité (et car les quantités sont finies), $\int_X (f - s) \, d\mu < \frac{\epsilon}{2}$.
3. La fonction simple s'écrit $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{E_i}$. Notons $M = \max_{1 \le i \le n} \alpha_i$. Ainsi, $s \le M$ uniformément sur $X$.
4. Posons $\delta = \frac{\epsilon}{2M}$ (si $M=0$, le résultat est trivial).
5. Soit $A$ un sous-ensemble mesurable tel que $\mu(A) < \delta$.
6. Écrivons la décomposition de l'intégrale sur $A$ :
   $$ \int_A f \, d\mu = \int_A (f - s + s) \, d\mu = \int_A (f - s) \, d\mu + \int_A s \, d\mu $$
7. Majorons le premier terme :
   Comme $f - s \ge 0$ partout, l'intégrale sur $A$ est inférieure ou égale à l'intégrale sur $X$ tout entier (monotonie et positivité).
   $$ \int_A (f - s) \, d\mu \le \int_X (f - s) \, d\mu < \frac{\epsilon}{2} $$
8. Majorons le second terme :
   Puisque $s \le M$, par monotonie :
   $$ \int_A s \, d\mu \le \int_A M \, d\mu = M \cdot \mu(A) $$
   Or $\mu(A) < \delta = \frac{\epsilon}{2M}$, donc $M \cdot \mu(A) < M \cdot \frac{\epsilon}{2M} = \frac{\epsilon}{2}$.
9. En sommant les deux majorations :
   $$ \int_A f \, d\mu < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon $$
La démonstration est terminée, établissant une puissante propriété de contrôle continu de l'intégrale.
