# Exercice 10 : Complétude et Séries de Fonctions (Prélude à Riesz-Fischer)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Dans l'espace vectoriel normé $L^1([0,1])$, on considère une suite de fonctions $(f_n)$ définie par :
$$ f_n(x) = \sum_{k=1}^n \frac{1}{k^2 \sqrt{x}} \mathbf{1}_{]0, 1]}(x) $$

1. Montrer que chaque $f_n \in L^1([0,1])$.
2. Montrer que la suite $(f_n)$ est de Cauchy dans $L^1([0,1])$.
3. Déterminer la limite $f$ vers laquelle cette suite converge en norme $L^1$, et montrer que $f \in L^1$.

---

## Correction détaillée

1. **Intégrabilité de $f_n$ :**
   $f_n$ est une somme finie de fonctions. Posons $g(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{]0, 1]}(x)$.
   $$ \|g\|_1 = \int_0^1 x^{-1/2} \, dx = 2 < +\infty $$
   Donc $g \in L^1$. Comme $f_n = (\sum_{k=1}^n \frac{1}{k^2}) g$, et que l'espace $L^1$ est vectoriel, $f_n \in L^1$.

2. **Suite de Cauchy dans $L^1$ :**
   Pour $m > n$, évaluons la norme de la différence :
   $$ \|f_m - f_n\|_1 = \left\| \sum_{k=n+1}^m \frac{1}{k^2} g \right\|_1 = \sum_{k=n+1}^m \frac{1}{k^2} \|g\|_1 = 2 \sum_{k=n+1}^m \frac{1}{k^2} $$
   La série numérique $\sum \frac{1}{k^2}$ est convergente (série de Riemann avec $\alpha = 2 > 1$). Par le critère de Cauchy pour les séries numériques, la quantité $\sum_{k=n+1}^m \frac{1}{k^2}$ tend vers $0$ lorsque $n, m \to +\infty$.
   Donc $\|f_m - f_n\|_1 \to 0$. La suite $(f_n)$ est bien une suite de Cauchy dans $L^1$.

3. **Limite dans $L^1$ :**
   La limite naturelle ponctuelle de la suite est $f(x) = (\sum_{k=1}^\infty \frac{1}{k^2}) g(x) = \frac{\pi^2}{6} g(x)$.
   Vérifions que $f \in L^1$ :
   $$ \|f\|_1 = \frac{\pi^2}{6} \|g\|_1 = \frac{\pi^2}{6} \times 2 = \frac{\pi^2}{3} < +\infty $$
   Vérifions la convergence en norme $L^1$ :
   $$ \|f - f_n\|_1 = \left\| \left(\sum_{k=n+1}^\infty \frac{1}{k^2}\right) g \right\|_1 = \left(\sum_{k=n+1}^\infty \frac{1}{k^2}\right) \times 2 $$
   Le reste d'une série convergente tend vers 0, donc $\lim_{n \to \infty} \|f - f_n\|_1 = 0$.
   Cet exercice illustre le fait qu'une série de Cauchy d'éléments de $L^1$ converge bien vers un élément de $L^1$. Ce sera l'objet du théorème de Riesz-Fischer (Jalon 75) qui prouve que les espaces $L^p$ sont complets (espaces de Banach).
