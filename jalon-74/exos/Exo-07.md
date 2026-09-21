---
title: "Exercice 7 : Cas d'égalité dans Hölder"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 7 : Cas d'égalité dans Hölder

## Énoncé
Soient $p, q > 1$ conjugués, $f \in L^p, g \in L^q$ non nulles. Montrer que l'égalité $\int |fg| = \|f\|_p \|g\|_q$ a lieu si et seulement s'il existe $\alpha, \beta > 0$ tels que $\alpha |f|^p = \beta |g|^q$ presque partout.

## Corrigé
L'égalité dans Hölder se produit ssi l'égalité a lieu dans l'inégalité de Young ponctuelle $a(x)b(x) \le \frac{a(x)^p}{p} + \frac{b(x)^q}{q}$ pp, où $a(x) = \frac{|f(x)|}{\|f\|_p}$ et $b(x) = \frac{|g(x)|}{\|g\|_q}$.
L'inégalité de Young est une égalité ssi $a(x)^p = b(x)^q$.
Donc $\frac{|f(x)|^p}{\|f\|_p^p} = \frac{|g(x)|^q}{\|g\|_q^q}$ pp.
Ceci s'écrit $\|g\|_q^q |f|^p = \|f\|_p^p |g|^q$ pp.
Posons $\alpha = \|g\|_q^q > 0$ et $\beta = \|f\|_p^p > 0$. On a bien $\alpha |f|^p = \beta |g|^q$ pp.
Réciproquement, s'il existe de tels $\alpha, \beta$, alors $|f|^p$ est proportionnel à $|g|^q$. On intègre et on retrouve l'égalité dans Hölder.
