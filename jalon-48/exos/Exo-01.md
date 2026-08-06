# Exercice 1 : Dérivation de la fonction Sigmoïde
**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé
Calculer la dérivée de la fonction d'activation sigmoïde $\sigma(x) = \frac{1}{1 + e^{-x}}$ et l'exprimer en fonction de $\sigma(x)$.

## Correction détaillée
1. On utilise la règle de dérivation d'un quotient. Soit $f(x) = 1 + e^{-x}$. Alors $\sigma(x) = \frac{1}{f(x)}$.
2. $\sigma'(x) = -\frac{f'(x)}{(f(x))^2}$.
3. La dérivée de $f(x)$ est $f'(x) = -e^{-x}$.
4. Donc, $\sigma'(x) = -\frac{-e^{-x}}{(1 + e^{-x})^2} = \frac{e^{-x}}{(1 + e^{-x})^2}$.
5. On réécrit le numérateur : $e^{-x} = (1 + e^{-x}) - 1$.
6. Ainsi, $\sigma'(x) = \frac{(1 + e^{-x}) - 1}{(1 + e^{-x})^2} = \frac{1 + e^{-x}}{(1 + e^{-x})^2} - \frac{1}{(1 + e^{-x})^2}$.
7. On simplifie : $\sigma'(x) = \frac{1}{1 + e^{-x}} - \left(\frac{1}{1 + e^{-x}}\right)^2$.
8. Finalement, en factorisant : $\sigma'(x) = \sigma(x) (1 - \sigma(x))$.
Cette propriété est cruciale pour optimiser le calcul du gradient lors de la rétropropagation.
