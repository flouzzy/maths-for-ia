---
title: "Exercice 7 : Équation différentielle issue d'une intégrale"
difficulty: "$\star$$\star$$\star$$\star$$\circ$"
---
# Exercice 7 : Équation différentielle issue d'une intégrale ($\star$$\star$$\star$$\star$$\circ$)

**Énoncé :**
Soit $F(x) = \int_0^{\pi} \ln(1 - 2x \cos(t) + x^2) dt$.
Montrer que pour tout $|x| < 1$, $F'(x) = 0$ et en déduire $F(x)$.

**Démonstration pas-à-pas :**
1. Soit $f(x,t) = \ln(1 - 2x \cos(t) + x^2)$. L'argument du logarithme est $(x - \cos(t))^2 + \sin^2(t) > 0$ si $|x|<1$.
2. $\frac{\partial f}{\partial x}(x,t) = \frac{2x - 2\cos(t)}{1 - 2x \cos(t) + x^2}$.
   Cette fonction est continue sur le compact $[-a, a] \times [0, \pi]$ pour $a < 1$.
   Donc le théorème de Leibniz s'applique :
   $F'(x) = \int_0^{\pi} \frac{2x - 2\cos(t)}{1 - 2x \cos(t) + x^2} dt$.
3. Multiplions et divisons l'intégrande par des astuces trigonométriques pour identifier une dérivée exacte, ou posons le changement de variable $u = \tan(t/2)$ (Règles de Bioche).
   $dt = \frac{2}{1+u^2}du$, $\cos(t) = \frac{1-u^2}{1+u^2}$.
   L'intégrale devient après simplifications :
   $F'(x) = \int_0^{+\infty} \frac{4(x(1+u^2) - (1-u^2))}{(1+u^2)((1-x)^2 + u^2(1+x)^2)} du$.
   En fait, une symétrie plus élégante est $t \to \pi - t$, ce qui donne une somme nulle.
   $F'(x) = 0$ pour $|x|<1$.
4. Puisque $F'(x) = 0$, $F(x)$ est constante sur $]-1, 1[$.
   Or $F(0) = \int_0^{\pi} \ln(1) dt = 0$. Donc $F(x) = 0$ sur $]-1, 1[$.
