# Exercice 06 : Intégrale de la partie fractionnaire ($\bigstar$$\bigstar$$\bigstar$$\star$$\star$)

## Énoncé

Calculer $\lim_{n \to \infty} \int_0^n \left(x - \lfloor x \rfloor\right) e^{-x} \,dx$ avec Beppo Levi.

## Correction Détaillée

1. **Suite de fonctions :** Posons $f_n(x) = (x - \lfloor x \rfloor) e^{-x} \mathbf{1}_{[0, n]}(x)$.
2. **Positivité et Croissance :** La fonction $x - \lfloor x \rfloor$ est la partie fractionnaire, strictement positive sur $\mathbb{R} \setminus \mathbb{Z}$ et bornée par 1. $e^{-x}$ est positive. Donc $f_n \ge 0$. De plus, $f_n(x) \le f_{n+1}(x)$ car on multiplie par l'indicatrice d'un intervalle qui s'agrandit. La suite est donc croissante.
3. **Limite simple :** $f(x) = \lim_{n \to \infty} f_n(x) = (x - \lfloor x \rfloor) e^{-x} \mathbf{1}_{[0, +\infty[}(x)$.
4. **TCM :** Par Beppo Levi, $\int_0^\infty f(x) \,dx = \lim_{n \to \infty} \int_0^n f_n(x) \,dx$.
5. **Calcul explicite :** $\int_0^\infty (x - \lfloor x \rfloor) e^{-x} \,dx = \sum_{k=0}^\infty \int_k^{k+1} (x - k) e^{-x} \,dx$.
6. **Changement de variable :** Dans chaque intégrale, on pose $t = x - k$, $dx = dt$.
   $\int_k^{k+1} (x - k) e^{-x} \,dx = \int_0^1 t e^{-(t+k)} \,dt = e^{-k} \int_0^1 t e^{-t} \,dt$.
7. **Sommation :** On factorise la somme :
   $$ \left( \sum_{k=0}^\infty e^{-k} \right) \int_0^1 t e^{-t} \,dt = \frac{1}{1 - e^{-1}} \cdot \left[ -t e^{-t} - e^{-t} \right]_0^1 = \frac{e}{e-1} \cdot (1 - 2e^{-1}) = \frac{e-2}{e-1} $$
