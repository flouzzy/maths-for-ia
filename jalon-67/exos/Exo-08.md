# Exercice 8 : L'intégrale de Gauss revisitée

**Difficulté :** $\bigstar$$\bigstar$$\bigstar$$\bigstar$$\star$

## Énoncé
En utilisant $f_n(x) = (1 - x^2/n)^n \mathbf{1}_{[0, \sqrt{n}]}(x)$ sur $\mathbb{R}_+$, prouver que $\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$.

## Correction Détaillée
1. La suite $f_n$ est croissante (par étude de fonction) et positive.
2. Elle converge ponctuellement vers $e^{-x^2}$.
3. Par Beppo-Levi, la limite des intégrales (qui donne des intégrales de Wallis) est l'intégrale de la gaussienne.
