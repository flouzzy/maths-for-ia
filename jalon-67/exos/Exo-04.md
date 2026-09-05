# Exercice 4 : Fonction Gamma d'Euler \quad $\bigstar\bigstar\bigstar\star\star$

Soit la fonction Gamma définie par $\Gamma(x) = \int_{0}^{\infty} t^{x-1} e^{-t} dt$ pour $x > 0$.

**Question :** Montrer que $\Gamma$ est bien définie pour $x > 0$ en la voyant comme limite d'une suite croissante.

**Solution Détaillée :**
1. Soit la suite de fonctions $g_n(t) = t^{x-1} e^{-t} \mathbf{1}_{[1/n, n]}(t)$ pour $t > 0$.
2. Les fonctions $g_n$ sont positives et mesurables.
3. La suite d'intervalles $[1/n, n]$ est croissante pour l'inclusion. Ainsi, pour tout $t > 0$, la suite $(g_n(t))$ est croissante et converge vers $g(t) = t^{x-1} e^{-t}$.
4. Le théorème de convergence monotone s'applique :
   $$ \int_{0}^{\infty} t^{x-1} e^{-t} dt = \lim_{n \to \infty} \int_{1/n}^{n} t^{x-1} e^{-t} dt $$
5. Pour $x > 0$, l'intégrale de Riemann impropre converge en $0$ et en $+\infty$.
   - En $0$, $t^{x-1} e^{-t} \sim t^{x-1}$, intégrable car $x-1 > -1 \iff x > 0$.
   - En $+\infty$, $t^{x-1} e^{-t} = o(1/t^2)$, intégrable.
6. La convergence de l'intégrale de Riemann garantit que la limite existe et est finie pour tout $x > 0$.
