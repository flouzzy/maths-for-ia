---
title: "Exercice 2 : Règle de Leibniz"
difficulty: "$\star$$\star$$\circ$$\circ$$\circ$"
---
# Exercice 2 : Règle de Leibniz ($\star$$\star$$\circ$$\circ$$\circ$)

**Énoncé :**
Soit $F(x) = \int_{0}^{+\infty} \frac{e^{-xt}}{1+t^2} dt$.
Montrer que $F$ est de classe $\mathcal{C}^2$ sur $]0, +\infty[$ et trouver une relation différentielle liant $F$ et $F''$.

**Démonstration pas-à-pas :**
Considérons la fonction $f(x,t) = \frac{e^{-xt}}{1+t^2}$ pour $x > 0$ et $t \ge 0$.
1. L'application $(x,t) \mapsto f(x,t)$ est de classe $\mathcal{C}^2$ par rapport à $x$, avec :
   $\frac{\partial f}{\partial x}(x,t) = \frac{-t e^{-xt}}{1+t^2}$ et $\frac{\partial^2 f}{\partial x^2}(x,t) = \frac{t^2 e^{-xt}}{1+t^2}$.
2. Pour $x \ge a > 0$, on majore la dérivée seconde :
   $\left| \frac{\partial^2 f}{\partial x^2}(x,t) \right| = \frac{t^2}{1+t^2} e^{-xt} \le 1 \cdot e^{-at}$.
   La fonction $t \mapsto e^{-at}$ est intégrable sur $[0, +\infty[$.
3. Par le théorème de dérivation de Leibniz itéré, $F \in \mathcal{C}^2(]0, +\infty[)$ et :
   $F''(x) = \int_{0}^{+\infty} \frac{t^2 e^{-xt}}{1+t^2} dt$.
4. Relation différentielle :
   $F''(x) + F(x) = \int_{0}^{+\infty} \frac{t^2 e^{-xt} + e^{-xt}}{1+t^2} dt = \int_{0}^{+\infty} e^{-xt} \frac{t^2+1}{t^2+1} dt = \int_{0}^{+\infty} e^{-xt} dt = \left[ -\frac{1}{x} e^{-xt} \right]_0^{+\infty} = \frac{1}{x}$.
Ainsi, $F''(x) + F(x) = \frac{1}{x}$.
