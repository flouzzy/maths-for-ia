---
title: "Exercice 3 : Généralisation de l'inégalité de Young avec epsilon"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 3 : Généralisation de l'inégalité de Young avec epsilon

## Énoncé
Soient $p, q > 1$ conjugués, $a, b \ge 0$ et $\epsilon > 0$. Démontrer l'inégalité de Young avec $\epsilon$ :
$$ a b \le \epsilon \frac{a^p}{p} + \frac{b^q}{q \epsilon^{q/p}} $$

## Corrigé
On part de l'inégalité de Young classique : $XY \le \frac{X^p}{p} + \frac{Y^q}{q}$.
Posons $X = \epsilon^{1/p} a$ et $Y = \epsilon^{-1/p} b$.
On a $XY = \epsilon^{1/p} a \epsilon^{-1/p} b = ab$.
De plus, $X^p = (\epsilon^{1/p} a)^p = \epsilon a^p$.
Et $Y^q = (\epsilon^{-1/p} b)^q = \epsilon^{-q/p} b^q$.
En remplaçant dans l'inégalité de Young classique, on obtient :
$$ a b \le \frac{\epsilon a^p}{p} + \frac{\epsilon^{-q/p} b^q}{q} = \epsilon \frac{a^p}{p} + \frac{b^q}{q \epsilon^{q/p}} $$
C'est le résultat demandé. Cette forme est très utile dans l'étude des EDP pour "absorber" des termes de gradient.
