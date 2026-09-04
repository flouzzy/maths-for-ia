# Exercice 03 : Série d'intégrales rationnelles ($\bigstar$$\bigstar$$\star$$\star$$\star$)

## Énoncé

Prouver que $\int_0^\infty \frac{1}{e^x - 1} \,dx = +\infty$, puis justifier que $\int_0^\infty \frac{x}{e^x - 1} \,dx = \frac{\pi^2}{6}$.

## Correction Détaillée

1. **Développement en série :** On écrit $\frac{x}{e^x - 1} = \frac{x e^{-x}}{1 - e^{-x}}$. Pour $x > 0$, $e^{-x} \in ]0, 1[$, on peut utiliser le développement de la série géométrique : $\frac{1}{1 - e^{-x}} = \sum_{n=0}^\infty e^{-nx}$. Donc $\frac{x}{e^x - 1} = \sum_{n=0}^\infty x e^{-(n+1)x} = \sum_{n=1}^\infty x e^{-nx}$.
2. **Application de Beppo Levi :** Les fonctions $u_n(x) = x e^{-nx}$ sont continues (donc mesurables) et positives sur $]0, +\infty[$. Le corollaire de Beppo Levi s'applique :
   $$ \int_0^\infty \sum_{n=1}^\infty x e^{-nx} \,dx = \sum_{n=1}^\infty \int_0^\infty x e^{-nx} \,dx $$
3. **Calcul de l'intégrale :** Par intégration par parties : $\int_0^\infty x e^{-nx} \,dx = \left[ -\frac{x}{n}e^{-nx} \right]_0^\infty + \int_0^\infty \frac{1}{n} e^{-nx} \,dx = 0 + \left[ -\frac{1}{n^2}e^{-nx} \right]_0^\infty = \frac{1}{n^2}$.
4. **Sommation finale :** L'intégrale vaut donc $\sum_{n=1}^\infty \frac{1}{n^2}$, qui est un résultat classique de la fonction Zêta de Riemann, $\zeta(2) = \frac{\pi^2}{6}$.
5. **Première question :** Par le même procédé, $\int_0^\infty \frac{1}{e^x - 1} \,dx = \sum_{n=1}^\infty \int_0^\infty e^{-nx} \,dx = \sum_{n=1}^\infty \frac{1}{n} = +\infty$ (série harmonique).
