---
title: "Exercice 8 : Transformation de Laplace"
difficulty: "$\star$$\star$$\star$$\star$$\star$"
---
# Exercice 8 : Transformation de Laplace ($\star$$\star$$\star$$\star$$\star$)

**Énoncé :**
Soit $F(p) = \int_0^{+\infty} e^{-pt} f(t) dt$.
Si $f$ est continue et bornée par $M$ sur $\mathbb{R}^+$, montrer que $F$ est de classe $\mathcal{C}^\infty$ sur $]0, +\infty[$ et donner l'expression de $F^{(n)}(p)$.

**Démonstration pas-à-pas :**
1. Notons $g(p,t) = e^{-pt} f(t)$.
2. $g$ est indéfiniment dérivable par rapport à $p$, et $\frac{\partial^n g}{\partial p^n}(p,t) = (-t)^n e^{-pt} f(t)$.
3. Soit $K = [a, +\infty[$ un segment avec $a > 0$. Pour $p \ge a$, on a :
   $\left| \frac{\partial^n g}{\partial p^n}(p,t) \right| = t^n e^{-pt} |f(t)| \le M t^n e^{-at}$.
4. La fonction $\psi_n(t) = M t^n e^{-at}$ est intégrable sur $]0, +\infty[$ car $e^{-at}$ l'emporte sur toute puissance de $t$.
5. La domination étant vérifiée sur tout sous-intervalle $[a, +\infty[ \subset ]0, +\infty[$, on peut appliquer le théorème de Leibniz à l'ordre $n$.
6. On conclut que $F$ est de classe $\mathcal{C}^\infty$ sur $]0, +\infty[$ et $F^{(n)}(p) = \int_0^{+\infty} (-t)^n e^{-pt} f(t) dt$.
