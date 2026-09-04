# Exercice 01 : Calcul d'une intégrale avec série géométrique ($\bigstar$$\star$$\star$$\star$$\star$)

## Énoncé

Calculer $\int_0^1 \sum_{n=0}^\infty (1-x)x^n \,dx$ en justifiant rigoureusement le passage à la limite sous l'intégrale.

## Correction Détaillée

1. Posons $u_n(x) = (1-x)x^n$. Pour tout $n \ge 0$, la fonction $u_n$ est mesurable (car continue) et positive sur $[0, 1]$.
2. Par le corollaire du théorème de Beppo Levi (sommation terme à terme de fonctions mesurables positives), on peut intervertir série et intégrale :
   $$ \int_0^1 \sum_{n=0}^\infty (1-x)x^n \,dx = \sum_{n=0}^\infty \int_0^1 (1-x)x^n \,dx $$
3. Calculons l'intégrale du terme général :
   $$ \int_0^1 (1-x)x^n \,dx = \int_0^1 (x^n - x^{n+1}) \,dx = \frac{1}{n+1} - \frac{1}{n+2} $$
4. La somme est alors une série télescopique :
   $$ \sum_{n=0}^\infty \left(\frac{1}{n+1} - \frac{1}{n+2}\right) = \lim_{N \to \infty} \sum_{n=0}^N \left(\frac{1}{n+1} - \frac{1}{n+2}\right) = \lim_{N \to \infty} \left(1 - \frac{1}{N+2}\right) = 1 $$
5. On vérifie également que la limite simple de la série est $\sum_{n=0}^\infty (1-x)x^n = (1-x)\frac{1}{1-x} = 1$ pour $x \in [0, 1[$, et $0$ pour $x=1$. L'intégrale de cette limite est bien $\int_0^1 1 \,dx = 1$. L'égalité est vérifiée.
