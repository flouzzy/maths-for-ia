# Exercice 02 : Intégrale de Gauss et fonctions Gamma ($\bigstar$$\star$$\star$$\star$$\star$)

## Énoncé

Soit $f_n(x) = \left(1 - \frac{x^2}{n}\right)^n \mathbf{1}_{[0, \sqrt{n}]}(x)$. Montrer que $(f_n)$ est une suite croissante de fonctions mesurables positives et calculer $\lim_{n \to \infty} \int_0^\infty f_n(x) \,dx$.

## Correction Détaillée

1. **Croissance :** Posons $\phi(t) = \ln(1-t) + \frac{t}{1-t}$ pour $t < 1$. $\phi'(t) = \frac{-1}{1-t} + \frac{1}{(1-t)^2} = \frac{t}{(1-t)^2} > 0$ pour $t \in ]0, 1[$. Puisque $\phi(0) = 0$, $\phi(t) > 0$. On a $\ln(1 - \frac{x^2}{n}) - \ln(1 - \frac{x^2}{n+1})$. Un raisonnement plus simple consiste à utiliser l'inégalité de Bernoulli : pour $x \in [0, \sqrt{n}]$, $1 - \frac{x^2}{n} \le (1 - \frac{x^2}{n+1})^{\frac{n+1}{n}}$. Élevant à la puissance $n$, on obtient $f_n(x) \le f_{n+1}(x)$.
2. **Limite simple :** Pour tout $x \ge 0$, pour $n$ assez grand ($n > x^2$), $f_n(x) = (1 - \frac{x^2}{n})^n = \exp(n \ln(1 - \frac{x^2}{n})) = \exp(n (-\frac{x^2}{n} + o(\frac{1}{n}))) \to e^{-x^2}$.
3. **Beppo Levi :** La suite $(f_n)$ étant croissante de fonctions mesurables positives vers $x \mapsto e^{-x^2}$, le théorème de convergence monotone s'applique :
   $$ \lim_{n \to \infty} \int_0^\infty f_n(x) \,dx = \int_0^\infty \lim_{n \to \infty} f_n(x) \,dx = \int_0^\infty e^{-x^2} \,dx $$
4. **Conclusion :** L'intégrale de Gauss donne $\int_0^\infty e^{-x^2} \,dx = \frac{\sqrt{\pi}}{2}$. Ainsi, $\lim_{n \to \infty} \int_0^\sqrt{n} (1 - \frac{x^2}{n})^n \,dx = \frac{\sqrt{\pi}}{2}$.
